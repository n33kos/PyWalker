#!/usr/bin/env python
# -*- coding: utf-8 -*-

#---------PyWalker V_1.0-----------
import os, sys, argparse, json
from filters_replace import replaceDict
from filters_ignore import ignoreDict

#---------Global Variables-----------
f = []
fileName = ''
startingLocation = ''
args = sys.argv
parser = argparse.ArgumentParser()

#---------Parse Arguments-----------

group2 = parser.add_mutually_exclusive_group()
group2.add_argument("-dirs", help="Directory only output", action="store_true")
group2.add_argument("-files", help="File only output", action="store_true")

parser.add_argument("-json", help="Export to JSON", action="store_true")
parser.add_argument("-filter", help="Use replacement filter", action="store_true")
parser.add_argument("-ignore", help="Use ignore filter", action="store_true")
parser.add_argument("-hide", help="Hide file extensions", action="store_true")

parser.add_argument("--f", help="Export file name")
parser.add_argument("--p", help="Starting file path")
args = parser.parse_args()

if args.f:
    fileName = args.f
elif args.json:
	fileName = 'pywalker_output'
else:
	fileName = 'terminal'

if args.p:
    startingLocation = args.p
else:
	startingLocation = '.'

#------------Functions---------------
def openFile(filename):
	global f
	f = open(filename, 'w')

def closeFile(filevar):
	filevar.close()
	
def filter_output(theString):
	if replaceDict.get(theString):
		return replaceDict.get(theString)
	else:
		return theString

def parse_ignore(theString):
	if args.ignore:
		if any(theString in s for s in ignoreDict):
			return False
		else:
			return True
	else:
		return True

def remove_extension(theString):
	newString = theString.split('.', 1)[0]
	return newString

def list_files(startpath, padding):
	for root, dirs, files in os.walk(startpath, topdown=True):
		level = root.replace(startpath, '').count(os.sep)
		indent = ' ' * padding * (level)
		if args.dirs or args.files == False:
			if parse_ignore(os.path.basename(root)):
				if args.filter:
					print('{}{}/'.format(indent, filter_output(os.path.basename(root))))
				else:
					print('{}{}/'.format(indent, os.path.basename(root)))
		subindent = ' ' * padding * (level + 1)
		if args.files or args.dirs == False:
			for f in files:
				if parse_ignore(f):
					if args.hide:
						if args.filter:
							print('{}{}'.format(subindent, filter_output(remove_extension(f))))
						else:
							print('{}{}'.format(subindent, remove_extension(f)))
					else:
						if args.filter:
							print('{}{}'.format(subindent, filter_output(f)))
						else:
							print('{}{}'.format(subindent, f))

def json_output(startpath, fileName):
	openFile(fileName)
	print('Working...')

	f.write('{')
	counter = 0
	fileOnlyList = []
	for root, dirs, files in os.walk(startpath, topdown=True):
		level = root.replace(startpath, '').count(os.sep)
		if counter > 0:
			f.write(', ')
			f.write(json.dumps(root.replace(startpath, '')))
		else:
			f.write(json.dumps('root'))
		f.write(':')
		for i, d in enumerate(dirs):
			dirs[i] += '/'
			if parse_ignore(dirs[i]) != True:
				dirs.remove(dirs[i])
		for i, g in enumerate(files):
			if parse_ignore(files[i]) != True:
				files.remove(files[i])
			if args.hide:
				if args.filter:
					files[i] = filter_output(remove_extension(files[i]))
				else:
					files[i] = remove_extension(files[i])
			else:
				if args.filter:
					files[i] = filter_output(files[i])
		if args.dirs == True and args.files == False:
			f.write(json.dumps(dirs))
		elif args.files == True and args.dirs == False:
			for i in files:
				fileOnlyList.append(i)
		else:
			f.write(json.dumps(dirs+files))
		counter += 1
	if args.files == True and args.dirs == False:
		f.write(json.dumps(fileOnlyList))
	f.write('}')

	closeFile(f)
	print('Completed.')

#------------Execute---------------
if fileName == 'terminal':
	if args.files:
		paddingval = 0
	else:
		paddingval = 3
	list_files(startingLocation, paddingval)
else:
	if args.json:
		fileName += '.json'
		json_output(startingLocation, fileName)