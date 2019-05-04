'''
Given an set of numbers, and an integer; find if any 2 numbers add to the given integer
ie.
	def pairHasSum([1,2,3,4], 8)
		return False
	def pairHasSum([1,2,4,4], 8)
		return True
'''

def pairHasSum(pair_arr, sum_val):
	'''
	Work from either end of the array to cut the cost of the algorthm down while still finding correct matches.
	'''
	low = 0
	high = len(pair_arr) -1
	while (low<high):
		temp = pair_arr[low] + pair_arr[high]
		if (temp==sum_val): return True
		elif (temp>sum_val): high -= 1
		elif (temp<sum_val): low += 1
	# If no value was found before high/low crossed, there was no sum.
	return False

print(pairHasSum([1,2,3,4], 8))
print(pairHasSum([1,2,4,4], 8))
