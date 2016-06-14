from nose.tools import assert_equal
import sys


"""
	Testing the bokeh generator functions
	There are two functions to create bokeh html
	Different functions written to test their correctness.
"""

# Updating the system path to src directory
sys.path.insert(0, '../')


try:
	import bokeh_html as bok 
except:
	print("Failed to import the bokeh_html.py file")

def test_bokeh1():
	print("Starting test 1 bokeh")

	fname = "../../csv_data/50089_2015.csv"	
	if os.path.isfile(fname):
		print("File exists")
	else:
		print("File not exists")
		return 0
		
	exp = "50089_2015_bokeh_min_max.html"
	obs = bok.plot_minmax(fname)
	
	assert_equal(exp, obs)

	print("Test was successful")


test_bokeh1()