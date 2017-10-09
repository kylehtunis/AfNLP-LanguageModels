#answer to question on the bottom

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

#print(counts[word_index_dict['all']][word_index_dict['the']])
#print(counts[word_index_dict['the']][word_index_dict['jury']])

counts+=.1
#TODO: normalize counts
probs=normalize(counts, norm='l1', axis=1)
#print(probs.tolist())
#g=GENERATE(word_index_dict, probs, 'bigram', 10, '<s>')
#print(g)

#TODO: writeout bigram probabilities
wf=open('smooth_probs.txt','w+')

wf.write('p(the | all) = '+str(probs[word_index_dict['all']][word_index_dict['the']])+'\n')
wf.write('p(jury | the) = '+str(probs[word_index_dict['the']][word_index_dict['jury']])+'\n')
wf.write('p(campaign | the) = '+str(probs[word_index_dict['the']][word_index_dict['campaign']])+'\n')
wf.write('p(calls | anonymous) = '+str(probs[word_index_dict['anonymous']][word_index_dict['calls']])+'\n')
        
wf.close()


f.close()


#Answer to question: the probabilities drop much less for the bigrams conditioned on 'the'
#because the counts are much higher, so the extra .1*n added to the denominator is not as significant
#as for bigrams with lower counts