import sys
import os.path
from gdd import generate_gdd
from download import download


""" This file is a version of optional task 3.
	This file should not be mentioned in Makefile.
	The procedure is self-explanatory and it gets its input from user.
	User should know the desired Station IDs for completing this task.


"""
# global variables
sids = [0, 0]
years = [0, 0]

def main():
	print("-------------------------------------------------------")
	print(" Welcome to Extended version of GDD")
	print(" This function gets 2 station IDs and a year for each of them")
	print(" It will download the data and calculate the gdd for each and plot them all in one graph. ")
	print("-------------------------------------------------------")
	# getting station ids and years from user
	get_info()
	# Download the info from the server:
	# first file
	f_name_1 = "../csv_data/" + download(sids[0],years[0])
	# second file
	f_name_2 = "../csv_data/" + download(sids[1],years[1])

	print("Now that downloading is completed.")
	print("Here comes the GDD calculation.")
	tbase = input('Enter a t_base value: ')
	print("Please wait...")
	# Calculate the GDDs
	# first file
	generate_gdd(f_name_1, int(tbase), 0)
	# second file
	generate_gdd(f_name_2, int(tbase), 0)

	print("GDD calculation is done.")
	print("Now ploting...")
	# ploting 2 gdd files together

	


def get_info():
	print("Enter the information for comparing 2 stations in 2 years:")
	for i in range(0, 2):
		s_id = input('Enter station Id #{0}:  '.format(i+1))
		y = input('Enter a year for #{0}:  '.format(i+1))
		sids[i] = int(s_id)
		years[i] = int(y)


if __name__ == '__main__':main()
