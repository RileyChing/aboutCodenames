import spacy
nlp = spacy.load('en_core_web_lg')

from scipy.spatial.distance import cosine
import numpy as np
import random

f = open('./wordlistmini','r')

transform = random.randint(1,5)

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
a_list = []
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
    if num != i:
        sim = vector_similarity(nlp.vocab[a1].vector, nlp.vocab[word_list[i]].vector)

        if sim >= 0.45:
            arr1.append(word_list[i])
        else:
            arr2.append(word_list[i])
a_list.append(a1)
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
a_list.append(a2)
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
a_list.append(a3)
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
a_list.append(a4)
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
a_list.append(a5)
print(a1,a2,a3,a4,a5)
#----------------最简单的情况----------------------
b_easy = random.sample(arr_far, 4)
print('最简单的情况:')
for i in b_easy:
    print(i, end=' ')
print("   ")

#----------------最困难的情况----------------------
b_hard = random.sample(arr_near, 4)
print('困难的情况:')
for i in b_hard:
    print(i, end=' ')
print("   ")

#----------------中等难度的情况----------------------
print('中等难度情况1:')
b1 = random.choice(arr_near)
print(b1, end=' ')
b2_4 = random.sample(arr_far, 3)
for i in b2_4:
    print(i, end=' ')
print("   ")

print('中等难度情况2:')
b1_b2 = random.sample(arr_near, 2)
for i in b1_b2:
    print(i, end=' ')
b3_b4 = random.sample(arr_far, 2)
for i in b3_b4:
    print(i, end=' ')
print("   ")

print('中等难度情况3:')
b1_b3 = random.sample(arr_near, 3)
for i in b1_b3:
    print(i, end=' ')
b4 = random.choice(arr_far)
print(b4)
print("   ")
print("first time:")
print(transform)

# print(a1)
# print(a2)
# print(a3)
# print(a4)
# print(a5)
# print("........")
# print(b_easy)
transform1 = 1
if transform == 3:
    if vector_similarity(nlp.vocab[a_list[3]].vector, nlp.vocab[a_list[4]].vector) > 0.45:
        transform1 = transform1 + 1
elif transform == 5:
    transform1 = 0
elif transform < 3 :
    for i in range(transform, len(a_list)):
        for j in range(transform, len(a_list)):
            if i < j and vector_similarity(nlp.vocab[a_list[i]].vector, nlp.vocab[a_list[j]].vector) > 0.45 :
                transform1 = transform1 + 1

print("second time:")
print(transform1)









