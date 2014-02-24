"""
Software Design Homework 5
Web Scraping + Text Analysis
author: chris @ softdes ninjas
"""

from pattern.web import *
import os
import pickle as p
import analysis as an
from wrappers import debug

@debug
def save(data):
	"""
	Saves data temporarily in a pickle file
	"""
	with open('temp.p','wb') as f:
		p.dump(data,f)

@debug
def load():
	"""
	Loads data from a pickle file
	"""
	with open('temp.p','r') as f:
		data = p.load(f)
	return data

@debug
def getText(url):
	"""
	Download the text
	"""
	text = URL(url).download()
	save(text)

@debug
def analyze(text):
	"""
	Do some analysis on the text
	"""
	freq = an.wordFrequency(text)
	most_freq = an.mostFrequentWord(freq)
	#print most_freq
	print an.linguistics(text)


if __name__ == "__main__":
	url = 'http://www.gutenberg.org/ebooks/730.txt.utf-8'
	if not os.path.exists("temp.p"):
		getText(url)
	else:
		analyze(load())
	
	