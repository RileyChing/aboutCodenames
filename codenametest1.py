from gensim.models import word2vec
import gensim
sentences = word2vec.Text8Corpus("/Users/apple/PycharmProjects/helloworld/wordlistmini")
#model = Word2Vec(sentences, sg=1, size=100,  window=5,  min_count=5,  negative=3, sample=0.001, hs=1, workers=4)
model=gensim.models.Word2Vec(sentences,sg=1,size=100,window=5,min_count=1,negative=3,sample=0.001,hs=1,workers=4)

# min_count，是去除小于min_count的单词
# size，神经网络层数
# sg， 算法选择
# window， 句子中当前词与目标词之间的最大距离
# workers，线程数

model.save("/Users/apple/PycharmProjects/helloworld/wordlistmini2")	#模型会保存到该 .py文件同级目录下，该模型打开为乱码
#model.wv.save_word2vec_format("文件名"，binary = "Ture/False")
# 通过该方式保存的模型，能通过文本格式打开，也能通过设置binary是否保存为二进制文件。
# 但该模型在保存时丢弃了树的保存形式（详情参加word2vec构建过程，以类似哈夫曼树的形式保存词），
# 所以在后续不能对模型进行追加训练

#对.sava保存的模型的加载：
model = gensim.models.Word2Vec.load("/Users/apple/PycharmProjects/helloworld/wordlistmini2")

#对..wv.save_word2vec_format保存的模型的加载：
#model = model.wv.load_word2vec_format('模型文件名')

#model.train(more_sentences)

#如果对..wv.save_word2vec_format加载的模型进行追加训练，会报错：
#AttributeError: 'Word2VecKeyedVectors' object has no attribute 'train'


x = model.most_similar(positive=['Woman', 'King'], negative=['Man'])

print(x)
y = model.similarity('Woman', 'Man')

print(y)
