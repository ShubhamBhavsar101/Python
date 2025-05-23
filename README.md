# Python

All my python code practice is stored here.


## Creating a virtual Environment

Step 1: Create a virtual environment (in a directory named venv)
```bash
python3 -m venv venv
```
Step 2: Activate the virtual environment
```bash
source venv/bin/activate
```

Step 3: Now install the dependencies
```bash
pip install -r requirements.txt
```
## Using Pyenv to change python versions
Reference - [Pyenv Github Repo](https://github.com/pyenv/pyenv)
```bash
pyenv versions
```
Install Python Version
```bash
pyenv install 3.12
```
Activate Python globally
```bash
pyenv global 3.12
python --version
```
Activate Python for a local folder
```bash
pyenv local 3.10
```
