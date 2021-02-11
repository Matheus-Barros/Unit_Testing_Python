# ==========================================
#		@Author: Matheus Barros 
#		Date: 02/11/2021
# ==========================================

def invert_str(string, seperator=' '):
	lenght = len(string)
	string = list(string)
	lenght += -1
	nome = list()
	while lenght != -1:
		nome.append(string[lenght])
		lenght += -1
	return str(seperator.join(nome).replace(' ' , '').strip())

def sum_floats(value1, value2, value3):
	return value1 + value2 + value3
