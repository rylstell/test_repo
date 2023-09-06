
# This is an edit on branch main

from print_funcs import print_regular

def add(num1, num2):
	return num1 + num2

def sub(num1, num2):
	return num1 - num2

def multiply(num1, num2):
	return num1 * num2

def divide(num1, num2):
	return num1 / num2

def main():

	a = 4
	b = 7

	c = add(a, b)
	d = sub(a, b)
	e = multiply(a, b)
	f = divide(a, b)

	print_regular(c)
	print_regular(d)
	print_regular(e)
	print_regular(f)

if __name__ == "__main__":
	main()
