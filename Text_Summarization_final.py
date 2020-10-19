# -*- coding: utf-8 -*-
"""
Created on Mon Oct 19 11:12:21 2020

@author: yashj
"""


#TEXT SUMMARIZATION
#!pip install beautifulsoup4
#Needed to extract the data from website which is in html and xml format
#!pip install lxml
#Fetching article from wikipedia
#Import Libraries
#
import bs4 as bs #beautifulsoup4
import urllib.request #To extract data from website, also useful for web scrapping
import re #regular expression(NLP),to remove unnecessary things from data
import nltk #natural language tool kit
#nltk.download()
#Data Collection/Extraxtion
web_url=input()
scrapped_data=urllib.request.urlopen(web_url)
#print(scrapped_data)
#urlopen() to open particular website
article = scrapped_data.read()
#read() to convert data into readble format
#print(article)
#data contains HTML tags and attributes
#To remove HTML tags beautifulsoup4 library is used. It is very strong library for web scrapping based projects
parsed_article=bs.BeautifulSoup(article,'lxml')
#print(parsed_article)
#Data Preprocessing - I
#data is present in paragraph form
paragraphs = parsed_article.find_all('p')  #paragraph tag
#print(paragraphs)
article_text=""
for p in paragraphs:
    article_text+=p.text
#print(article_text)
#Data is free from HTML tags
#It is a form of web scrapping
#Data Preprocessing - II
#Lower Case
#
#article_text=article_text.lower()
#Punctuation Removal
#
#from string import punctuation
#def remove_punctuation(s):
#    return ''.join(c for c in s if c not in punctuation)
##text="Hello! how are you doing?"
##text=remove_punctuation(text)
##print(text)
#article_text=remove_punctuation(article_text)
##print(article_text)
#Removal of Numeric Digits
#
##To remove the numbers, you can use .isnumeric() or .isdigit()
#output=''.join(c for c in article_text if not c.isdigit())
##print(article_text)
#Removing Other things using re
#
#Removing Square Brackets and extra spaces
article_text=re.sub(r'\[[0-9]*\]', ' ',article_text)
article_text=re.sub(r'\s+', ' ',article_text)
#print(article_text)
# Removing Special characters and digits
formatted_article_text=re.sub('[^a-zA-Z]',' ',article_text)
formatted_article_text=re.sub(r'\s+',' ',formatted_article_text)
#print(formatted_article_text)
#Tokenization
#Converting text to sentences
#sentence tokenization
sentence_list=nltk.sent_tokenize(article_text) 
len(sentence_list)
#print(sentence_list)
#Removing Stopwards
#Stopward removal
#nltk.download('stopwords')
stopwords=nltk.corpus.stopwords.words('english')
#Frequencies of words
#
#Collect the frequency of words
word_freq={}
for word in nltk.word_tokenize(formatted_article_text):
    if word not in stopwords:
        if word not in word_freq.keys():
            word_freq[word]=1
        else:
            word_freq[word]+=1
#print(word_freq)
#word_freq
#Normalization of frequencies
#Scaling of frequencies
max_freq=max(word_freq.values())
for word in word_freq.keys():
    word_freq[word]=(word_freq[word]/max_freq)
    #print(word_freq[word])
#Calculationg the sentence score
#
sentence_score = {}
#print(sentence_list)
for sent in sentence_list:
    for word in nltk.word_tokenize(sent.lower()):
        if word in word_freq.keys():
            if len(sent.split(' ')) < 30:
                if sent not in sentence_score.keys():
                    sentence_score[sent] = word_freq[word]
                else:
                    sentence_score[sent] += word_freq[word]
                    #print(sentence_score[sent])
#Getting Summary
 
import heapq
summary_sentences=heapq.nlargest(7, sentence_score, key=sentence_score.get)
summary = ' '.join(summary_sentences)
print(summary)