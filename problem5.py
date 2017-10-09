# -*- coding: utf-8 -*-
"""
Created on Sun Oct  8 21:56:04 2017

@author: kyleh
"""

import codecs
import numpy as np
from sklearn.preprocessing import normalize
from generate import GENERATE
import random

word_index_dict = {}

# TODO: read brown_vocab_100.txt into word_index_dict
file=open('brown_vocab_100.txt', 'rb')
f=file.read()
f=f.decode('utf-16')
f=f.split()
#print(f)
i=0
for word in f:
    word_index_dict[word]=i
    i+=1
#print(word_index_dict)
file.close()

numerators = [0.]*6
denominators = [0.]*6

f = codecs.open("brown_100.txt", encoding = "utf-16")

prev=''
prev2=''
for word in f.read().split():
    word=word.rstrip().lower()
    if prev=='the' and prev2=='in':
        denominators[0]+=1
        denominators[1]+=1
        if word=='past':
            numerators[0]+=1
        if word=='time':
            numerators[1]+=1
    if prev=='jury' and prev2=='the':
        denominators[2]+=1
        denominators[3]+=1
        if word=='said':
            numerators[2]+=1
        if word=='recommended':
            numerators[3]+=1
    if prev=='said' and prev2=='jury':
        denominators[4]+=1
        if word=='that':
            numerators[4]+=1
    if prev=='teacher' and prev2=='agriculture':
        denominators[5]+=1
        if word==',':
            numerators[5]+=1
    prev2=prev
    prev=word

#print(numerators)
#print(denominators)
            
probs=[0.]*6
for i in range(len(probs)):
    probs[i]=numerators[i]/denominators[i]
    
print('Unsmoothed probabilities:')
print(probs)

print()
for i in range(len(probs)):
    probs[i]=(numerators[i]+.1)/(denominators[i]+.1*len(word_index_dict))

print('Smoothed probabilities:')
print(probs)