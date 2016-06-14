from nose.tools import assert_equal
import sys
import os


"""
	Testing the download function
	Two functions are implemented in order to test the download correctness
	At the end it passes the test if the file was downloaded
"""

# including src files to the sys path
newpath = os.path.dirname(os.path.realpath(__file__)) + '/../'
sys.path.insert(0, newpath)

try:
	import download as dnd
except Exception as e:
	raise e


""" Test 1, download """
def test_download1():
	print("Performing test 1 on download ")

	stationid = 50089
	year = 2016

	exp = "{}_{}.csv".format(stationid, year)
	obs = dnd.download(stationid, year)
	
	assert_equal(exp, obs)
	print("Test successful")

""" Test 2, download """
def test_download2():
	print("Performing test 2 on download ")

	stationid = 50430
	year = 2013

	exp = str(stationid) + '_' + str(year) + '.csv'
	obs = dnd.download(stationid, year)
	
	assert_equal(exp, obs)
	print("Test successful")


#test_download1();
#test_download2();

######
#running the test functions via: nosetests testsuite.py
