## Example Python CLI App for NLTK (using Miniconda)

### Prerequisites
[Install Miniconda](https://conda.io/miniconda.html)  

### Setup
```bash
# Install source from Github
mkdir HelloNLTK  
cd HelloNLTK  
git clone <https://github.com/markbrownsword/hello-nltk.git> .  

# Create Python 3.5 environment (with NLTK)
conda create --name python35 python=3.5
conda install nltk

# Or create environment from requirements.txt
conda create --name python35 --file requirements.txt

```

### Dev and Test

```bash
# Activate environment
conda activate python35

# Install (required one time only with pip option --editable used)
./install.sh

# Run
helloNLTK

# Test
python -m unittest discover -v

# Create Requirements File
conda list --export > requirements.txt 

# Deactivate environment
conda deactivate
```
