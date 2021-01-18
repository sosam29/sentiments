from string import digits, punctuation
import nltk

def cleanfile(src, dest):
    with open(src,"r") as f:
        data=f.read().replace('\n','')
        remove_punctuation=str.maketrans('','', punctuation)
        remove_digit=str.maketrans('','',digits)
        remove_punctuation=str.maketrans('','', punctuation)
        res= data.translate(remove_digit)
        res2= res.translate(remove_punctuation)
        n=open(dest,"w")
        n2=n.write(res2)
        n.close()


cleanfile('romans', 'romans2')
cleanfile('hebrew', 'hebrew2')
