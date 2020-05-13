import spacy
nlp = spacy.load('en_core_web_lg')

from scipy.spatial.distance import cosine
import numpy as np
import random

matrix1 = []
for i in range(0, len(matrix1)):
    matrix1[i] = matrix1[i].strip('\n')

#print("matrix---", matrix1[0])


embedding = np.array([])
word_list = []

text = " ".join(matrix1)
doc = nlp(text)

for token in doc:
    if not(token.is_punct) and not(token.text in word_list):
        word_list.append(token.text)


for word in word_list:
    embedding = np.append(embedding, nlp.vocab[word].vector)#.vocab[,.vector

#print(embedding[0])
embedding = embedding.reshape(len(word_list), -1)

#cosine_similarity = lambda x, y: 1 - spatial.distance.cosine(x, y)
def vector_similarity(x, y):
    np.seterr(invalid='ignore')

    return 1 - cosine(x, y)

num = 0
for i in range(0, len(matrix1)):
    for j in range(0, len(matrix1)):
        if i < j:
            sim = vector_similarity(embedding[i], embedding[j])
            if sim >= 0.45:
                num = num + 1

print(num)











