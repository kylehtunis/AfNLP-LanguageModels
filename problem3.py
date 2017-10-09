import codecs
import numpy as np
from sklearn.preprocessing import normalize
from generate import GENERATE
import random


vocab = codecs.open("brown_vocab_100.txt", "r", encoding="utf-16")

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

f = codecs.open("brown_100.txt", encoding = "utf-16")


counts = np.ndarray((len(word_index_dict),len(word_index_dict)))
counts[:][:]=0


#TODO: iterate through file and update counts
sents=f.readlines()
for sent in sents:
    sent=sent.split()
#    print(sent)
    prev='<s>'
    for word in sent:
        word=word.rstrip().lower()
#        print(prev+' | '+word)
        counts[word_index_dict[prev],word_index_dict[word]]+=1
#        print(counts[word_index_dict[prev],word_index_dict[word]])
        prev=word

#TODO: normalize counts
probs=normalize(counts, norm='l1', axis=1)
#print(probs.tolist())
#g=GENERATE(word_index_dict, probs, 'bigram', 10, '<s>')
#print(g)

#TODO: writeout bigram probabilities
wf=open('bigram_probs.txt','w+')
for i in range(len(probs)):
    for j in range(len(probs[i])):
        if probs[i][j]==0.:
            continue
        out='p('+str(list(word_index_dict)[j])+' | '+str(list(word_index_dict)[i])+') = '+str(probs[i][j])+'\n'
        wf.write(out)
        
wf.close()


f.close()