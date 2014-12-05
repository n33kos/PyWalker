PyWalker
========
A python file walker which outputs structure to XML, JSON, or HTML.


###Features###
- Return directory structure or entire file tree
- Output to stdout, XML, HTML, or JSON

###To-Do###
- Implement directory only output
- Implement JSON Export
- Implement XML Export
- Implement HTML Export
  -Include css stylesheet injection
- Implement terminal output
- Implement String Replacement config file
- Comp interface
- Customize stylesheet

###Wishlist###
- Add description feature
- Database support?
- Smarty controller integration

###Usage###
usage: pywalker.py [-h] [-xml | -json | -html] [--f FILENAME] [--p PATH]

###Arguments###
  -h, --help  show this help message and exit
  -xml        Export to XML
  -json       Export to JSON
  -html       Export to HTML
  --f F       Custom file name
  --p P       Starting file path

###Changelog###
V_0.1 -
	-Tested output speed and methods
	-Set up plaintext prototype with HTML output
	-Created stylesheet
	-Added argument processing and mapped out arguments
  -Added file naming functionality
  -Added custom path functionality
  -Added formatted stdout functionality (default command function)