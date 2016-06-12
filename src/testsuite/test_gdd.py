

from nose.tools import assert_equal
import sys

#import gdd



# including src files to the sys path
sys.path.insert(0, '../')

try:
	import gdd

except Exception as e:
	raise e


print(sys.path)

def test_gdd(file):
	
	exp = 5
	obs = 5


	assert_equal(exp, obs)