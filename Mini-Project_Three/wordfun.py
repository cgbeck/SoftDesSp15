from pattern.web import *
from pattern.en import *
import random
import pickle

"""
Overall, interesting project. I think this is a valuable thing to be able to do with Wikipedia articles.

You had some great insight in your reflection on searches. Yours, as you mentioned, wasn't too efficient,
while the preset function does. Welcome to a common programming problem haha. Like you said though, if
you had a bunch of nested loops, this would be why. A single loop inside a loop runs on n squared time,
which you can imagine gets very large for big datasets. If you want to understand searching more in depth,
as you mentioned you were interested in, there is a whole course on algorithms. You may be interested in 
looking into the binary search algorithm. However, this is more for your understanding than in an actual
project, where you would just use the preset function. Getting simpler things done by a library can let
you do cooler things on your own - don't see that as a limitation.

Otherwise, good job with thinking about the user interaction and customizability - that's always 
a good thing to think about

However, please please work on making your code clean and readable. Seperate your huge function into
smaller chunks, etc. Check my specific comments.

+Functionality: 5/5
+Documentation: 4/5 (Work on file organization and making your code more intuitive)
+Style: 4/5 (Split your funcitons more, make everything more readable)
+CheckIn: yes
+Total: 4.25/5

"""

# # Save data to a file (will be part of your data fetching script)
# f = open('dickens_texts.pickle','w')
# pickle.dump(charles_dickens_texts,f)
# f.close()

# # Load data from a file (will be part of your data processing script)
# input_file = open('dickens_texts.pickle','r')
# reloaded_copy_of_texts = pickle.load(input_file)

w = Wikipedia()
indent = '	'


def chooseRandom(numArticles):
	artCheck = []
	for i in numArticles:
		x = random.randint(0,len(w))
		artCheck.append(x)
	return artCheck

#Hmm, what are all these empty functions doing?
def getArticle(artCheck):
	pass

def investigate(article):
	pass

def wordCount(string):
	pass

#You have a ton of stuff inside one function. I suggest splitting it up for better readability and
# also making it easier for yourself. Map out your functions and code architecture first, then 
# implement in a readable and most intuitive way

def evaluateArticle(article):
	
	sectionTitles = article.sections
	currentArticle = "Yes"
	print 'Article Abstract'
	for section in article.sections:
		if section.title == article.title:
			print section.string
	print "Below are the sections of the article you chose: "
	# currentArticle = input("Do you want to continue looking at the current article? [Yes/No]: ")
	while currentArticle == "Yes" or currentArticle == "yes":
		for section in article.sections:
		   	print ' ' * section.level + section.title + indent
		if currentArticle == "Yes" or currentArticle == "yes":
			typedSection = input("Choose a section of look at: ")
			for section in article.sections:
				if section.title == typedSection:
					currentText = section.string
					print currentText
					print 'Below is shows positivity of the section (0-1) and subjectivity (0-1)'
					print sentiment(currentText)
					# wordCount(currentText)

			cont = input('Type c to continue: ')
		currentArticle = input("Do you want to continue looking at the current article? [Yes/No]: ")

running = True
choosing = True
errorPrint = "The article you requested does not exist."
search = "Yes"

# I suggest wrapping this in a main function like so, and calling it inside "if __name__ == "__main__"".
# It's cleaner, and won't be called when you're importing this file into another one, for example

def main():
	# Main Code Loop
	print "When asked for input, put you answer in quotes"
	while search == "Yes" or search == "yes":
		while search == "Yes" or search == "yes":
			search = input("Do you want to search for an article? [Yes/No]: ")
			if search == "Yes" or search == "yes":
				typedArticle = input("Choose an Article: ")
				print "Searching..."
				chosenArticle = w.search(typedArticle)
				evaluateArticle(chosenArticle)
			else:
				print "Closing Program..."

if __name__ == "__main__":
	main()