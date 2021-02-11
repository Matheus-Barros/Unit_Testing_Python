# ==========================================
#		@Author: Matheus Barros 
#		Date: 02/11/2021
# ==========================================

import pytest
import sys
import os
user = os.environ['USERPROFILE']
sys.path.insert(0, user + '/Documents/GitHub/Unit_Testing_Python/Expected failures')
import src.data.Sum as fc

#IN

class TestSum(object):
	def test_sum_1_2(self):
		actual = fc.sum(1,2)
		expected = 3
		message = ("Returned {0} instead of {1}".format(actual,expected)) 
		assert actual is expected, message

	def test_sum_7_20(self):
		actual = fc.sum(7,20)
		expected = 27
		message = ("Returned {0} instead of {1}".format(actual,expected)) 
		assert actual is expected, message

	@pytest.mark.xfail(reason="Expected to fail, becausa I didn't implemented")
	def test_sum_97_3(self):
		pass

	def test_sum_6_5(self):
		actual = fc.sum(6,5)
		expected = 11
		message = ("Returned {0} instead of {1}".format(actual,expected)) 
		assert actual is expected, message

	@pytest.mark.xfail(reason="Expected to fail, becausa I didn't implemented")
	def test_sum_8_4(self):
		pass

#REMEMBER TO WRITE ON CMD 'pytest' BEFORE THE SCRIPT NAME
