"""
This script translated english texts, in a txt file, to a dutch and turkish version.
"""

import nltk.data
#nltk.download()

from googletrans import Translator
translator = Translator()

tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')

is_src_dutch = False


files = [
    "the_song_of_the_armadillo.txt",
    ]


def translate_single_file(fname):
    fin = open(fname + r".txt", 'r')
    fout = open(fname + r".tex", "w")
    for token in tokenizer.tokenize(fin.read()):
        if len(token) < 3:
            continue
        if is_src_dutch:
            nl = token
            en = translator.translate(token, src="nl", dest="en").text
        else:
            en = token
            nl = translator.translate(token, src="en", dest="nl").text
        tr = translator.translate(token, src="en", dest="tr").text
        res = "{}&\n{}&\n{}\\\\\n".format(nl, en, tr)
        fout.write(res)

for fname in files:
    translate_single_file(fname)
