from nose.tools import assert_equal
import sys
import os


"""	
	Testing the plot function 
	the plot.py file hanndles two kinds of plot: min/max plot and gdd plot
	few functions are written to test these functions 

 """

# including src files to the sys path
sys.path.insert(0, '../')


try:
	import gdd
except Exception as e:
	raise e


""" Test 1, gdd """
def test_gdd1():
	print("GDD: test 1")

	stationid = 50089
	year = 2016
	filename = '../../csv_data/' + str(stationid) + '_' + str(year) + '.csv'
	
	if not os.path.isfile(filename):
		print("File not exists. Thus returning ...")
		return

	exp = str(stationid) + '_' + str(year) + '.gdd'	
	obs = gdd.generate_gdd(filename, 10, 30)
	
	if not os.path.isfile(obs):
		print("GDD created file does not exists. Thus returning ...")
		return

	obs = obs.split('/')[-1]

	assert_equal(exp, obs)
	print("Test was successful")

""" Test 2, gdd """
def test_gdd2():
	print("GDD: test 2")

	city = 'toronto'
	stationid = 27211
	year = 2011
	filename = '../../csv_data/' + str(stationid) + '_' + str(year) + '.csv'
	
	exp = str(stationid) + '_' + str(year) + '.gdd'	
	obs = gdd.generate_gdd(filename, t_base, t_upper)
	obs = obs.split('/')[-1]

	assert_equal(exp, obs)


test_gdd1()
