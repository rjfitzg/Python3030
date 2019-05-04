"""
Problem:  Write a method which will remove any given character from a String.
Note: You cannot use methods like .remove(), .replace(), .sub()... You have to code your own method.

Example 1   Input: "Hello world!", "!"
            Output: "Hello world"

Example 2	Input: "Hello world!", "o"
            Output: "Hell wrld!"

Example 3	Input: "The string is the most common thing you come across on any programming language.", "t"
            Output: "The sring is he mos common hing you come across on any programming language."
"""


def remove(string, character):
	return_string = ""
	for i in range(len(string)):
		if not (string[i]==character):
			return_string += string[i]
	return return_string

print(remove('The string is the most common thing you come across on any programming language.', 't'))
