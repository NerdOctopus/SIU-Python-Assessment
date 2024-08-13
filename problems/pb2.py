# declare and fill out function here
def max_values2(array):
	a = -99999
	b = -99999
	ai = 0
	bi = 0
	i = 0
	for x in array:
		print (array[i])
		if (x > a):
			b = a
			bi = ai
			a = array[i]
			ai = i
		elif (x > b):
			b = array[i]
			bi = i
		i = i+1
	return [ai,bi]

# test case
print(max_values2([-5, -2, -1, -11])) # -> [1, 2]
