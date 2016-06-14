from nose.tools import assert_equal
import sys
import os

"""	
	Testing the plot function 
	the plot.py file hanndles two kinds of plot: min/max plot and gdd plot
	few functions are written to test these functions 

 """

# including src files to the sys path
newpath = os.path.dirname(os.path.realpath(__file__)) + '/../'
sys.path.insert(0, newpath)

# import the plot file
try:
	import plot
except Exception as e:
	raise e
	#print(e)


""" Testing the min/max and gdd plot functions """

""" Test 1, min / max plot """
def test_plot1():
    print("Performing test 1 on plot for min max")

    stationid = 50089
    year = 2016

    exp = "{}_{}_minmax.png".format(stationid, year)

    filename = os.path.dirname(os.path.realpath(__file__)) + '/../../csv_data/{}_{}.csv'.format(stationid, year)
    if os.path.isfile(filename):
        obs = plot.plot_maxmin(filename)
        assert_equal(exp, obs)
        print("Test successful")

"""Test 2, gdd plot"""
def test_plot2():
    print("Performing test 2 on plot for gdd")

    stationid = 50089
    year = 2016

    exp = "{}_{}_gdd.png".format(stationid, year)

    filename = os.path.dirname(os.path.realpath(__file__)) + '/../../csv_data/{}_{}.gdd'.format(stationid, year)
    if os.path.isfile(filename):
        obs = plot.plot_gdd(filename, None, None)
        assert_equal(exp, obs)
        print("Test successful")

#test_plot1()
#test_plot2()
