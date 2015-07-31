PyWalker
========
A python file walker which outputs hierarchy to stdout or JSON.

###Features###
- Return directory structure or entire file tree
- Output to stdout or JSON

###Usage###
pywalker.py [-h] [-json] [-dirs] [-files] [-filter] [-ignore] [-hide] [--f FILENAME] [--p PATH]

###Arguments###
**-h, --help**  show this help message and exit

**-json**       Export to JSON

**-dirs**       Directory only output

**-files**      File only output

**-filter**     Use replacement filter

**-ignore**     Use ignore filter

**-hide**       Hide file extensions

**--f**     Export file name

**--p**         Starting file path
