from pattern.web import *
from pattern.en import *
import random
import pickle

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

def getArticle(artCheck):
	pass

def investigate(article):
	pass

def wordCount(string):
	pass

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