import nltk.data
#nltk.download()

from googletrans import Translator
translator = Translator()

tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')

is_src_dutch = False
    
fname="the_sleepy_teacher"
fin = open(fname + r".txt", 'r')
fout = open(fname + r".tex", "w")


for token in tokenizer.tokenize(fin.read()):
    if len(token) < 3:
        continue
    if is_src_dutch:
        res = translator.translate(token, src="nl", dest="en")
        res = "{}&\n{}&\n\\\\\n".format(token, res.text)
    else:
        res = translator.translate(token, src="en", dest="nl")
        res = "{}&\n{}&\n\\\\\n".format(res.text, token)
    fout.write(res)

