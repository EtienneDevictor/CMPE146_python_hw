def calculator(number1, number2, operator):
	x = float(number1)
	y = float(number2)
	if operator == '+':
		z = x + y
	elif  operator == '-':
		z = x - y
	elif operator == '*':
		z = x * y
	elif operator == '/':
		z = x / y
	elif operator == '//':
		z = x // y
	elif operator == '**':
		z = pow(x, y)
	else:
		z = 'Invalid Operator'
	print(z)

def parse_input():
	i = input('Enter Equation: ')
	list = i.split()
	calculator(list[0], list[2], list[1])

parse_input()
