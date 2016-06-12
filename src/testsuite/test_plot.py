from nose.tools import assert_equal
import sys


"""	
	Testing the plot function 
	the plot.py file hanndles two kinds of plot: min/max plot and gdd plot
	few functions are written to test these functions 

 """

# including src files to the sys path
sys.path.insert(0, '../')


# import the plot file
try:
	import plot
except Exception as e:
	raise e



""" Testing the min/max and gdd plot functions """

""" Test 1, min / max plot """
def test_plot1():
	city = 'stjohns'
	stationid = 50089
	year = 2016

	csv_file = '../../csv_data/50089_2014.csv'
	obs = plot.plot_minmax(csv_file)

	exp = '50089_2014.png'

	assert_equal(exp, obs)

"""Test 2, gdd plot"""
def test_plot2():
	city = 'alberta'
	stationid = 50089
	year = 2011

	csv_file = '../../csv_data/50089_2011.gdd'
	obs = plot.plot_gdd(csv_file, None, None)

	exp = '50089_2011.png'

	assert_equal(exp, obs)


#test_plot1()
#test_plot2()
