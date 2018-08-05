def mult(a,b):
	return a*b

def div(a,b):
	return a/b

def sum(a,b):
	return a+b

def sub(a,b):
	return a-b

answer = input("Would you like to? A: Multiply, B: Divide, C: Add or D: Subtract ")
answer = answer.lower()
a = int(input("What is the first number? "))
b = int(input("What is the second number? "))

try:
	if answer == "a":
		print(mult(a,b))
	elif answer == "b":
		print(div(a,b))
	elif answer == "c":
		print(sum(a,b))
	elif answer == "d":
		print(sub(a,b))
	else:
		input("You entered a wrong number.")

except ZeroDivisionError:
	input("You tried to divide by 0")
