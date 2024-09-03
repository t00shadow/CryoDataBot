import contextlib
import logging
import sys
from abc import ABC, abstractmethod
from queue import Queue

from PyQt5 import QtTest
from PyQt5.QtCore import PYQT_VERSION_STR, pyqtSignal, pyqtSlot, QObject, Qt, QT_VERSION_STR, QThread
from PyQt5.QtWidgets import QApplication, QPlainTextEdit, QProgressBar, QToolButton, QVBoxLayout, QWidget


__CONFIGURED = False


def setup_streams_redirection(tqdm_nb_columns=None):
    if not __CONFIGURED:
        tqdm_update_queue = Queue()
        perform_tqdm_default_out_stream_hack(tqdm_update_queue=tqdm_update_queue, tqdm_nb_columns=tqdm_nb_columns)
        return TQDMDataQueueReceiver(tqdm_update_queue)


def perform_tqdm_default_out_stream_hack(tqdm_update_queue: Queue, tqdm_nb_columns=None):
    import tqdm
    # save original class into module
    tqdm.original_class = tqdm.std.tqdm
    parent = tqdm.std.tqdm

    class TQDMPatch(parent):
        """
        Derive from original class
        """

        def __init__(self, iterable=None, desc=None, total=None, leave=True, file=None,
                     ncols=None, mininterval=0.1, maxinterval=10.0, miniters=None,
                     ascii=None, disable=False, unit='it', unit_scale=False,
                     dynamic_ncols=False, smoothing=0.3, bar_format=None, initial=0,
                     position=None, postfix=None, unit_divisor=1000, write_bytes=None,
                     lock_args=None, nrows=None, colour=None, delay=0, gui=False,
                     **kwargs):
            print('TQDM Patch called')  # check it works
            self.tqdm_update_queue = tqdm_update_queue
            self.tqdm_update_queue.put({"do_reset": True})
            super(TQDMPatch, self).__init__(iterable, desc, total, leave,
                                            file,  # no change here
                                            ncols,
                                            mininterval, maxinterval,
                                            miniters, ascii, disable, unit,
                                            unit_scale,
                                            False,  # change param ?
                                            smoothing,
                                            bar_format, initial, position, postfix,
                                            unit_divisor, gui, **kwargs)

        # def update(self, n=1):
        #     super(TQDMPatch, self).update(n=n)
        #     custom stuff ?

        def refresh(self, nolock=False, lock_args=None):
            super(TQDMPatch, self).refresh(nolock=nolock, lock_args=lock_args)
            self.tqdm_update_queue.put(self.format_dict)

        def close(self):
            self.tqdm_update_queue.put({"close": True})
            super(TQDMPatch, self).close()

    # change original class with the patched one, the original still exists
    tqdm.std.tqdm = TQDMPatch
    tqdm.tqdm = TQDMPatch  # may not be necessary
    # for tqdm.auto users, maybe some additional stuff is needed


class TQDMDataQueueReceiver(QObject):
    s_tqdm_object_received_signal = pyqtSignal(object)

    def __init__(self, q: Queue, *args, **kwargs):
        QObject.__init__(self, *args, **kwargs)
        self.queue = q

    @pyqtSlot()
    def run(self):
        while True:
            o = self.queue.get()
            # noinspection PyUnresolvedReferences
            self.s_tqdm_object_received_signal.emit(o)


class QTQDMProgressBar(QProgressBar):
    def __init__(self, parent, tqdm_signal: pyqtSignal):
        super(QTQDMProgressBar, self).__init__(parent)
        self.setAlignment(Qt.AlignCenter)
        self.setVisible(False)
        # noinspection PyUnresolvedReferences
        tqdm_signal.connect(self.do_it)

    def do_it(self, e):
        if not isinstance(e, dict):
            return
        do_reset = e.get("do_reset", False)  # different from close, because we want visible=true
        initial = e.get("initial", 0)
        total = e.get("total", None)
        n = e.get("n", None)
        desc = e.get("prefix", None)
        text = e.get("text", None)
        do_close = e.get("close", False)  # different from do_reset, we want visible=false
        if do_reset:
            self.reset()
        if do_close:
            self.reset()
        self.setVisible(not do_close)
        if initial:
            self.setMinimum(initial)
        else:
            self.setMinimum(0)
        if total:
            self.setMaximum(total)
        else:
            self.setMaximum(0)
        if n:
            self.setValue(n)
        if desc:
            self.setFormat(f"{desc} %v/%m | %p %")
        elif text:
            self.setFormat(text)
        else:
            self.setFormat("%v/%m | %p")


def long_procedure():
    # emulate late import of modules
    from tqdm.auto import tqdm # don't import before patch !
    __logger = logging.getLogger('long_procedure')
    __logger.setLevel(logging.DEBUG)
    tqdm_object = tqdm(range(10), unit_scale=True, dynamic_ncols=True)
    tqdm_object.set_description("My progress bar description")
    from tqdm.contrib.logging import logging_redirect_tqdm # don't import before patch !
    with logging_redirect_tqdm():
        for i in tqdm_object:
            QtTest.QTest.qWait(200)
            __logger.info(f'foo {i}')


