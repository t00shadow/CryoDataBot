# CryoDataBot

CryoDataBot is a Python package designed for ...

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Features](#features)
- [Contributing](#contributing)
- [License](#license)

## Installation

To install CryoDataBot:
```bash
pip install git+https://github.com/t00shadow/CryoDataBot.git@main
```


## Usage
You can run the main GUI for CryoDataBot with the following command:

```bash
python -m cryodatabot
```

## Project Structure

Here is the basic suggested skeleton for your app repo that each of the starter templates conforms to:

```bash
├── src/
│   ├── __init__.py
│   ├── main.py                   # Command line entry point for the application 
│   ├── main_gui.py               # GUI entry point for the application 
│   ├── backend_core/
│   │   ├── __init__.py
│   │   ├── fetch_sample_info.py
│   │   ├── redundancy_filter.py
│   │   ├── ...
│   ├── backend_helpers/
│   │   ├── __init__.py
│   │   ├── helper_funcs.py
│   │   ├── ...
│   ├── frontend_gui_assets/
│   │   ├── __init__.py
│   │   ├── helper_funcs.py
│   │   ├── ...
├── tests/                        # doesnt exist yet
│   ├── test_backend.py
│   ├── test_gui.py
│   ├── ...
├── examples/                     # doesnt exist yet
│   ├── example1.py
│   ├── example2.py
│   ├── ...
├── README.md
├── LICENSE
├── .gitignore
├── setup.py
├── CHANGE_LOG.txt                # will get deleted or contents changed to match name
├── configwriter.py               # unorganized
├── CryoDataBotConfig.ini         # unorganized
```
