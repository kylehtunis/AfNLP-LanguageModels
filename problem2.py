import codecs
import numpy as np
from generate import GENERATE


vocab = codecs.open("brown_vocab_100.txt", "r", encoding="utf-16")

#load the indices dictionary
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

counts = np.ndarray((len(word_index_dict)))
counts[:]=0

#TODO: iterate through file and update counts
corpus=f.read().split()
#print(corpus)
for word in corpus:
    word=word.rstrip().lower()
    counts[word_index_dict[word]]+=1

f.close()

#TODO: normalize and writeout counts. 
probs=counts/np.sum(counts)
#print(counts)
#print(probs)
wf=open('unigram_probs.txt','w+')
wf.write(str(probs.tolist()))
wf.close()


