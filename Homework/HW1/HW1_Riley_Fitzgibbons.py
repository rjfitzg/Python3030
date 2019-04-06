'''
Homework 2
Riley Fitzgibbons
01/30/19
Simple program to show basic knowledge of Python. Uses: print, input, len, str, int, float, randint.

'''

def main():
	# Import necesary packages
	from random import randint

	# Code Block 1
	# Obtain user name, age, and then print some maths
	# Uses input(), int()
	userName = input("Please give me your name: ")
	age  = int(input("Please give me your age: "))

	# Use the required operators and the float()
	goblinAge = float(age)/randint(3,10)
	orcAge = age**randint(1,4)
	wizardAge = age % randint(1,7)
	eagleAge = age*randint(2,5)

	# Print the information and use the str(), len()
	print("\nThe length of your name is %s" % len(userName))
	print("In human years, you are " + str(age))
	print("Your goblin age is %s" % goblinAge)
	print("Your orc age is %s" % orcAge)
	print("Your wizard age is %s" % wizardAge)
	print("Your eagle age is %s" % eagleAge)

	# Code Block 2
	# while look to ask 3 questions in a For loop that may reveal the message
	# Uses while(), for(), continue, if(), elif(), else, and the SECRET MESSAGE
	while(True):
		for i in range(0,4):
			if (i == 0):
				color = input("\nWhat is your favorite color? ")
			elif (i==1):
				shape = input("What is your favorite shape? ")
			elif(i==2):
				continue
				print("I am meant to be skipped") # This should not print
			else:
				number = input("What is your favorite number? ")
		if (len(color) + len(shape) + int(number) > 10):
			print("You unlocked the secret message!")
			print("\n PEANUT BUTTER \n")
			break
		else:
			print("You did not unlock the message, try a bit LONGER")

	# Code block 3
	# This is literally just to use the truthy falsey values, they did not fit anywhere else
	myList = []
	if not myList:
		print("The list is empty... therefore it is falsey")


# Call Main.
if __name__=="__main__":
	main()