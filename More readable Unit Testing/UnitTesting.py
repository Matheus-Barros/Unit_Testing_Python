# ==========================================
#		@Author: Matheus Barros 
#		Date: 02/09/2021
# ==========================================

import pytest
import InvertString as fc

#IN CASE OF THE UNIT TESTING FAIL, IT'LL RETURN A CLEAR MESSAGE OF THE ERROR
def test_sum_floats():
	actual = fc.sum_floats(0.1,0.1,0.1)
	expected = 0.3
	message = ("Returned {0} instead of {1}".format(actual,expected)) 
	assert actual is expected, message

def test_sum_floats_approx():
	assert fc.sum_floats(0.1,0.1,0.1) == pytest.approx(0.3)

def test_invert_str_wrong_name():
	actual = fc.invert_str('Matheus')
	expected = 'Bianca'
	message = ("Returned {0} instead of {1}".format(actual,expected))
	assert actual is expected, message

def test_invert_str_right_name():
	actual = fc.invert_str('Matheus')
	expected = str('suehtaMk')
	message = ("Returned {0} instead of {1}".format(actual,expected))
	assert expected in actual, message

#REMEMBER TO WRITE ON CMD 'pytest' BEFORE THE SCRIPT NAME
