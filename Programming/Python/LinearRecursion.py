#!/usr/bin/python

def linear_sum(S,n):
	"""Return the sum of the first n numbers of sequence S."""

	if n == 0:
		return 0

	else:
		return linear_sum(S, n-1) + S[n-1] 



def reverse(S, start, stop):
	"""Reverse elements in implicit slice S[start:stop]."""

	if start < stop:								# if at least 2 elements
		S[start], S[stop] = S[stop], S[start]		# swap first and least
		reverse(S, start +1, stop-1)				# recur on rest




def power(x,n):
	"""Compute the value of x**n for integer n."""

	if n  == 0:
		return 1

	else:
		return x * power(x, n-1)



def power2(x,n):
	"""Compute the value x**n for integer n."""

	if n == 0:
		return 1


	else:
		partial = power(x, n//2)			# rely on truncated division
		result = partial* partial

		if n % 2 == 1:						# if n odd, include extra factor of x
			result *= x

		return result