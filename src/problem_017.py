#!/usr/bin/env python

def num_to_words(n):
	units_dict = {
		"1": "one",
		"2": "two",
		"3": "three",
		"4": "four",
		"5": "five",
		"6": "six",
		"7": "seven",
		"8": "eight",
		"9": "nine"
	}

	teens_dict = {
		"10": "ten",
		"11": "eleven",
		"12": "twelve",
		"13": "thirteen",
		"14": "fourteen",
		"15": "fifteen",
		"16": "sixteen",
		"17": "seventeen",
		"18": "eighteen",
		"19": "nineteen"
	}

	decimals_dict = {
		"2": "twenty",
		"3": "thirty",
		"4": "forty",
		"5": "fifty",
		"6": "sixty",
		"7": "seventy",
		"8": "eighty",
		"9": "ninety"
	}

	n = str(n)

	#thousands
	thousands_s = ""
	if len(n) > 3 and n[-4] != "0":
		thousands_s = "{0} thousand".format(units_dict[n[-4]])

	#hundrends
	hundreds_s = ""
	if len(n) > 2 and n[-3] != "0":
		hundreds_s = "{0} hundred".format(units_dict[n[-3]])

	# decimals
	decimals_s = ""
	if len(n) > 1:
		if n[-2:] in teens_dict:
			decimals_s = teens_dict[n[-2:]]
		elif n[-2] != "0":
			decimals_s = decimals_dict[n[-2]]
	
	#units
	units_s = ""
	if len(n) <= 1 or n[-2:] not in teens_dict:
		if n[-1] != "0":
			units_s = units_dict[n[-1]]

	#conjuction
	conjuction_s = ""
	if hundreds_s != "" and (decimals_s != "" or units_s != ""):
		conjuction_s = " and "

	#hyphen
	hyphen_s = ""
	if decimals_s != "" and units_s != "":
		hyphen_s = "-"

	return thousands_s + hundreds_s + conjuction_s + decimals_s + hyphen_s + units_s


"""https://projecteuler.net/problem=17"""
if __name__ == '__main__':
	length = 0

	for n in range(1, 1001):
		length += len(num_to_words(n).replace(" ", "").replace("-", ""))

	print(length)

