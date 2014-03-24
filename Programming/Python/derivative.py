#!/usr/bin/python

"""
Author: 		David Selassie Opoku

Description:	A Python program that takes a polynomial in standard algebraic
				notation and outputs the required derivative.

Use:			Interactive or batch mode
				
Interactive mode 	: 	python derivative.py 

batch mode 		 	:	python derivative.py 'polynomial expr' 'n'


expr: 			Polynomial expression. e.g: 5x^4+3x^2
n:				n-th derivative to calculate i.e 1 for 1st derivative, 2 for 2nd and so on.
"""

import sys
import re

def main():
	# Get user expression input
	# Check validity of input
	# Parse input to determine various terms
	# Derive derivative for each term
	# Combine derivatives of each term
	# Return final derivative

					      
	if len(sys.argv) < 2:		# sys.argv is list storing command-line parameters
		interactive_mode()

	else:
		batch_mode()



def interactive_mode():
	"""Runs program in interactive mode.

		Type quit to exit.
	"""

	print 'Type quit to exit'
	expr = raw_input('Enter polynomial expression: ').strip()
	while expr.lower() != 'quit':
		expr = check_expression(expr)
		n    = raw_input('Enter whole number(n) for n-th derivative. Eg: 0, 1,2: ')
		n    = int(n.strip())
		n    = check_n(n)
		expr = expr.strip()
		answer = solve_derivative(expr,n)
		print 'Derivative: %s'  %(answer)
		print '' 
		expr = raw_input('Enter polynomial expression: ').strip()
	print 'Hope this was helpful! Bye :)'


def batch_mode():
	"""Runs program in batch mode."""
	expr = str(sys.argv[1])
	n 	 = int(sys.argv[2])
	print solve_derivative(expr,n)

def check_expression(expr):
	""" Checks whether expression entered. Asks user to enter expr if not.

	expr 	polynomial expression entered by user

	"""

	expr = str(expr)

	while len(expr) < 1:
		print 'INVALID ENTRY! Need to enter an expression'
		expr = raw_input('Enter polynomial expression: ')
	return expr


def check_n(n):
	""" Checks whether n is a whole number. Asks user to re-enter number if not."""

	#while type(n)  != int:
	#	print 'INVALID ENTRY! You did not enter a number'
	#	n = raw_input('Enter a whole number: ')

	while n  < 0 :
		print 'INVALID ENTRY! You did not enter a whole number'
		n = int(raw_input('Enter a whole number: ').strip())

	return n



def get_terms(expr):
	"""Return individual terms of polynomial expression

	expr  	standard polynomial expression 

	"""
	expr = expr.replace(' ','')
	p = re.compile(r'[-+]*\d+\w\^*\d*')
	terms = p.findall(expr)

	return terms


def derivative(term):
	"""Return the derivative of a given term

	term 	unit term of expression e.g. x^3
	"""

	coeff, variable, power = get_coeff_var_power(term)
	
		
	# calculate new coefficient, variable and power for  derivative
	deriv_coeff = coeff*power
	deriv_power = power  - 1

	# return zero if derivative coefficient is zero
	if deriv_coeff == 0:
		deriv = 0

	# just return coefficient if derivative power is zero 
	elif deriv_power == 0:
		deriv = deriv_coeff

	# just return term with coefficient and variable if derivative power is one
	elif deriv_power == 1:
		deriv = '%s%s'	%(deriv_coeff,variable)


	else:
		deriv = '%s%s^%s' %(deriv_coeff,variable,deriv_power)

	return str(deriv)



def get_coeff_var_power(term):
	"""Returns the coefficient,variable and power for a given term."""

	term_split = term.split('^')
	base_term = term_split[0]

	# get coeff and variable
	if len(base_term) == 1:
		if base_term[-1].isdigit():
			coeff = int(base_term[-1])
			variable = ''
		else: 
			coeff = 1
			variable = base_term[-1]
	else:
		coeff = int(base_term[:-1])
		variable = base_term[-1]


	# get power
	if len(term_split) == 2:
		power = int(term_split[-1])

	elif len(term_split) == 1 and variable.isalpha():
		power = 1
	else:
		power = 0

	return coeff, variable, power

def form_answer(answer):
	""" Joins terms from answer list to form final expr.

	answer  : list containing derivative terms
	"""

	final = answer[0]
	for term in answer[1:]:
		if term[0] == '-':
			final += term
		else:
			final += '+%s' %(term)
	return final 


def solve_derivative(expr, n):
	""" Returns solved derivative of polynomial expression

	expr 	expression to calculate derivative of
	n 		n-th derivative to calculate

	e.g: 	solve_derivative('5x^4+3x^2', 1) --> 20x^3+6x
			solve_derivative('5x^4+3x^2', 2) --> 60x^2+6

	"""

	if  n == 0:
		return expr
	else:

		terms= get_terms(expr)
		list_derv =[]

		for term in terms:
			derv = derivative(term.strip())
			list_derv.append(derv)


		if len(list_derv) == 1 and list_derv[0] == '0':
			answer = list_derv[0]

		else:
			answer = [ drvt for drvt in list_derv if drvt != '0']
			answer = form_answer(answer)
		return solve_derivative(answer,n-1)


if __name__ == '__main__':
	main()
