from nltk.util import ngrams
from nltk.tokenize import *
#sentence = 'this is a foo bar sentences and i want to ngramize it'
sentence = "Wall Street billionaires should pay their fair share. We need an America where everyone gets a fair shake."
n = 1
sixgrams = ngrams(sentence.split(), n)
#for grams in sixgrams:
  #print grams
  #print type(grams)
  #print grams[0]

  #for gram in grams:
  	#print gram


def Ngrams(n, sent):
	from nltk.util import ngrams
	sixgrams = ngrams(sentence.split(), n) 
	return sixgrams

grams = Ngrams(n, sentence)






def counter(ngrams):
	terms = ["jobs", "economy", "Wall", "Street", "unemployment", "income", "wealth", "inequality", "class", "America"]


	for term in terms:
		#print term
		count = 0
		for grams in ngrams:
			#print grams
			for tok in grams:
				#print tok
				if str(tok) == str(term):
					print tok
					count += 1

		#print "Total count ", term, ": ", count

#counter(grams)