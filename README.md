<a id="readme-top"></a>

# CryoDataBot

CryoDataBot is a Python workflow designed for curating high-quality cryoEM datasets for AI-driven structural biology.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
  - [1. Running the GUI](#1-running-the-gui)
  - [2. Standard workflow](#2-standard-workflow)
  - [3. Quickstart](#3-quickstart)
  - [4. Command-line interface (CLI)](#4-command-line-interface-cli)
  - [5. Running backend scripts modularly](#5-running-backend-scripts-modularly)
- [Project Structure](#project-structure)
- [License](#license)

## Installation

### Option 1: Run from source
This option gives you full control, including being able to run the core backend scripts modularly (see [5. Running backend scripts modularly](#5-running-backend-scripts-modularly)).

Clone the repo and change directory to CryoDataBot.
```sh
git clone https://github.com/t00shadow/CryoDataBot.git
cd CryoDataBot

# Create a virtual environment
python3 -m venv .venv
```
Activate the virtual environment and pip install packages from the requirements.txt.

> Linux/Mac:
```sh
source .venv/bin/activate
pip install -r requirements.txt
```

> Windows:
```sh
.\.venv\Scripts\activate
pip install -r requirements.txt
```

### Option 2: Download pre-built binaries (executables) under Releases
If you only want to use the GUI:

[Download latest release](https://github.com/t00shadow/CryoDataBot/releases/latest)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Usage
### 1. Running the GUI
#### If running from source:
&nbsp;&nbsp;&nbsp;&nbsp;Run as a module with -m:
```sh
python -m cryodatabot
```
&nbsp;&nbsp;&nbsp;&nbsp;OR run as a script directly:
```sh
python run_gui.py
```

#### If running pre-built binary (executable):
&nbsp;&nbsp;&nbsp;&nbsp;Double click the executable.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

### 2. Standard workflow
<ol type="i">
  <li><b>Collect Metadata</b></li>
  [INSERT IMAGE(S) HERE]
  <li><b>Curation</b></li>
  [INSERT IMAGE(S) HERE]
  <li><b>Construct Datasets</b></li>
  [INSERT IMAGE(S) HERE]
</ol>

<p align="right">(<a href="#readme-top">back to top</a>)</p>

### 3. Quickstart
Same as the standard workflow but with less clicks and **without** intermediate output.

[INSERT IMAGE(S) HERE]

<p align="right">(<a href="#readme-top">back to top</a>)</p>

### 4. Command-line interface (CLI)
fix this, on another branch, need to check something (think need to change some imports or paths)

[INSERT IMAGE(S) HERE]

<p align="right">(<a href="#readme-top">back to top</a>)</p>

### 5. Running backend scripts modularly
<details> 
<summary> (Optional) If you want to run the backend scripts individually: </summary>
  
  **This only works if you cloned the repository.**
  
  There are 4 core backend scripts (see <a href="#project-structure">Project Structure</a>). 
  
  _Note: The curation page in the GUI uses 2 of them, hence why the GUI only has 3 pages in the standard workflow._
  
  ```
  python -m cryodatabot.src.backend.core.[backend_script]
  ```
  Options are `fetch_sample_info`, `redundancy_filter`, `downloading_and_preprocessing_NO_GPU2`, and `generate_dataset`. Running as a module, so drop the ".py" suffix.

  ex)
  ```
  python -m cryodatabot.src.backend.core.fetch_sample_info
  ```

  To change user inputs (parameters, thresholds, paths, etc.), one way is to modify the `main()` function of the target script directly (ex. the `main()` function of `fetch_sample_info.py`), and then run the above command. Each of the 4 core backend scripts has a `main()` function with example usage. 
  
  The other way is edit the config file CryoDataBotConfig.ini (located in the root level directory).

[INSERT IMAGE(S) HERE, 2 total, 1 for main(), 1 for ini]

</details>

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Project Structure

```
CryoDataBot
├── cryodatabot
│   ├── src
│   │   ├── backend
│   │   │   ├── core
│   │   │   │   ├── fetch_sample_info.py
│   │   │   │   ├── redundancy_filter.py
│   │   │   │   ├── downloading_and_preprocessing_NO_GPU2.py
│   │   │   │   └── generate_dataset.py
│   │   │   └── helper
│   │   │       └── ...
│   │   └── frontend
│   │       └── ...
│   ├── __main__.py
│   └── main_gui.py
├── CryoDataBotConfig.ini
├── LICENSE
├── README.md
├── requirements.txt
└── run_gui.py
```

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## License
This project is licensed under the terms of the [MIT License](LICENSE).

<p align="right">(<a href="#readme-top">back to top</a>)</p>
