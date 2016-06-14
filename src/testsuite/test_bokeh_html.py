from nose.tools import assert_equal
import sys
import os

"""
	Testing the bokeh generator functions
	There are two functions to create bokeh html
	Two functions written to test their correctness
"""

# including src files to the sys path
newpath = os.path.dirname(os.path.realpath(__file__)) + '/../'
sys.path.insert(0, newpath)
print("PAthththththth :", os.path.realpath(__file__))

try:
	import bokeh_html as bok 
except Exception as e:
	raise e


""" Test 1, bokeh """
def test_bokeh1():
    print("Performing test 1 on bokeh generator")

    stationid = 50089
    year = 2016

    exp = "{}_{}_bokeh_min_max.html".format(stationid, year)

    filename = os.path.dirname(os.path.realpath(__file__)) + '/../../csv_data/{}_{}.csv'.format(stationid, year)
    if os.path.isfile(filename):
        obs = bok.plot_minmax(filename)
        assert_equal(exp, obs)
        print("Test successful")


""" Test 2, bokeh """
def test_bokeh2():
    print("Performing test 2 on bokeh generator")

    stationid = 50430
    year = 2014

    exp = "{}_{}_bokeh_gdd.html".format(stationid, year)

    filename = os.path.dirname(os.path.realpath(__file__)) + '/../../csv_data/{}_{}.gdd'.format(stationid, year)
    if os.path.isfile(filename):
        obs = bok.plot_gdd(filename)
        assert_equal(exp, obs)
        print("Test successful")

#test_bokeh1()
#test_bokeh2()
