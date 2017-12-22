"""
This script splits an english text into single sentences. These sentences have to be improved by hand. such that the final latex output becomes nice. .

Include the txt file, without its ".txt" extension. Then move the translated tex file to the source_files. 
"""

import nltk.data
#nltk.download()

from googletrans import Translator
translator = Translator()

tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')

is_src_dutch = False


files = [
    #"jack_beanstalk"
    #"the_pink_fairy_book",
    #"arabian_nights"
    "the_traveling_musicians"
    ]


def format_single_file(fname):
    fin = open(fname + r".txt", 'r')
    fout = open(fname + r".tex", "w")
    for token in tokenizer.tokenize(fin.read()):
        if len(token) < 2:
            continue
        res = "<en> {}&\n\\\\\n".format(token)
        fout.write(res)

for fname in files:
    format_single_file(fname)
