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

```bash
├── src/                          # oops rename to cryodatabot or update the Usage section
│   ├── __init__.py
│   ├── main.py                   # Command line entry point for the application 
│   ├── main_gui.py               # GUI entry point for the application 
│   ├── backend_core/
│   │   ├── __init__.py
│   │   ├── fetch_sample_info.py                      # Step 1
│   │   ├── redundancy_filter.py                      # Step 2
│   │   ├── downloading_and_preprocessing.py          # Step 3
│   │   ├── generate_dataset.py                       # Step 4
│   ├── backend_helpers/
│   │   ├── __init__.py
│   │   ├── helper_funcs.py
│   │   ├── atom_in_models.py
│   ├── frontend_gui_assets/
│   │   ├── __init__.py
│   │   ├── gui_skin.py
│   │   ├── resources_rc.py
│   │   ├── custom_widgets ...
│   │   ├── other misc assets ...
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
├── configwriter.py               # prob will make a config folder and move it there
├── CryoDataBotConfig.ini         # prob will make a config folder and move it there
```
