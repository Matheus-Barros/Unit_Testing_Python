# ==========================================
#		@Author: Matheus Barros 
#		Date: 02/09/2021
# ==========================================

import pytest
from ConvertToInt import convert_to_int

def test_convert_to_int_1():
	assert convert_to_int(2.9) == 2


def test_convert_to_int_string():
	assert convert_to_int('teste') == 3


def test_convert_to_int_3():
	assert convert_to_int(75) == 4


def test_convert_to_int_4():
	assert convert_to_int(9.8) == 9

#REMEMBER TO WRITE ON CMD 'pytest' BEFORE THE SCRIPT NAME
