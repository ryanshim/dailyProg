''' r/dailyprogrammer [Easy] Challenge 20: Primes under 2000'''

def find_primes(n):	

	primes = []

	for p in range(2, n+1):
		for i in range(2, p):
			if p % i == 0:
				break
		else:
			primes.append(p)
	print primes

find_primes(2000)