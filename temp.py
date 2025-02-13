from pathlib import Path
# my_directory = "zzzzz_TEST/parent/parent/directory"
# Path(my_directory).mkdir(parents=True, exist_ok=True)

# path = Path(r'C:\Users\noelu\CryoDataBot\temp.py')
path = Path(r'C:\Users\noelu/CryoDataBot\temp.py')
path = str(path)
print(path)
print(type(path))


from PyInstaller.utils.hooks import collect_submodules
...
hiddenimports = collect_submodules('cupy_backends.cuda')  # collect submodules only for CUDA backend
# hiddenimports += collect_submodules('cupy_backends.cuda')  # collect submodules only for CUDA backend
#hiddenimports += collect_submodules('cupy_backends')  # collect submodules for all backends
print(hiddenimports)