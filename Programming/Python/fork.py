#! /usr/bin/python

import os

def main():
	if (not os.fork() or not os.fork()):
		print "AA"

	elif(not os.fork() and os.fork()):
		print "BB"

	else:
		print "CC"

if __name__ == '__main__':
	main()