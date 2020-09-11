#!/usr/bin/env python
# coding: utf-8

# We'll use the python library gensim: https://radimrehurek.com/gensim/





import gensim

from gensim import corpora

# Load a premade word2vec model built on Google News articles.
# 
# Download from: https://drive.google.com/file/d/0B7XkCwpI5KDYNlNUTTlSS21pQmM




model = gensim.models.KeyedVectors.load_word2vec_format('GoogleNews-vectors-negative300.bin', binary=True, limit=500000)


# We limit the vocabulary to the 500,000 most common words.  Even at 500,000, it starts to get to nonsense words.
# Here are the top 50 and bottom 50 words by frequency. And even for the real words that are infrequent, if a word is too obscure, it wouldn't make for a good clue.



print("Most common:",model.index2word[:50])
print("Least common:",model.index2word[-50:])


# Here's an example Codenames board.  `blue` is one team's words, `red` the other and `assassin` is the assassin word.




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

# In[10]:

'''
model.most_similar(
    positive=board['blue'],
    restrict_vocab=50000,
    topn=20
)

'''
# This looks much better, and produces some decent clues.  
# * "bed", "paramedics", "emergency" all relate to "ambulance" and "hospital." 
# * "jail" could relate to "lock" and "charge." 
# * "click" to "web" and "link."
# 
# But “bed” would also relate to the other team’s word “sleep”; and “click” with “button.” It would be bad to give clues which could point to the opponent’s cards. 
# 
# gensim allows for negative examples to be included as well to help avoid that.

# In[11]:


clue = model.most_similar(
    positive=board['blue'],
    negative=board['red'],
    restrict_vocab=50000
)


# I really like the clue "telemedicine." It's non-obvious, but relates to four words: "web," "link," "ambulance" and "hospital." This shows the potential for this method to produce novel clues.
# 
# Let's say that the clue were "telemedicine" and the four words were removed from the board, then the next team got a turn.  What might their clues be?

# In[12]:
'''

board = {
    'blue': ['spell', 'lock', 'charge', 'tail', 'link'],
    'red': ['cat', 'button', 'pipe', 'pants', 'mount', 'sleep', 'stick', 'file', 'worm'],
    'assassin': 'doctor'
}

model.most_similar(
    positive=board['red'],
    negative=board['blue'],
    restrict_vocab=50000
)
'''

# This appears much less successful.  The top words mostly just seem to relate to a singe word:
# * pillow -> sleep
# * bra -> pants
# * couch -> sleep? cat?

# In[6]:

'''
game = {
    'blue': ['Sitter', 'Aunt', 'Teenager', 'Protestant', 'Blacksmith'],
    'red': ['Ear', 'Rim', 'Sentence', 'Money',],
    'assassin': 'Doctor'
}


# In[7]:


model.similar_by_word('Sitter', topn=10)


# In[8]:


model.most_similar(positive=game['blue'])


# In[9]:


model.most_similar(
    positive=game['blue'],
    restrict_vocab=50000,
    topn=20
)


# In[10]:


model.most_similar(
    positive=game['blue'],
    negative=game['red'],
    restrict_vocab=50000
)


# In[ ]:




'''