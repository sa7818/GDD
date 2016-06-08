#! /usr/bin/env python

"""
   for making this file executable, 
   you must first enter the following command:
   $ chmod +x main.py
   then you can run this file like this:
   ./main.py --list
   ./main.py gdd [filename] [tbase] [tupper]
"""
import argparse
import os.path
import glob

parser = argparse.ArgumentParser()
parser.add_argument('gdd', nargs='?')
parser.add_argument('plot', nargs='?')
parser.add_argument('--list', action='store_true', help='show a list of cities, and files available for each.')
parser.add_argument('filename', nargs='?')
parser.add_argument('t_base', nargs='?', type=int)
parser.add_argument('t_upper', nargs='?', type=int)


#condition for executing some commands
conA = False  # for gdd command
conB = False  # for plot command
con1 = False  # for filename
con2 = False  # for tbase 
con3 = False  # for tupper 


args = parser.parse_args()
if args.list:
    file_dir = "../csv_data/"
    print("List of files:")
    print("---------------------------------------------------")
    pattern = file_dir + "/*.CSV"
    files_in_city = glob.glob(pattern)
    for f in files_in_city:
	print("{0}".format(f))

if args.gdd:
    conA = True

if args.plot:
    conB = True


if args.filename:
    if os.path.isfile(args.filename):
    	print("~ Filename: {} exists!".format(args.filename))
	con1 = True
    else:
	print("~ Filename: {} does not exist!".format(args.filename))
	con1 = False
if args.t_base:
    print("~ TBase: {}".format(args.t_base))
    con2 = True
if args.t_upper:
    print("~ TUpper: {}".format(args.t_upper))
    con3 = True

if con1 and con2 and con3:
    print("file name and number of parameters entered are correct")
    if conA == True and conB == False:
  	print("Now we can call the GDD function")
	# call gdd here
    if conA == False and conB == True:
  	print("Now we can call the PLOT function")
	# call plot here












