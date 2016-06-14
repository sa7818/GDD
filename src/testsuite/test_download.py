from nose.tools import assert_equal
import sys


"""
	Testing the download function
"""

# including src files to the sys path
sys.path.insert(0, '../')
print(sys.path)

try:
	import download as dnd
except Exception as e:
	raise e


""" Test 1, download """
def test_download1():
	print("Download: test 1")

	city = 'stjohns'
	stationid = 50089
	year = 2016

	exp = str(stationid) + '_' + str(year) + '.csv'
	obs = dnd.download(stationid, year)
	
	assert_equal(exp, obs)

""" Test 2, download """
def test_download2():
	print("Download: test 2")

	city = 'alberta'
	stationid = 50089
	year = 2011

	exp = str(stationid) + '_' + str(year) + '.csv'
	obs = dnd.download(stationid, year)
	
	assert_equal(exp, obs)

""" Test 3, download """
def test_download3():
	print("Download: test 3")

	city = 'toronto'
	stationid = 50089
	year = 2012

	exp = str(stationid) + '_' + str(year) + '.csv'
	obs = dnd.download(stationid, year)
	
	assert_equal(exp, obs)


#test_download1();

######
#test_download()
#running the test functions via: nosetests testsuite.py
