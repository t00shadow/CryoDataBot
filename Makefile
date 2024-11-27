.PHONY: install clear uninstall install_dev

install:
	pip install .
	make clear

clear:
	rm -rf build dist *.egg-info

uninstall:
	pip uninstall -y cryodatabot

install_dev:
	pip install -e .