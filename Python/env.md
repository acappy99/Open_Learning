# Setting up virtual environment

(venv tutorial)[https://www.youtube.com/watch?v=Kg1Yvry_Ydk]

### Create virtual environment
```
python3 -m venv [virtual_env_name]
```
'-m' searches sys.path for specified module and runs that as the main module
#### Activate virtual environment
```
source [virtual_env_name]/bin/activate
```
#### Which python you are using (path)
```
which python
```
#### Check packages
```
pip list
```

### Export/import packages for a specific env
#### Export
Using a requirements.txt
```
pip freeze > requirements.txt
```
Check the export
```
cat requirements.txt
```
#### Import
```
pip install -r requirements.txt
```

### Deactivate env
```
deactivate
```
#### Delete env
```
rm -rf project_env/
```

## Typical convention

Create environment in project folder and name it 'venv'
```
mkdir [project name]

python3 -m venv [project_name]/venv

source [project_name]/venv/bin/activate
```
