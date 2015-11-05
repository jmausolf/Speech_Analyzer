##################################
###                            ###
###      Joshua G. Mausolf     ###
###    Computation Institute   ###
###    University of Chicago   ###
###                            ###
##################################

import nltk
from nltk.tokenize import *


"""

with open("2014-01-15_ID1.txt", 'rU') as speech:
		#reader = csv.reader(urls_file)
		lines = list(speech)
		#Xpotus = len(lines)
		#print "Requested President speech:", lines
		#print speech
		for sent in speech:
			print (sent_tokenize(str(speech)))
		
		#print len(speech.words())
		print type(lines), type(speech)
		print lines[1:6]






#for sent in lines:
#	(sent_tokenize(str(lines)))
		
"""

def namestr(obj, namespace):
    return [name for name in namespace if namespace[name] is obj]




f = open("2014-01-15_ID1.txt", 'rU')
raw = f.read().decode('utf8')
#print type(raw)
#print len(raw)
#print raw[:75]

tokens = word_tokenize(raw)
#print type(tokens), len(tokens)
#print tokens[:10]

"""
jobs = 0
economy = 0
unemployment = 0

for tok in tokens:
	if tok == "House":
		print tok
	elif tok == "jobs":
		print tok
		jobs += 1
	elif tok == "economy":
		print tok
		economy += 1
	elif tok == 'unemployment':
		unemployment += 1


print "Total times 'jobs' mentioned: ", jobs

print "Total times 'economy' mentioned: ", economy

print "Total times 'unemployment' mentioned: ", unemployment 
"""


def counter():
	terms = ["jobs", "economy", "unemployment", "income", "wealth", "inequality", "class", "America"]


	for term in terms:
		count = 0
		for tok in tokens:
			if tok == term:
				count += 1

		print "Total count ", term, ": ", count

#counter()



#text = raw.decode("utf8")

#for word in text:
#	if word == "jobs":
#		print word
#	else:
#		print word

#text = lambda raw: raw.decode('utf8', 'ignore')
#print raw

#print text

#sents = sent_tokenize(text)
#print sents
#print len(sents)
#print type(sents), sents[1:20]


# regular expression that was successful online:
# /([A-Z])\w+:|([Q])\s+/g

import re
#new_speaker = re.compile("\d?(\(?\d{3}\D{0,3}\d{3}\D{0,3}\d{4})")
new_speaker = re.compile("/([A-Z])\w+:|([Q])\s+/g")

for tok in raw:
	new_speaker = re.compile("/([A-Z])\w+:|([Q])\s+/g")
	#print new_speaker
	#result = new_speaker.sub(lambda m: re.sub('\g', '', m.group(1)), tok)
	#print result

	re_newspeaker = re.compile('^(<bullet> |  )(?P<name>(%s|(((Mr)|(Ms)|(Mrs))\. [-A-Za-z ]+( of [A-Z][a-z]+)?))|((The ((VICE|ACTING|Acting) )?(PRESIDENT|SPEAKER|CHAIR(MAN)?)( pro tempore)?)|(The PRESIDING OFFICER)|(The CLERK)|(The CHIEF JUSTICE)|(The VICE PRESIDENT)|(Mr\. Counsel [A-Z]+))( \([A-Za-z.\- ]+\))?)\.')
	result = re_newspeaker.sub(lambda m: re.sub('\g', '', m.group(1)), tok)
	print result
	#print re_newspeaker


for word in text:
	pass
	#new_speaker = re.compile("/([A-Z])\w+:|([Q])\s+/g")
	#print new_speaker
	#result = new_speaker.sub(lambda m: re.sub('\g', '', m.group(1)), word)
	#print result

	#re_newspeaker =         r'^(<bullet> |  )(?P<name>(%s|(((Mr)|(Ms)|(Mrs))\. [-A-Za-z ]+( of [A-Z][a-z]+)?))|((The ((VICE|ACTING|Acting) )?(PRESIDENT|SPEAKER|CHAIR(MAN)?)( pro tempore)?)|(The PRESIDING OFFICER)|(The CLERK)|(The CHIEF JUSTICE)|(The VICE PRESIDENT)|(Mr\. Counsel [A-Z]+))( \([A-Za-z.\- ]+\))?)\.'
	#print re_newspeaker

