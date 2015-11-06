###################################
###                             ###
###      Joshua G. Mausolf      ###
###   Department of Sociology   ###
###    Computation Institute    ###
###    University of Chicago    ###
###                             ###
###################################

import re
import pandas as pd
import numpy as np

# group a text into groups of words
# used Python31 should work with Python26
def group_text(text, group_size):
    """
    groups a text into text groups set by group_size
    returns a list of grouped strings
    """
    word_list = text.split()
    group_list = []
    for k in range(len(word_list)):
        start = k
        end = k + group_size
        group_slice = word_list[start: end]
        # append only groups of proper length/size
        if len(group_slice) == group_size:
            group_list.append(" ".join(group_slice))
    return group_list
        


text = "Wall Street billionaires should pay their fair share. We need an America where everyone gets a fair shake. American jobs are important to ensure wealth for everyone. Warren Buffett's secretary. We must shape unemployment to meet our needs."
#sent = text.replace('.', ' ')


def remove_non_ascii_2(text):
	import re
	#return re.sub(r'[^\xe2]+', "'", text)
	return re.sub(r'[^\x00-\x7F]+', "'", text)


def read_speech(speechfile):
	speech = str(speechfile)
	f = open(speech, 'rU')
	raw = f.read().decode('utf8')
	raw1 = raw.replace('.', ' ')
	sent = remove_non_ascii_2(raw1)
	return sent




def get_group_set(group_size, text):
	group_list = group_text(text, group_size)
	group_set = set(group_list)
	return group_set




def ngram(n, data):
	ngram = get_group_set(n, data)
	return ngram




terms = ["We", "gets a fair shake", "jobs", "fair", "fair share", "economy", "unemployment", "99", "99 percent", "1 percent", "1", "wealthy", "loophole", "main street", "Warren Buffett", "Warren Buffett's secretary", "secretary", "income", "wealth", "occupy", "occupying", "tax rate", "middle class", "upper class", "working class", "lobby", "corporate", "fair shot", "special interests", "lower class", "poor", "poverty", "rich", "inequality", "class", "America", "Wall Street", "Wall Street billionaires"]





def speech_phrase_counter(ngram1, ngram2, ngram3, ngram4, terms):
	#print "FUNCTION TEST"
	for term in terms:
		for gram in ngram4:
			if term == gram:
				count = sent.count(gram)
				print "Count: ", count, "| ", gram
		for gram in ngram3:
			if term == gram:
				count = sent.count(gram)
				print "Count: ", count, "| ", gram
		for gram in ngram2:
			if term == gram:
				count = sent.count(gram)
				print "Count: ", count, "| ", gram
		for gram in ngram1:
			if term == gram:
				count = sent.count(gram)
				print "Count: ", count, "| ", gram

#speech_phrase_counter(ngram1, ngram2, ngram3, ngram4, terms)

"""
speeches = ["2014-01-15_ID1.txt", "2014-01-16_ID1.txt",  "2011-12-06_ID1.txt"]

for speech in speeches:
	print speech
	sent = read_speech(speech)

	ngram1 = get_group_set(1, sent)
	ngram2 = get_group_set(2, sent)
	ngram3 = get_group_set(3, sent)
	ngram4 = get_group_set(4, sent)

	speech_phrase_counter(ngram1, ngram2, ngram3, ngram4, terms)




date = "date"
time = "time"
location = "location"



try:
	f=open('speech_data.csv', 'a')
	#for term in terms:
	#f.write(u"TERMS \n")
	f.write(u"DATE, TIME, LOCATION, We, gets a fair shake, jobs, fair, fair share, economy, unemployment, 99, 99 percent, 1 percent, 1, wealthy, loophole, main street, Warren Buffett, Warren Buffett's secretary, secretary, income, wealth, occupy, occupying, tax rate, middle class, upper class, working class, lobby, corporate, fair shot, special interests, lower class, poor, poverty, rich, inequality, class, America, Wall Street, Wall Street billionaires \n")
finally:
	f.close()
"""


def speech_phrase_counter2(ngram1, ngram2, ngram3, ngram4, terms, df, n):
	#print "FUNCTION TEST"
	for term in terms:
		for gram in ngram4:
			if term == gram:
				count = sent.count(gram)
				df.ix[n, term] = count
		for gram in ngram3:
			if term == gram:
				count = sent.count(gram)
				df.ix[n, term] = count
		for gram in ngram2:
			if term == gram:
				count = sent.count(gram)
				df.ix[n, term] = count
		for gram in ngram1:
			if term == gram:
				count = sent.count(gram)
				df.ix[n, term] = count


#Setup Initial Data Frame
header = ["DATE", "TIME", "LOCATION"]+terms
index = np.arange(0)
df = pd.DataFrame(columns=header, index = index)






speeches = ["2014-01-15_ID1.txt", "2014-01-16_ID1.txt", "2014-01-17_ID1.txt", "2011-12-06_ID1.txt"]


for speech in speeches:
	#print speech
	date = speech.split('_')[0]
	#print date

	#print "NUMBER IN INDEX", len(df.index)

	n = len(df.index)
	#print n

	#Add Row to Data Frame
	#df.loc[3] = "value", where 3 = the number of the next data row
	df.loc[n] = 0
	df.ix[n, "DATE"] = date

	sent = read_speech(speech)

	ngram1 = get_group_set(1, sent)
	ngram2 = get_group_set(2, sent)
	ngram3 = get_group_set(3, sent)
	ngram4 = get_group_set(4, sent)

	speech_phrase_counter2(ngram1, ngram2, ngram3, ngram4, terms, df, n)



print df
df.to_csv("test_csv.csv", encoding='utf-8')


