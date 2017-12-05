import nltk.data
#nltk.download()

from googletrans import Translator
translator = Translator()

tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')

    
fname = "the_story_of_the_baked_head"
fin = open(fname + r".txt", 'r')
fout = open(fname + r".tex", "w")

for token in tokenizer.tokenize(fin.read()):
    if len(token) < 3:
        continue
    nl = translator.translate(token, src="en", dest="nl")
    res = "{}&\n{}&\n\\\\\n".format(nl.text, token)
    fout.write(res)

