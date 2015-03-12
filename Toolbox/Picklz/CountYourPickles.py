""" A program that stores and updates a counter using a Python pickle file"""
from os.path import exists
import sys
from pickle import dump, load

global Pickles

def pickleIn(filename):
    filein = './'+str(filename)
    data_file = open(filename,'r+')
    pickles = load(data_file)
    data_file.close()
    return pickles

def pickleOut(filename,pickles):
    fileout = './' +str(filename)
    data_file = open(filename,'w')
    dump(pickles,data_file)
    data_file.close()
    return pickles

def update_counter(filename, reset=False):
	""" Updates a counter stored in the file 'file_name'
	A new counter will be created and initialized to 1 if none exists or if
	the reset flag is True.
	If the counter already exists and reset is False, the counter's value will
	be incremented.
	file_name: the file that stores the counter to be incremented. If the file
	doesn't exist, a counter is created and initialized to 1.
	reset: True if the counter in the file should be rest.
	returns: the new counter value
	>>> update_counter('blah.txt',True)
	1
	>>> update_counter('blah.txt')
	2
	>>> update_counter('blah2.txt',True)
	1
	>>> update_counter('blah.txt')
	3
	>>> update_counter('blah2.txt')
	2
	"""

	if reset:
		Pickles = 1
		pickleOut(filename,Pickles)
	else:
		if exists(filename):
			Pickles = pickleIn(filename)
			Pickles += 1
			pickleOut(filename,Pickles)
		else:
			Pickles = 1
			pickleOut(filename,Pickles)
	return Pickles


if __name__ == '__main__':
	if len(sys.argv) < 2:
		import doctest
		doctest.testmod()
	else:
		pass