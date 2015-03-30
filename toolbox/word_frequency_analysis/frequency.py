""" Analyzes the word frequencies in a book downloaded from
	Project Gutenberg """

import string

filename = './TheAeneidVirgil.txt'
f = open(filename,'r')
lines = f.readlines()
wordList = [] 
wordCountList = []

curr_line = 0
while lines[curr_line].find('*** START OF THIS PROJECT GUTENBERG EBOOK THE AENEID ***') == -1:
    curr_line += 1
startLine = curr_line + 1

curr_line = 0
while lines[curr_line].find('End of the Project Gutenberg EBook of The Aeneid, by Virgil') == -1:
    curr_line += 1
endLine = curr_line - 1

readArea = lines[startLine:endLine]


def get_word_list():
	""" Reads the specified project Gutenberg book.  Header comments,
		punctuation, and whitespace are stripped away.  The function
		returns a list of the words used in the book as a list.
		All words are converted to lower case.
	"""
	n = 1
	m = 0
	curr_line = startLine
	while curr_line != endLine:
		while lines[curr_line][:n] != lines[curr_line]:
			if lines[curr_line][m] == ' ':
				m += 1
			if lines[curr_line][n+1] == ' ':
				wordList.append(lines[curr_line][m:n])
				n += 1
				m = n
			elif lines[curr_line][n] != ' ':
				n += 1
			# print n
			# print m
		curr_line += 1


def get_top_n_words(word_list, n):
	""" Takes a list of words as input and returns a list of the n most frequently
		occurring words ordered from most to least frequently occurring.

		word_list: a list of words (assumed to all be in lower case with no
					punctuation
		n: the number of words to return
		returns: a list of n most frequently occurring words ordered from most
				 frequently to least frequentlyoccurring
	"""
	get_word_list()
	x = 0
	wordPlace = 0
	preExisiting = False
	for word in wordList:
		wordCount = 0
		wordCheck = True
		x = 0
		while wordCheck == True and x < len(wordList)-1:
			if word != wordList[x]:
				preExisiting = False
				x += 1
			else:
				preExisiting = True
				wordCheck = False
				x = 0

		if preExisiting == False:
			currWord = word
			for word in wordList:
				if word == currWord:
					wordCount += 1

			wordCountList.append([currWord,wordCount])

	ordered_by_frequency = sorted(wordCountList, key=word_counts.get, reverse=True)

	listPlace = 0
	while listPlace <= n:
		print wordCountList[listPlace]
		listPlace += 1



get_word_list()

print wordList