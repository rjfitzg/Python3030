'''
given a string, retuns the first recurring string in that string
ie.
	recur_string('abcda')
		return 'a'
	recur_String('asdfghdjiuk')
		return d
'''

def recur_string(var1):
	temp = []
	for let in var1:
		if let in temp:
			return let
		temp.append(let)


print(recur_string('abcda')) # a
print(recur_string('ujmyhnj')) # j

