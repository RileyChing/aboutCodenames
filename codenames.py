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



# print("Most common:",model.index2word[:50])
# print("Least common:",model.index2word[-50:])



# Here's an example Codenames board.  `blue` is one team's words, `red` the other and `assassin` is the assassin word.

f = open('./wordlistmini','r')

# transform = random.randint(1,5)
print("请输入棋盘难易度1-5:")
transform = input()

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

num = random.choice(range(0, len(word_list)))
a1 = word_list[num]

arr1 = []   #与a1含义相近
arr2 = []   #与a1含义不相近


for i in range(0, len(word_list)):
    if num!=i:
        sim = vector_similarity(nlp.vocab[a1].vector, nlp.vocab[word_list[i]].vector)

        if sim >= 0.45:
            arr1.append(word_list[i])
        else:
            arr2.append(word_list[i])
#--------------a2------------------------
if transform == 1:
    a2 = random.choice(arr2)
else:
    a2 = random.choice(arr1)

arr3 = []   #与a1和a2含义都不相近
arr3_1 = [] #与a1和a2含义都相近

for i in range(0, len(arr2)):
    sim = vector_similarity(nlp.vocab[a2].vector, nlp.vocab[arr2[i]].vector)
    if sim < 0.45:
        arr3.append(arr2[i])
    else:
        arr3_1.append(arr2[i])

arr3_1 = arr3_1 + arr1
arr3_1.remove(a2)

#--------------a3------------------------
if transform == 1 or transform == 2:
    a3 = random.choice(arr3)
else:
    a3 = random.choice(arr3_1)

arr4 = []   #与a1和a2和a3含义都不相近
arr4_1 = [] #与a1和a2和a3含义都相近

for i in range(0, len(arr3)):
    sim = vector_similarity(nlp.vocab[a3].vector, nlp.vocab[arr3[i]].vector)
    if sim < 0.45:
        arr4.append(arr3[i])
    else:
        arr4_1.append(arr3[i])

arr4_1 = arr4_1 + arr3_1
arr4_1.remove(a3)

#--------------a4------------------------
if transform == 4 or transform == 5:
    a4 = random.choice(arr4_1)
else:
    a4 = random.choice(arr4)

arr5 = []   #与a1、a2、a3、a4含义都不相近
arr5_1 = [] #与a1、a2、a3、a4含义都相近

for i in range(0, len(arr4)):
    sim = vector_similarity(nlp.vocab[a4].vector, nlp.vocab[arr4[i]].vector)
    if sim < 0.45:
        arr5.append(arr4[i])
    else:
        arr5_1.append(arr4[i])

arr5_1 = arr5_1 + arr4_1
arr5_1.remove(a4)

#--------------a5------------------------
if transform == 5:
    a5 = random.choice(arr5_1)
else:
    a5 = random.choice(arr5)

arr_far = []    #与a1、a2、a3、a4、a5含义都不相近
arr_near = []   #与a1、a2、a3、a4、a5含义都相近

for i in range(0, len(arr5)):
    sim = vector_similarity(nlp.vocab[a5].vector, nlp.vocab[arr5[i]].vector)
    if sim < 0.45:
        arr_far.append(arr5[i])
    else:
        arr_near.append(arr5[i])

arr_near = arr_near + arr5_1
arr_near.remove(a5)

# print(a1, a2, a3, a4, a5)
blue = [a1, a2, a3, a4, a5]
# print(blue)

b1, b2, b3, b4 = random.sample(arr_far, 4)
#----------------最简单的情况----------------------
if transform == 1 :
    b1, b2, b3, b4 = random.sample(arr_far, 4)
    # print('最简单的情况:')
    '''
    for i in b1, b2, b3, b4:
        print(i, end=' ')
    print("   ")
    '''

#----------------最困难的情况----------------------
if transform == 5 :
    b1, b2, b3, b4 = random.sample(arr_near, 4)
    # print('困难的情况:')

