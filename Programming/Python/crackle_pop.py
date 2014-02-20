#! /usr/bin/python


def main():
	crackle_pop1(1,100)

def crackle_pop1(start,stop):
	""" Prints numbers from start to stop. Prints Crackle, Pop or CracklePop if number is divisible by 3, 5 or 3 and 5 respectively

	start  number that begins the sequence

	stop   number that ends the sequence
	"""

	if(start%3==0 and start%5==0):
		print "CracklePop"

	elif(start%3==0):
		print "Crackle"

	elif(start%5==0):
		print "Pop"

	else:
		print start

	if stop == start:
		return

	else:
		return crackle_pop1(start+1, stop)


def crackle_pop2(start,stop):
	for num in range(start,stop+1):
		if(num%3==0 and num%5==0):
			print "CracklePop"

		elif(num%3==0):
			print "Crackle"

		elif(num%5==0):
			print "Pop"

		else:
			print num

if __name__ == '__main__':
	main()

