from fractions import Fraction

def continued_fractions(num):
	"""Computes the improper fraction of a continued
	fraction given a continued fraction 
	written in Gauss representation.
	Computes the Gauss representation of a continued
	fraction given an improper fraction.


	>>> continued_fractions("45/16")
	"[2;1,4,3]"

	>>> continued_fractions("[2;1,7]")
	"23/8"
	"""

	if "/" in num:
		num = fraction_parser(num)
		result = continued_fractions_helper(num)
		return "[" + str(result[0]) + ";" \
			+ ",".join(map(str, result[1:])) + "]"
	else:
		num = gauss_parser(num)
		result = continued_fractions_helper(num)
		return str(result.numerator) + "/" + str(result.denominator)

def continued_fractions_helper(num):
	"""Recursively computes the Gauss representation 
	or the improper of the given input of
	the continued_fractions function."""

	if type(num) is list:
		if len(num) == 0:
			return 0
		elif len(num) == 1:
			return num[0]
		else:
			return num[0] + Fraction(1, continued_fractions_helper(num[1:]))

	if type(num) is Fraction:
		if num.numerator % num.denominator == 0:
			return [num.numerator // num.denominator]
		else:
			return [num.numerator // num.denominator] \
				+ continued_fractions_helper(Fraction(num.denominator, num.numerator % num.denominator))



def gauss_parser(num):
	"""Takes a Gauss representation and converts it into a list."""

	first_num, rest = num[1:-1].split(";")
	rest = rest.split(",")
	result = [int(first_num)] + [int(x) for x in rest]
	return result

def fraction_parser(num):
	"""Take an improper fraction and converts it into a Fraction object."""
	
	num, denom = num.split("/")
	return Fraction(int(num), int(denom))