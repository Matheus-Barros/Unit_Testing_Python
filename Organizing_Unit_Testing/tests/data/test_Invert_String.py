# ==========================================
#		@Author: Matheus Barros 
#		Date: 02/11/2021
# ==========================================

import pytest
import sys
import os
user = os.environ['USERPROFILE']
sys.path.insert(0, user + '/Documents/GitHub/Unit_Testing_Python/Organizing_Unit_Testing')
import src.data.Invert_String as fc

class TestSum(object):
	def test_sum_floats(self):
		actual = fc.sum_floats(0.1,0.1,0.1)
		expected = 0.3
		message = ("Returned {0} instead of {1}".format(actual,expected)) 
		assert actual is expected, message

	def test_sum_floats_approx(self):
		assert fc.sum_floats(0.1,0.1,0.1) == pytest.approx(0.3)

class TestInvertString:
	def test_invert_str_wrong_name(self):
		actual = fc.invert_str('Matheus')
		expected = 'Bianca'
		message = ("Returned {0} instead of {1}".format(actual,expected))
		assert actual is expected, message

	def test_invert_str_right_name(self):
		actual = fc.invert_str('Matheus')
		expected = str('suehtaM')
		message = ("Returned {0} instead of {1}".format(actual,expected))
		assert expected in actual, message

#REMEMBER TO WRITE ON CMD 'pytest' BEFORE THE SCRIPT NAME
