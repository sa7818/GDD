#! /usr/bin/env python
import argparse
import os.path
import glob
from gdd import generate_gdd
from plot import plot_maxmin

""" This file works as a command-line 
   ./main.py --list
   ./main.py gdd [filename] [tbase] [tupper]
"""

def main():
	parser = argparse.ArgumentParser()
	parser.add_argument('cmd', nargs='?')
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

	fname = ""

	args = parser.parse_args()
	if args.list:
		file_dir = "../csv_data/"
		print("List of files:")
		print("---------------------------------------------------")
		pattern = file_dir + "/*.csv"
		files_in_city = glob.glob(pattern)
		for f in files_in_city:
			print("{0}".format(f))

	if args.cmd:
		#print("~ CMD entered: {}".format(args.cmd))
		if(args.cmd == "gdd"):
			conA = True
		if(args.cmd == "plot"):
			conB = True

	if args.filename:
		if os.path.isfile(args.filename):
			print("~ Filename: {} exists!".format(args.filename))
			con1 = True
			fname = args.filename
		else:
			print("~ Filename: {} does not exist!".format(args.filename))
			con1 = False
	if args.t_base:
	    #print("~ TBase: {}".format(args.t_base))
	    con2 = True
	if args.t_upper:
	    #print("~ TUpper: {}".format(args.t_upper))
	    con3 = True

	if con1 and con2 and con3:
		print("file name and number of parameters entered are correct")
		print("~ Filename: {}".format(args.filename))
		print("~ TBase: {}".format(args.t_base))
		print("~ TUpper: {}".format(args.t_upper))

		if conA == True and conB == False:
			print("GDD function is called based on the above parameters.")
			generate_gdd(args.filename,args.t_base,args.t_upper)
		if conA == False and conB == True:
	        	print("Plot function is called based onte above parameters.")

if __name__ == '__main__':main()

