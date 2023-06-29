# Get Started Tutorial for Sphinx Documentation

## STEPS:

### 1. Clone the repository that you want to document
Example:
```git
git clone https://github.com/MarianaMendanha/Projeto_Sphinx.git
```

### 2. Set up a virtual environment for your project
For Windows, install and create VENV:
```bash
pip install virtualenv
```
```py
py -m virtualenv sphinxenv
```
With the VENV ready, activate it: 
```bash
cd .\sphinxenv\Scripts\
.\activate
```
To deactivate:
```bash
cd .\sphinxenv\Scripts\
.\deactivate
```

### 3. Set up the documentation
Create a folder "docs" in the base of your project:
```bash
mkdir docs
cd docs
```
Install and iniciate sphinx inside docs directory:
```bash
pip install sphinx
sphinx-quickstart
```
There will be a build and source folder, a makefile, a conf.py file and a index.rst, something like this:
```
docs
├───build
│   ├───doctrees
│   └───html
│       ├───_images
│       ├───_modules
│       │   └───src
│       │       ├───module1
│       │       ├───module2
│       │       └───utils
│       ├───_sources
│       └───_static
│           ├───css
│           │   └───fonts
│           ├───fonts
│           │   └───calcutta
│           └───js
└───source
    ├───images
    ├───_static
    └───_templates
        conf.py
        index.rst
make.bat
Makefile
```
After that, we need to configure our sphinx in **conf.py**, there we can set a lot of things including themes for our documentation:
- [Site with some disponible themes](https://sphinx-themes.org/)
Here is an example of the parameters we can\need to change:
```py
# So sphinx can look outside its scope (look through the project)
# In this case is '..\..' because our .rst files are inside docs\source directory
import os
import sys
sys.path.insert(0, os.path.abspath('..\..'))

extensions = ["sphinx.ext.todo", "sphinx.ext.viewcode", "sphinx.ext.autodoc", "sphinx.ext.napoleon"]
templates_path = ['_templates']
html_theme = 'renku'
```
You can make your own .rst files and document your code too, to do so you need to, you need to use:
```bash
# We are now located at the \docs folder 
cd ..
# We are now located at the root of the project 
sphinx-apidoc -o docs\source .
```
where **"docs\source"** is the place we are going to create our .rst files and "." means that we are looking for all the files of our project that has docstrings in it, for this to work, every directory (module) has to have a **"__init__.py"** file, so sphinx can indentify the folder as a python module/package. We can use this command in specific directories too, as shown in:
```bash
sphinx-apidoc -o docs\source PLATAFORMA\Relatorio_py\modulos
```
After our .rst files are ready and configured (don't forget to chage the paths and doctrees inside them, check **".rst"** files above for examples to be followed), we can create our html with the command:
```bash
cd docs
.\make html
```
Open the **index.html** file gerated in **\docs\build\html**, and that`s it.

> **NOTE**: **WAIT** If that is some kind of ERROR on generating the html regarding sphinx not finding imported files try seeing in which directory sphinx is working at the moment of the ERROR. Example:
```py
sys.path.insert(0, os.path.abspath('..\PLATAFORMA\Relatorio_py'))
dir = sys.path[0]

cwd = os.getcwd()
print("CurrentWorkingDirectory>>>", cwd)

# change directory
os.chdir(os.path.join(dir, "modulos"))
```

#### References used for this tutorial:
- [How to Document using Sphinx: Part 1—Setting up](https://www.youtube.com/watch?v=WcUhGT4rs5o)
- [How to Document using Sphinx: Part 2—Building and Changing Themes](https://www.youtube.com/watch?v=RvJ54ADcVno)
- [How to Document using Sphinx: Part 3—Formatting with reStructuredText](https://www.youtube.com/watch?v=DSIuLnoKLd8&t=419s)
- [How to Document using Sphinx: Part 4—Using Git to push docs to GitHub](https://www.youtube.com/watch?v=CqR1b0Y-o5k)
- [Sphinx - How to generate documentation from python doc strings - Five + Minutes on Tips and Tricks](https://www.youtube.com/watch?v=BWIrhgCAae0)
- [Sphinx Documentation Tool | HTML UI | How to Document Large Python Codebases and Classes |](https://www.youtube.com/watch?v=5s3JvVqwESA)


🖼️ 📦 ❤️ 🤖 📃 💬 🐋 🧪 ✅ 📊 🛳️ 🎯 🔄 🖼️ 📦 ❤️ 🤖 📃 💬 🐋 🧪 ✅ 📊 🛳️ 🎯 🔄 🖼️ 📦 ❤️ 🤖 📃 💬 🐋 🧪 ✅ 📊 🛳️ 🎯 🔄



