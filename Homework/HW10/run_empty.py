"""
Problem: Write a function to find if two strings are rotations of each other.

Example 1   Input: "ABC", "BCA"
            Output: True

Example 2	Input: "ABC", "CAB"
            Output: True

Example 3	Input: "ABC", "CBA"
            Output: False
"""


def string_rotation(var1, var2):
	# Check if the variables are even the same length
	if (len(var1) != len(var2)):
		return false
	elif (var1 == var2):
		return True

	# If the string or any variation of it matches, return True.
	for i in range(len(var2)):
		temp = var2[i:]
		temp = temp + var2[0:i]
		if (temp == var1):
			return True
	# Else return false
	return False

print(string_rotation('ABCDEFG', 'BCDEFGA'))
print(string_rotation('ABC', 'CAB'))
print(string_rotation('ABC', 'CBA'))
