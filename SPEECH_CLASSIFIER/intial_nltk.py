##################################
###                            ###
###      Joshua G. Mausolf     ###
###    Computation Institute   ###
###    University of Chicago   ###
###                            ###
##################################

import nltk
from nltk.tokenize import sent_tokenize




with open("2014-01-15_ID1.txt", 'rU') as speech:
		#reader = csv.reader(urls_file)
		lines = list(speech)
		#Xpotus = len(lines)
		#print "Requested President speech:", lines
		#print speech
		for sent in speech:
			print (sent_tokenize(str(speech)))
		
		#print len(speech.words())
		#print type(lines), type(speech)

for sent in lines:
	(sent_tokenize(str(lines)))

f = open("2014-01-15_ID1.txt", 'rU')
raw = f.read()




text = raw.decode("utf8")

#text = lambda raw: raw.decode('utf8', 'ignore')
#print raw

print text

sents = sent_tokenize(text)
#print sents
print len(sents)

#for sent in speech:
#	sent_tokenize(str(speech))

#from nltk.corpus import brown

#print brown.words()[0:10]
#print brown.tagged_words()[0:10]
#print len(brown.words())