#----------------中等难度的情况----------------------
if transform == 2 :
    # print('中等难度情况1:')
    b1 = random.choice(arr_near)

    b2, b3, b4 = random.sample(arr_far, 3)

if transform == 3 :
    # print('中等难度情况2:')
    b1, b2 = random.sample(arr_near, 2)

    b3, b4 = random.sample(arr_far, 2)

if transform == 4 :
    # print('中等难度情况3:')
    b1, b2, b3 = random.sample(arr_near, 3)

    b4 = random.choice(arr_far)

    #print("   ")
    # print(transform)

red = [b1, b2, b3, b4]
# print(red)
words = blue + red
# print(words)
random.shuffle(words)
# print(words)

board = {
    'blue': [a1, a2, a3, a4, a5],
    'red': [b1, b2, b3, b4],
}
# print(board)
'''
blue0 = []
for k in board:
    blue0.append((board[k]))

board_ran = random.shuffle(blue0)
print(board_ran)
'''
# print(board['blue'][0])

point_b = 0
point_r = 0

print("--------GAME START--------")

print("WORDS:")
for i, j in enumerate(words):
    print(j, end=" ")
print()

while len(board['blue']) != 1 and len(board['red']) != 0 :

    # -------------blue---------------
    # dict = corpora.Dictionary([board['blue']])
    # print(dict)
    # We can use gensim to find the 10 words most related to the word in this word2vec model.

    print("CLUE FOR BLUE：")

    clue = model.most_similar(
        positive=board['blue'],
        negative=board['red'],
        restrict_vocab=50000
    )
    # 设置clue 待优化
    clue_b = ' '
    for i, j in clue:
        clue_b = i
        break

    sum = 0

    for i in range(len(blue)):

        sim = vector_similarity(nlp.vocab[clue_b].vector, nlp.vocab[blue[i]].vector)
        if sim > 0.25:
            sum += 1

    print(clue_b, sum)

    num = 0

    while True:

        print("ENTER THE ANSWER FOR BLUE")

        ans = input()

        if ans in blue:

            print("CORRECT")
            num += 1
            point_b += 1

            words.remove(ans)
            blue.remove(ans)
            board['blue'].remove(ans)

            print("WORDS:")
            for i, j in enumerate(words):
                print(j, end=" ")
            print()

            if num == sum + 1:
                break

        elif ans in red:
            print("WRONG")
            words.remove(ans)
            red.remove(ans)
            board['red'].remove(ans)
            break

        else:
            print("TRY AGAIN")
            continue
    # -------------red---------------
    # dict = corpora.Dictionary([board['blue']])
    # print(dict)
    # We can use gensim to find the 10 words most related to the word in this word2vec model.

    print("WORDS:")
    for i, j in enumerate(words):
        print(j, end=" ")
    print()
    print("CLUE FOR RED：")

    clue = model.most_similar(
        positive=board['red'],
        negative=board['blue'],
        restrict_vocab=50000
    )

    # 设置clue 待优化
    clue_r = ' '
    for i, j in clue:
        clue_r = i
        break
    sum = 0

    for i in range(len(red)):

        sim = vector_similarity(nlp.vocab[clue_r].vector, nlp.vocab[red[i]].vector)
        if sim > 0.25:
            sum += 1

    print(clue_r, sum)

    num = 0

    while True:

        print("ENTER THE ANSWER FOR BLUE")

        ans = input()

        if ans in red:
            print("CORRECT")
            num += 1
            point_b += 1
            words.remove(ans)
            red.remove(ans)
            board['red'].remove(ans)

            print("WORDS:")
            for i, j in enumerate(words):
                print(j, end=" ")
            print()
            if num == sum + 1:
                break
        elif ans in blue:
            print("WRONG")
            words.remove(ans)
            blue.remove(ans)
            board['blue'].remove(ans)
            break
        else:
            print("TRY AGAIN")
            continue

if point_b > point_r :
    print("BLUE WIN!")

elif point_r > point_b :
    print("RED WIN!")

elif point_b == point_r :
    print("DRAW")
