class CircularBuffer:
	"""Creates a circular buffer  that appends, removes and lists contents."""


	def __init__(self,size):
		"""Creates new instance of Circular Buffer class

		size  maximum size of circular buffer

		"""

		self._n = 0
		self._capacity = 1 
		self._bufffer = ['']*self._size
		self._cur = 0
		self._last = 0


	def get_size():
		""" Returns the maximum size of the Circular Buffer"""
		return self._size

	def append(self, number):
		""" Appends n items to the end of the Circular Buffer

		n  number of items to add to end of buffer

		"""

		if 
		while n > 0:
			content = input()						# get contents from caller
			self._cur %= self._size					# ensure index is not out of range 
			self._circ_buffer[self._cur] = content
			self._cur += 1							# increment current index
			n -= 1

		self._cur += 1


	def remove(self,n):
		""" Removes top n items from list

		n 	number of items to remove from buffer

		"""

		while n > 0:
			self._cur %= self._size
			self._circ_buffer

