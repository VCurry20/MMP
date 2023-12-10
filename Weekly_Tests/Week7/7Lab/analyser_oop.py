# OOP Solution



# Number of words
# Number of characters
# Number of characters excluding white spaces
# Number of sentences
# Number of paragraphs
# Average number of words in a sentence
# Average number of sentences in a paragraph


# sentences and paragraphs are made of of words and characters 
# we test the numnber of characters and words to make up each
# paragraphs are made up of chars, words and sentences - paragraphs are the super class
# Do we need a word class with just char?

import csv
import re

class document(object):
    def __init__(self, filename):
        self.filename = filename


    def review_txt_file(self):
        f = open(self.filename, 'r' , encoding="utf8")
        file= f.read()
        #self.file = file
        print("this is the file", file)


    def characters(file):
        count=(len(file))
        print("The number of characters is", count)

    
    def words_in_file(file):
        res = len(re.findall(r'\w+', file))
        
        
        print ("The number of words in string are : " + str(res))
        

    def sentences(file):
        txt = str(file)
        sentence= str(txt.count('.'))
        print("The number of sentences is", sentence)
        


class paragraph():
    def __init__(self, words):
        #self.spaces = spaces
        #self.char = char
        self.words = words


    def count_paragraphs():
        num_paragraphs = str(document.count('\n'))
        print("Number of paragraphs found: {}".format(num_paragraphs))

    



class sentence():
    def __init__(self, words):
        #self.spaces = spaces
        #self.char = char
        self.words = words


    def sentence_len ():
        pass


       
    
if __name__=="__main__":

    d= document('text.txt')
    print(d)

    #doc = d.review_txt_file()
    #print (doc)





    


