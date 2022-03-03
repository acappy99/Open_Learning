# Python Environment

## Read these
(Mark Jamison Pt 1)[https://towardsdatascience.com/what-is-a-python-environment-for-beginners-7f06911cf01a]

(Mark Jamison Pt 2)[https://towardsdatascience.com/python-the-system-path-and-how-conda-and-pyenv-manipulate-it-234f8e8bbc3e]



```
>>> import sys
>>> sys.prefix
'/Library/Frameworks/Python.framework/Versions/3.10'

>>> import site
>>> site.getsitepackages()
['/Library/Frameworks/Python.framework/Versions/3.10/lib/python3.10/site-packages']
```

### Running pip as a module

When you run your system pip directly, the command itself doesn’t reveal which Python version pip belongs to. This unfortunately means that you could use pip to install a package into the site-packages of an old Python version without noticing. To prevent this from happening, you can run pip as a Python module:
```
python3 -m pip
```

