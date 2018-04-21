## Example Python CLI App for NLTK (using Anaconda)

### Prerequisites
[Install Anaconda](https://conda.io/docs/installation.html)  

### Install source from Github
mkdir HelloNLTK  
cd HelloNLTK  
git clone <https://github.com/markbrownsword/hello-nltk.git> .  

### Create Python 3.5 environment (with NLTK)

```bash
conda create --name python35 python=3.5
conda install nltk

```

### Activate environment

```bash
source activate python35
```

### Install and run the Application

```bash
./install.sh
helloNLTK
```

### Deactivate environment

```bash
source deactivate
```

### PyCharm - Open Project
Set 'python35' as project interpreter  

### PyCharm - Create Run Configuration
Select Run / Edit Configurations  
Add Python configuration  
Change 'Script path' to 'Module name: helloNLTK'    
Set Python Interpreter to 'python35'  
Set Working Directory to '/path/to/HelloNLTK/helloNLTK'