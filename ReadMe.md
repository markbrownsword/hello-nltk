## Example Setup NLTK using virtual environment and pip

## Prerequisites - python3 (with venv)
sudo apt install python3-venv

## Create the project folder
mkdir Hello-NLTK  
cd Hello-NLTK

## Create Python3 virtual environment
python3 -m venv .venv

## To install from github
git clone <https://github.com/markbrownsword/hello-nltk.git> .  
pip install -r requirements.txt

## To install from scratch
pip install -U nltk  
pip freeze > requirements.txt

## Activate environment
source .venv/bin/activate

## Deactivate environment
deactivate

## References
<https://cloud.google.com/python/setup>  
<https://docs.python.org/3/tutorial/venv.html>  
<https://stackoverflow.com/questions/39406177/managing-contents-of-requirements-txt-for-a-python-virtual-environment>  
