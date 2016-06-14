from nose.tools import assert_equal
import sys
import os


"""	
	Testing the gdd calculations function 
	The gdd.py file contains a function for calculating the gdd for each year
	Two functions are written to test these functions 
 """

# including src files to the sys path
newpath = os.path.dirname(os.path.realpath(__file__)) + '/../'
sys.path.insert(0, newpath)

try:
	import gdd
except Exception as e:
	raise e


""" Test 1, gdd """
def test_gdd1():
    print("Performing test 1 on gdd calculations")

    stationid = 50089
    year = 2016

    exp = "{}_{}.gdd".format(stationid, year)

    filename = os.path.dirname(os.path.realpath(__file__)) + '/../../csv_data/{}_{}.csv'.format(stationid, year)
    if os.path.isfile(filename):
        obs = gdd.generate_gdd(filename, 10, 30)
        assert_equal(exp, obs)
        print("Test successful")

""" Test 2, gdd """
def test_gdd2():
    print("Performing test 2 on gdd calculations")

    stationid = 50430
    year = 2014

    exp = "{}_{}.gdd".format(stationid, year)

    filename = os.path.dirname(os.path.realpath(__file__)) + '/../../csv_data/{}_{}.csv'.format(stationid, year)
    if os.path.isfile(filename):
        obs = gdd.generate_gdd(filename, 10, 30)
        assert_equal(exp, obs)
        print("Test successful")

#test_gdd1()
#test_gdd2()
