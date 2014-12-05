#!/usr/bin/env python
# -*- coding: utf-8 -*-

#---------PyleWalker V_0.1-----------
import os, sys, argparse

#---------Global Variables-----------
f = []
fileName = ''
startingLocation = ''
args = sys.argv
parser = argparse.ArgumentParser()

#---------Parse Arguments-----------
group = parser.add_mutually_exclusive_group()
group.add_argument("-xml", help="Export to XML", action="store_true")
group.add_argument("-json", help="Export to JSON", action="store_true")
group.add_argument("-html", help="Export to HTML", action="store_true")
parser.add_argument("--f", help="Custom file name")
parser.add_argument("--p", help="Starting file path")
args = parser.parse_args()

if args.f:
    fileName = args.f
elif args.xml or args.json or args.html:
	fileName = 'index'
else:
	fileName = 'terminal'

if args.p:
    startingLocation = args.p
else:
	startingLocation = '.'

#------------Functions---------------
def openFile(filename = 'index.html'):
	global f
	f = open(filename, 'w')

def closeFile(filevar):
	filevar.close()

def html_output_test(startpath, fileName):
	openFile(fileName)
	f.write('<html><body>'+'\n')
	f.write('<link rel="stylesheet" type="text/css" href="style.css">'+'\n')
	print('WORKING...')
	for root, dirs, files in os.walk(startpath, topdown=True):
		level = root.replace(startpath, '').count(os.sep)
		f.write('<div class="dir level"><h'+str(level+1)+'>'+str(os.path.basename(root)))
		f.write('</h'+str(level+1)+'>'+'\n')
		for fyle in files:
			f.write('<div class="file">'+str(fyle)+'</div>'+'\n')
		f.write('</div>')
	f.write('</body></html>'+'\n')
	closeFile(f)
	print('Completed.')

def list_files(startpath, padding):
    for root, dirs, files in os.walk(startpath):
        level = root.replace(startpath, '').count(os.sep)
        indent = ' ' * padding * (level)
        print('{}{}/'.format(indent, os.path.basename(root)))
        subindent = ' ' * padding * (level + 1)
        for f in files:
            print('{}{}'.format(subindent, f))

#------------Execute---------------
if fileName == 'terminal':
	list_files(startingLocation, 5)
else:
	if args.xml:
		fileName += '.xml'
		#xml output
		print('xml')
		html_output_test(startingLocation, fileName)
	if args.json:
		fileName += '.json'
		#json output
		print('json')
		html_output_test(startingLocation, fileName)
	if args.html:
		fileName += '.html'
		print('html')
		html_output_test(startingLocation, fileName)