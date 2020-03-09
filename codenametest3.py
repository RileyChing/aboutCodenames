import random

# from random import randint
# import numpy
import gensim.models.word2vec as word2vec
import gensim
import logging


# word2vec Text8 的训练
def train_save_model():
    # logging.basicConfig(format='%(asctime)s : %(levelname)s :%(message)',level=logging.INFO)
    # 加载预料
    sentences = word2vec.Text8Corpus('/Users/apple/PycharmProjects/text8')
    model = word2vec.Word2Vec(sentences, size=200)
    model.save('/Users/apple/PycharmProjects/text.model')
# 加载模型
def load_model():
    model = word2vec.Word2Vec.load('/Users/apple/PycharmProjects/text.model')
    #simi = model.similar_by_vector('women', 'men')
    #print(simi)
    simi = model.most_similar(positive=['woman', 'king'], negative=['man'])
    #print(simi)
    return simi
    #print(model['red'])

# 执行代码
#train_save_model()
#load_model()
def play_spymaster():
    """
           Play a complete game, with the robot being the spymaster.
           """
    """
    words = random.sample(self.codenames, self.cnt_rows * self.cnt_cols)
    my_words = set(random.sample(words, self.cnt_agents))
    used_clues = set(my_words)
    """
    print_words()  # 打印5*5
    while True:
        clue = load_model()
        print("clue:",clue)
        print("your guess:")
        break
            #print('Clue: "{} {}" (certainty {:.2f}, remaining words {})'
            # .format(clue, len(group), score, len(my_words)))
        print()
        # 被猜过的词划掉
        """
            for pick in reader.read_picks(words, my_words, len(group)):
                words[words.index(pick)] = "---"
                if pick in my_words:
                    my_words.remove(pick)
        """
def play_agent():
        """
        Play a complete game, with the robot being the agent.
        """
        print_words()
        """while any(w not in picked for w in my_words):
            reader.print_words(
                [w if w not in picked else "---" for w in words], nrows=self.cnt_rows
            )
            print("Your words:", ", ".join(w for w in my_words if w not in picked))
            clue, cnt = reader.read_clue(self.word_to_index.keys())
            for _ in range(cnt):
                guess = self.most_similar_to_given(
                    clue, [w for w in words if w not in picked]
                )
                picked.append(guess)
                answer = input("I guess {}? [Y/n]: ".format(guess))
                if answer == "n":
                    cnt = cnt-1 # 机会减少
                    print("Sorry about that.")
                    break
            else:
                print("I got them all!")
"""
def print_words():
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

    # print("matrix---", matrix)

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

def main():


    while True:
        try:
            mode = input("\nWill you be agent or spymaster?: ")
        except KeyboardInterrupt:
            print("\nGoodbye!")
            break
        try:
            if mode == "spymaster":
                play_agent()
            elif mode == "agent":
                play_spymaster()
        except KeyboardInterrupt:
            # Catch interrupts from play functions
            # 从游戏功能捕获中断
            pass


main()