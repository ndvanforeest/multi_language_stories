#!/usr/bin/env python3

import re, os
from googletrans import Translator

translator = Translator()

def format_single_file_raw(filename):
    story = []
    with open(filename, 'r') as fin:
        for line in fin:
            story.append(line.strip())

    story = "\n".join(story)
    story = re.sub(r'(\n\n)', r'<par>', story)
    story = re.sub(r'(\n)', r' ', story)
    story = re.sub(r'<par>', r'\n\n', story)
    story = re.sub(r'\n(\n)+', r'\n\n', story)

    os.system("mv {} unformatted_{}".format(filename, filename))

    res = story.split("\n")
    with open(filename, "w") as fout:
        for line in res:
            fout.write("{}\n".format(line))


def translate(fname):
    res = []
    with open(fname, "r") as fp:
        for line in fp:
            source = line.strip()
            res.append("<fr>" + source)
            target = translator.translate(source, src="fr", dest="en").text
            target = re.sub(r' ​​', " ", target)
            res.append("<en>" + target)

    with open("source_files/"+fname, "w") as fp:
        fp.write("\n".join(res))


fname="histoire_gribouille.txt"

format_single_file_raw(fname)
translate(fname)

    
