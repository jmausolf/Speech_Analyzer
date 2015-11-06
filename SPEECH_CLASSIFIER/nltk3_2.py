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



#sent = read_speech("2011-12-06_ID1.txt")


"""
f = open("2011-12-06_ID1.txt", 'rU')
#f = open("2014-01-15_ID1.txt", 'rU')
raw = f.read().decode('utf8')
print type(raw)
print len(raw)

sent2 = raw.replace('.', ' ')
sent = remove_non_ascii_2(sent2)

"""

#print sent

#n = 1
group_size = 2
group_list = group_text(text, group_size)
# convert list to set to avoid duplicates
group_set = set(group_list)
#print(group_set)

def get_group_set(group_size, text):
	group_list = group_text(text, group_size)
	group_set = set(group_list)
	return group_set

#ngram1 = get_group_set(1, sent)
#ngram2 = get_group_set(2, sent)
#ngram3 = get_group_set(3, sent)
#ngram4 = get_group_set(4, sent)



def ngram(n, data):
	ngram = get_group_set(n, data)
	return ngram





#print ngram5

# optionally take the word_groups in the set
# and count them in the text
for group in group_set:
    count = text.count(group)
    sf = "'%s' appears %d times in the text"
    #print(sf % (group, count))




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

