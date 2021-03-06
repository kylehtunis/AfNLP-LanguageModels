##answer to question on the bottom

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

#print(counts.tolist())

f.close()

#TODO: normalize and writeout counts. 
probs=counts/np.sum(counts)
#print(counts)
#print(probs)
wf=open('unigram_probs.txt','w+')
wf.write(str(probs.tolist()))
wf.close()

#part 6 code
f = codecs.open("toy_corpus.txt", encoding = "utf-16")
wf=open('unigram_eval.txt','w+')
sents=f.readlines()
for sent in sents:
    sent=sent.split()
    prob=1.
    for word in sent:
        word=word.rstrip().lower()
        prob*=probs[word_index_dict[word]]
    wf.write(str(prob)+'\n')
f.close()
wf.close()

f = codecs.open("toy_corpus.txt", encoding = "utf-16")
wf=open('unigram_eval.txt','w+')
sents=f.readlines()
for sent in sents:
    sent=sent.split()
    sent_len=len(sent)
    prob=1
    for word in sent:
        word=word.rstrip().lower()
        prob*=probs[word_index_dict[word]]
    perplexity = 1/(pow(prob, 1.0/sent_len))
    wf.write(str(perplexity)+'\n')
f.close()
wf.close()

##part 7 code
wf=open('unigram_generation.txt', 'w+')
for i in range(10):
    wf.write(GENERATE(word_index_dict, probs, 'unigram', 10, '<s>'))
    wf.write('\n')
wf.close()


#answer to question: roughly 2/3 of the words were only seen once. I would expect this 
#ratio to be lower in a larger corpus, since the vocabulary of any corpus tends to be much
#lower than the size