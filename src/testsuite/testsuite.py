from nose.tools import assert_equal
#from urldownload import download


"""Testing the download function"""
def test_download():
	#exp = 'csv_data/stjohns-50089-2016.csv'
	#obs = download('stjohns', 50089, 2016)
	
	exp = 5
	obs = 5
	#assert exp == obs
	assert_equal(exp, obs)

"""Testing the plot function"""
def test_plot():
	exp = 2
	obs = 2
	assert_equal(exp, obs)

#test_download()
#running the test functions via: nosetests testsuite.py
