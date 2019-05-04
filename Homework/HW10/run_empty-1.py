"""
Problem:  Find all pairs in an array of integers whose sum is equal to the given number.

Example 1   Input: [1, 2, 3], 5
            Output: [(2, 3), (3, 2)]

Example 2	Input: [1, 2, 3, 4, 5], 8
            Output: [(3, 5), (4, 4), (5, 3)]

Example 3	Input: [1, 2, 3], 8
            Output: []
"""


def find_pairs(array, num):
	# Set up array to be sent back
	pair_array = []

	# Check if array values can even match number.
	if (sum(array) < num):
		return pair_array

	for i in range(len(array)):
		for j in range(i, len(array)):
			pass

print(find_pairs([1,2,3], 5))
print(find_pairs([1,2,3,4,5], 8))
print(find_pairs([1,2,3], 8))
