PyWalker
========
A python file walker which outputs structure to XML or JSON.

###Features###
- Return directory structure or entire file tree
- Output to stdout, XML, or JSON

###Usage###
pywalker.py [-h] [-xml | -json] [-dirs] [-files] [-filter] [-ignore] [-hide] [--f FILENAME] [--p PATH]

###Arguments###
-h, --help  show this help message and exit

-xml        Export to XML
-json       Export to JSON

-dirs       Directory only output
-files      File only output
-filter     Use replacement filter"
-ignore     Use ignore filter"
-hide       Hide file extensions

--f         Export file name
--p         Starting file path