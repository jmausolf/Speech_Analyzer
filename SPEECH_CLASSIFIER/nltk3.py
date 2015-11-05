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
        
text = "Wall Street billionaires should pay their fair share. We need an America where everyone gets a fair shake. American jobs are important to ensure wealth for everyone. We must shape unemployment to meet our needs."
sent = text.replace('.', ' ')
print sent

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

ngram1 = get_group_set(1, sent)
ngram2 = get_group_set(2, sent)
ngram3 = get_group_set(3, sent)
ngram4 = get_group_set(4, sent)

# optionally take the word_groups in the set
# and count them in the text
for group in group_set:
    count = text.count(group)
    sf = "'%s' appears %d times in the text"
    #print(sf % (group, count))


"""
#Awesome, this seems to work for this small example. 
for group in group_set:
	if "Wall Street" == group:
		print "Hell yeah"


for gram in ngram2:
	if "Wall Street" == gram:
		print "Double Hell yeah"


for gram in ngram3:
	gram_count = 0
	if "Wall Street billionaires" == gram:
		gram_count +=1
		print "Count: ", gram_count, "| ", gram

"""


terms = ["We", "gets a fair shake", "jobs", "fair", "fair share", "economy", "unemployment", "income", "wealth", "inequality", "class", "America", "Wall Street", "Wall Street billionaires"]

for term in terms:
	for gram in ngram4:
		count = sent.count(gram)
		if term == gram:
			print "Count: ", count, "| ", gram
	for gram in ngram3:
		count = sent.count(gram)
		if term == gram:
			print "Count: ", count, "| ", gram
	for gram in ngram2:
		count = sent.count(gram)
		if term == gram:
			print "Count: ", count, "| ", gram
	for gram in ngram1:
		count = sent.count(gram)
		if term == gram:
			print "Count: ", count, "| ", gram



