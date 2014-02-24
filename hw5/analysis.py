from wrappers import debug
import operator
from pattern.en import *
@debug
def wordFrequency(text):
	"""
	Performs word Frequency of text and returns a freq. dict
	"""
	words = dict()
	for word in text.split():
		words[word] = words.get(word, 0) + 1
	return words

@debug 
def mostFrequentWord(text):
	"""
	Looks at the top 10 most frequent words
	"""
	return sorted(text.iteritems(), key=operator.itemgetter(1), reverse = True)[:10]

@debug
def linguistics(text):
	return sentiment(text)


if __name__ == "__main__":
	wordFrequency("chris was chris was here and there")