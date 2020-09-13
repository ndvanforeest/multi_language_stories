#!/usr/bin/env python3 
"""This script translates a dutch source text to English and French.

en: English
nl: Dutch
fr: Spanish

First activate the virtualenv. This contains the modules for google
translate. Then run:

> python this_file.py deur.txt

"""

import re
from googletrans import Translator
import click


translator = Translator()

#translations = translator.translate(['The quick brown fox', 'jumps over', 'the lazy dog'], dest='ko')

def clean_up(array):
    res = []
    for r in array:
        if len(r) == 0:
            continue
        target = re.sub(r' ​​', " ", r)
        target = re.sub(r'([\.\?\!,]) "', r"\1'", target)
        target = re.sub(r'"(\w)', r"`\1", target)
        target = re.sub(r"'(\w)", r"`\1", target)
        target = re.sub(r'([\.\?\!,])"', r"\1'", target)
        target = re.sub(r"([\.\?\!,]) '", r"\1'", target)
        #target = re.sub(r"'(\w)", r"`\1", target)
        res.append(target)
    return res


@click.command()
@click.argument('fin')
#@click.argument('target_language')
def translate_single_file(fin):
    with open(fin, "r") as fp:
        res = [l.strip() for l in fp]

    english = clean_up([l.text for l in translator.translate(res, src="nl", dest='en')])
    french = clean_up([l.text for l in translator.translate(res, src="nl", dest='fr')])

    fout = fin + "_tr"
    with open(fout, "w") as fp:
        for n,e,f, in zip(res, english, french):
            fp.write(f"<nl>{n}\n")
            fp.write(f"<en>{e}\n")
            fp.write(f"<fr>{f}\n")
            fp.write("\n")



if __name__ == "__main__":
    translate_single_file()