class QtLoggingHelper(ABC):
    @abstractmethod
    def transform(self, msg: str):
        raise NotImplementedError()


class QtLoggingBasic(QtLoggingHelper):
    def transform(self, msg: str):
        return msg


class QtLoggingColoredLogs(QtLoggingHelper):
    def __init__(self):
        # offensive programming: crash if necessary if import is not present
        pass

    def transform(self, msg: str):
        import coloredlogs.converter
        msg_html = coloredlogs.converter.convert(msg)
        return msg_html


class QTextEditLogger(logging.Handler, QObject):
    appendText = pyqtSignal(str)

    def __init__(self,
                 logger_: logging.Logger,
                 formatter: logging.Formatter,
                 text_widget: QPlainTextEdit,
                 # table_widget: QTableWidget,
                 parent: QWidget):
        super(QTextEditLogger, self).__init__()
        super(QObject, self).__init__(parent=parent)
        self.text_widget = text_widget
        self.text_widget.setReadOnly(True)
        # self.table_widget = table_widget
        try:
            self.helper = QtLoggingColoredLogs()
            self.appendText.connect(self.text_widget.appendHtml)
            logger_.info("Using QtLoggingColoredLogs")
        except ImportError:
            self.helper = QtLoggingBasic()
            self.appendText.connect(self.text_widget.appendPlainText)
            logger_.warning("Using QtLoggingBasic")
        # logTextBox = QTextEditLogger(self)
        # You can format what is printed to text box
        self.setFormatter(formatter)
        logger_.addHandler(self)
        # You can control the logging level
        self.setLevel(logging.DEBUG)

    def emit(self, record: logging.LogRecord):
        msg = self.format(record)
        display_msg = self.helper.transform(msg=msg)
        self.appendText.emit(display_msg)
        # self.add_row(record)


class MainApp(QWidget):
    def __init__(self):
        super().__init__()

        self.__logger = logging.getLogger(self.__class__.__name__)
        self.__logger.setLevel(logging.DEBUG)

        layout = QVBoxLayout()

        self.setMinimumWidth(500)

        self.btn_perform_actions = QToolButton(self)
        self.btn_perform_actions.setText('Launch long processing')
        self.btn_perform_actions.clicked.connect(self._btn_go_clicked)

        self.thread_initialize = QThread()
        self.init_procedure_object = LongProcedureWorker(self)

        self.thread_tqdm_update_queue_listener = QThread()
        # must be done before any TQDM import
        self.tqdm_update_receiver = setup_streams_redirection()
        self.tqdm_update_receiver.moveToThread(self.thread_tqdm_update_queue_listener)
        self.thread_tqdm_update_queue_listener.started.connect(self.tqdm_update_receiver.run)

        self.pb_tqdm = QTQDMProgressBar(self, tqdm_signal=self.tqdm_update_receiver.s_tqdm_object_received_signal)
        layout.addWidget(self.pb_tqdm)
        self.thread_tqdm_update_queue_listener.start()

        self.plain_text_edit_logger = QPlainTextEdit(self)
        LOG_FMT = "{asctime} | {levelname:10s} | {message}"
        try:
            import coloredlogs
            FORMATTER = coloredlogs.ColoredFormatter(fmt=LOG_FMT, style="{")
        except ImportError:
            FORMATTER = logging.Formatter(fmt=LOG_FMT, style="{")

        self.logging_ = QTextEditLogger(logger_=logging.getLogger(),  # root logger, to intercept every log of app
                                        formatter=FORMATTER,
                                        text_widget=self.plain_text_edit_logger,
                                        parent=self)
        layout.addWidget(self.plain_text_edit_logger)
        layout.addWidget(self.btn_perform_actions)
        self.setLayout(layout)
        import tqdm
        self.__logger.info(f"tqdm {tqdm.__version__}")
        self.__logger.info(f"Qt={QT_VERSION_STR}; PyQt={PYQT_VERSION_STR}")
        with contextlib.suppress(ImportError):
            import coloredlogs
            self.__logger.info(f"coloredlogs {coloredlogs.__version__}")
        # prepare thread for long operation
        self.init_procedure_object.moveToThread(self.thread_initialize)
        self.thread_initialize.started.connect(self.init_procedure_object.run)
        self.init_procedure_object.finished.connect(self._init_procedure_finished)
        self.init_procedure_object.finished.connect(self.thread_initialize.quit)
        self.show()

    @pyqtSlot()
    def _btn_go_clicked(self):
        # start thread
        self.btn_perform_actions.setEnabled(False)
        self.__logger.info("Launch Thread")
        self.thread_initialize.start()

    def _init_procedure_finished(self):
        self.btn_perform_actions.setEnabled(True)


class LongProcedureWorker(QObject):
    finished = pyqtSignal()

    def __init__(self, main_app: MainApp):
        super(LongProcedureWorker, self).__init__()
        self._main_app = main_app

    @pyqtSlot()
    def run(self):
        long_procedure()
        self.finished.emit()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyle('Fusion')
    ex = MainApp()
    sys.exit(app.exec_())
