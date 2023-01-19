# 4. WAP to print sum of n terms of series 1+11+111+1111+....
def summation(n):
	sum = 0
	j = 1
	
	for i in range(1, n + 1):
		sum = sum + j
		j = (j * 10) + 1
		
	return sum
		
# Driver Code
n = 5
print(summation(n))
