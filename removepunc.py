from string import punctuation
from nltk.corpus import stopwords
from nltk import FreqDist
from matplotlib import pyplot as plt
from nltk.tokenize import word_tokenize
def freqdist(text, top=10):
    # test='This is the day that , the lord a has made and we will " an rejoice and be glad in it'
    stop_words= set(stopwords.words('english'))
    s= text.translate(str.maketrans('','', punctuation))
    word_tokens= word_tokenize(s)
    filtered=[w for w in word_tokens if not w in stop_words]
    freqdist= FreqDist(filtered)
    topmost=freqdist.most_common(top)
    # print(type(topmost[0]))
    plt.scatter(*zip(*topmost))
    plt.show()
    # x=topmost.keys()
    # y= topmost.values()
    # plt.plot(topmost)
# s= test.translate(str.maketrans('','', punctuation))
# print(filtered)

with open('../romans2','r') as f:
    data=f.read()
    freqdist(data,20)


with open('../hebrew2','r') as f:
    data=f.read()
    freqdist(data,20)
