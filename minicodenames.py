import random

# from random import randint
# import numpy


oldf = open('/Users/apple/PycharmProjects/helloworld/wordlistmini', 'r')
newf = open('/Users/apple/PycharmProjects/helloworld/wordlistmini1', 'w')
n = 0
resultList = random.sample(range(0, 673), 4)  # sample(x,y)函数的作用是从序列x中，随机选择y个不重复的元素。
print("resultList---", resultList)
lines = oldf.readlines()
matrix = []
for i in resultList:
    newf.write(lines[i])
    matrix.append(lines[i])

oldf.close()
newf.close()
print("..........")

for i in range(4):
    matrix[i] = matrix[i].strip('\n')

print("matrix---", matrix)

print("...................")
print()

longest = max(map(len, matrix))

for i in range(4):
    if i % 2 == 0:
        print()
    print(matrix[i].rjust(longest), end='   ')

print()
print()
# words.close()

print("...................")
