#!/usr/bin/env python
# coding: utf-8

# We'll use the python library gensim: https://radimrehurek.com/gensim/

import gensim

from gensim import corpora
import spacy
nlp = spacy.load('en_core_web_lg')

from scipy.spatial.distance import cosine
import numpy as np
import random

# Load a premade word2vec model built on Google News articles.
# 
# Download from: https://drive.google.com/file/d/0B7XkCwpI5KDYNlNUTTlSS21pQmM




model = gensim.models.KeyedVectors.load_word2vec_format('GoogleNews-vectors-negative300.bin', binary=True, limit=500000)


# We limit the vocabulary to the 500,000 most common words.  Even at 500,000, it starts to get to nonsense words.
# Here are the top 50 and bottom 50 words by frequency. And even for the real words that are infrequent, if a word is too obscure, it wouldn't make for a good clue.



print("Most common:",model.index2word[:50])
print("Least common:",model.index2word[-50:])


# Here's an example Codenames board.  `blue` is one team's words, `red` the other and `assassin` is the assassin word.

f = open('./wordlistmini','r')

transform = random.randint(1, 5)

lines1 = f.readlines()
matrix1 = []
for i in range(0, len(lines1)):
    matrix1.append(lines1[i])

f.close()

for i in range(0, len(matrix1)):
    matrix1[i] = matrix1[i].strip('\n')

text = " ".join(matrix1)
doc = nlp(text)

# embedding = []
word_list = []

for token in doc:
    word_list.append(token.text)

# for word in word_list:
#     embedding.append(nlp.vocab[word].vector)
#
# embedding = np.array(embedding)

def vector_similarity(x, y):
    np.seterr(invalid='ignore')

    return 1 - cosine(x, y)


blue = []
for i in range(0, 4):
    blue.append(i)

num = random.choice(range(0, len(word_list)))
blue[0] = word_list[num]

arr1 = []   #与a1含义相近
arr2 = []   #与a1含义不相近


for i in range(0, len(word_list)):
    if num!=i:
        sim = vector_similarity(nlp.vocab[blue[0]].vector, nlp.vocab[word_list[i]].vector)

        if sim >= 0.45:
            arr1.append(word_list[i])
        else:
            arr2.append(word_list[i])
#--------------a2------------------------
if transform == 1:
    blue[1] = random.choice(arr2)
else:
    blue[1] = random.choice(arr1)

arr3 = []   #与a1和a2含义都不相近
arr3_1 = [] #与a1和a2含义都相近

for i in range(0, len(arr2)):
    sim = vector_similarity(nlp.vocab[blue[1]].vector, nlp.vocab[arr2[i]].vector)
    if sim < 0.45:
        arr3.append(arr2[i])
    else:
        arr3_1.append(arr2[i])

arr3_1 = arr3_1 + arr1
arr3_1.remove(blue[1])

#--------------a3------------------------
if transform == 1 or transform == 2:
    blue[2] = random.choice(arr3)
else:
    blue[2] = random.choice(arr3_1)

arr4 = []   #与a1和a2和a3含义都不相近
arr4_1 = [] #与a1和a2和a3含义都相近

for i in range(0, len(arr3)):
    sim = vector_similarity(nlp.vocab[blue[2]].vector, nlp.vocab[arr3[i]].vector)
    if sim < 0.45:
        arr4.append(arr3[i])
    else:
        arr4_1.append(arr3[i])

arr4_1 = arr4_1 + arr3_1
arr4_1.remove(blue[2])

#--------------a4------------------------
if transform == 4 or transform == 5:
    blue[3] = random.choice(arr4_1)
else:
    blue[3] = random.choice(arr4)

arr5 = []   #与a1、a2、a3、a4含义都不相近
arr5_1 = [] #与a1、a2、a3、a4含义都相近

for i in range(0, len(arr4)):
    sim = vector_similarity(nlp.vocab[blue[3]].vector, nlp.vocab[arr4[i]].vector)
    if sim < 0.45:
        arr5.append(arr4[i])
    else:
        arr5_1.append(arr4[i])

arr5_1 = arr5_1 + arr4_1
arr5_1.remove(blue[3])

#--------------a5------------------------
if transform == 5:
    blue[4] = random.choice(arr5_1)
else:
    blue[4] = random.choice(arr5)

arr_far = []    #与a1、a2、a3、a4、a5含义都不相近
arr_near = []   #与a1、a2、a3、a4、a5含义都相近

for i in range(0, len(arr5)):
    sim = vector_similarity(nlp.vocab[blue[4]].vector, nlp.vocab[arr5[i]].vector)
    if sim < 0.45:
        arr_far.append(arr5[i])
    else:
        arr_near.append(arr5[i])

arr_near = arr_near + arr5_1
arr_near.remove(blue[4])

print(blue)

for i in range(0, 4):
    blue.append()

board = {
    'blue': ['ambulance', 'hospital', 'spell', 'lock', 'charge', 'tail', 'link', 'cook', 'web'],
    'red': ['cat', 'button', 'pipe', 'pants', 'mount', 'sleep', 'stick', 'file', 'worm'],
    'assassin': 'doctor'
}

print(board['blue'][0])

dict = corpora.Dictionary([board['blue']])
print(dict)
# We can use gensim to find the 10 words most related to "ambulance" in this word2vec model.




# print(model.similar_by_word('ambulance', topn=10))


# Each line is the word, followed by how similar the word is to "ambulance." Some of these words word be useful, "parametics" for instance, but many are just other forms of the word "ambulance."
# 
# gensim allows us to directly find words the most similar to a whole group of words at one time.

# In[9]:


# model.most_similar(positive=board['blue'])


# As we can see, it produces a lot of nonsense words. We can use `restrict_vocab` to limit results to only the top n most common words in the corpus.



# gensim allows for negative examples to be included as well to help avoid that.

clue = model.most_similar(
    positive=board['blue'],
    negative=board['red'],
    restrict_vocab=50000
)

for i in range(0, 4):
    sum = 0
    sim = vector_similarity(nlp.vocab[clue0].vector, nlp.vocab[blue[i]].vector)
    if sim > 0.4:
        num += 1

print(clue0, sum)
