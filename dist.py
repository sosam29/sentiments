from nltk.tokenize import sent_tokenize, word_tokenize
from nltk import FreqDist
from nltk.corpus import stopwords

with open('../romans2','r') as file:
    data=file.read()
    stop_words= set(stopwords.words('english'))
    filtered_sentence=[w for w in data if not w in stop_words]

    freqdist= FreqDist(filtered_sentence)
    print(type(freqdist))
    words= freqdist.keys()
    freqdist.plot(10)
    # tokenized_data=word_tokenize(data)
    # stop_words= set(stopwords.words('english'))
    # filtered_sentence=[w for w in tokenized_data if not w in stop_words]
   
    # frqdis1= FreqDist.plot(tokenized_data)
    # feqdis2= FreqDist.plot(filtered_sentence)
    # print(frqdis1)
    # print(frqdis2)
    #print(len(tokenized_data))
    #print(len(filtered_sentence))

    




