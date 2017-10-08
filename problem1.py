import codecs


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

# TODO: write word_index_dict to word_to_index_100.txt
wf=open('word_to_index_100.txt', 'w+')
wf.write(str(word_index_dict))
wf.close()
#
print(word_index_dict['all'])
print(word_index_dict['resolution'])
print(len(word_index_dict))
