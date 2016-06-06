def base26encode(number, alphabet="0123456789ABCDEFGHIJKLMNOP"):
	'''convert integer to base26 string'''
	if not isinstance(number, (int, long)):
		raise TypeError("Number must be an integer")

	base26 = ""
	sign = ""

	if number < 0:
		sign = "-"
		number = -number

	if 0 <= number < len(alphabet):
		return sign + alphabet[number]

	while number != 0:
		number, i = divmod(number, len(alphabet))
		base26 = alphabet[i] + base26

	return sign + base26

def alphadecode(number, alphabet="ABCDEFGHIJKLMNOPQRSTUVWXYZ"):
	result = ''
	for x in number:
		for i in xrange(len(alphabet)):
			if x == alphabet[i]:
				result += str(i)
	return result

sample_1 = "CSGHJ"
sample_2 = "CBA"
sample_3 = 218679

decoded_1 = alphadecode(sample_1)
decoded_2 = alphadecode(sample_2)

result = base26encode(int(decoded_1)*int(decoded_2))
print result