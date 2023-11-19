# Week 7 Lab

# Number of words
# Number of characters
# Number of characters excluding white spaces
# Number of sentences
# Number of paragraphs
# Average number of words in a sentence
# Average number of sentences in a paragraph

import re

# https://stackoverflow.com/questions/30768056/importing-external-txt-file-in-python
# https://stackoverflow.com/questions/9233027/unicodedecodeerror-charmap-codec-cant-decode-byte-x-in-position-y-character

f = open('test.txt', 'r' , encoding="utf8")
content = f.read()


test_string = "This is a test sentence, hopefully it doesnt return punction !;^, there are fourteen words"


# 1.number of words
# https://www.geeksforgeeks.org/python-program-to-count-words-in-a-sentence/
# using regex (findall())  to count words in string
res = len(re.findall(r'\w+', test_string))
#print ("The number of words in string are : " + str(res))


# 2.Number of characters
# https://sparkbyexamples.com/python/python-count-characters-in-string/#:~:text=The%20len()%20function%20counts,including%20spaces%20and%20special%20characters.
count = len(test_string)
#print("The number of characters in string are : " + str(count))


# Number of characters excluding white spaces
# https://www.geeksforgeeks.org/python-regex-re-search-vs-re-findall/
# https://www.tutorialspoint.com/python-program-to-count-the-number-of-characters-in-a-string#:~:text=The%20re.,matches%20any%20non%2Dwhitespace%20character.
# A sample regular expression to characters  
regex = '\S'             
match = re.findall(regex, test_string)  
#print("The number of characters exluding white space in string are : " + str(len(match)))

# Number of sentences

# total characters
count =(len(content))
#print(count)

# Number of Sentences
# counting full stops as opposed to sentences
# https://stackoverflow.com/questions/53357577/printing-out-number-of-sentences-in-a-text-file
text = str(content)
num_sentences = str(text.count('.'))
#print("Number of sentences found: {}".format(num_sentences))


# Number of Paragraphs
num_paragraphs = str(text.count('\n'))
#print("Number of paragraphs found: {}".format(num_paragraphs))

# https://stackoverflow.com/questions/48957252/how-can-i-count-how-many-n-new-lines-using-python-and-regular-expressions
newline = len(re.findall("\n\n", content))
#print (newline)



# Average number of words in a sentence
# avg_value = sum(list_of_values) / len(list_of_values)
#sum(len(s) for s in sentences)/len(sentences))
words = len(re.findall(r'\w+', content))
#print("The number of words is", words)
average = ( words / int(num_sentences))
print("The average number is words / sentences", ("%.2f" % average))


# Average number of sentences in a paragraph
# sentences / paragraph
avg_sen = (int(num_sentences) / int(num_paragraphs))
print ("%.2f" % avg_sen)