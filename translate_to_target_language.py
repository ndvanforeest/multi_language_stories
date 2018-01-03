#!/usr/bin/env python3 
"""This script translates an english source text to a target language and
turns it into an easy to correct latex file.

en: English
tr: Turkish
nl: Dutch
es: Spanish

First activate the virtualenv. This contains the modules for google
translate.

"""

import re
from googletrans import Translator
translator = Translator()

spanish = [
    "flying",
    "swimming",
    "traffic",
]

target_language, fname = "nl", "the_story_of_greek_king"
#target_language, fname = "es", "flying"
#target_language, fname = "tr", "shaving"


def translate_single_file(fin):
    res = []
    for line in fin:
        if line[:4] != "<en>":
            continue
        source = line[4:]
        target = translator.translate(source, src="en", dest=target_language).text
        # google translate sometimes adds weird characters to the
        # target translation. The line below removes such weird
        # characters.
        target = re.sub(r' ​​', " ", target)
        target = re.sub(r"([\.\?\!,]) '", r"\1'", target)
        target = re.sub(r"'(\w)", r"`\1", target)
        res.append([source, target])
    return res


latex_header = r"""
\documentclass[11pt]{article}
\usepackage{a4wide}
\usepackage[T1]{fontenc}
\usepackage[utf8]{inputenc}
\usepackage{fouriernc}

\begin{document}
\clearpage
"""

latex_trailer = r"""
\end{document}
"""


def latex_alternating(story, fout):
    fout.write(latex_header)
    for line in story:
        # fout.write("\\begin{samepage}\n\\noindent\n")
        fout.write("\\vbox{\n\\noindent\n")
        fout.write("{} \\newline\n{}".format(line[0].strip(), line[1]))
        # fout.write("\n\\end{samepage}\n\\vspace{3mm}\n\n")
        fout.write("\n}\n\\vspace{3mm}\n\n")
    fout.write(latex_trailer)


def translate_file():
    #fin_name = r"source_files/" + fname + ".txt"
    fin_name = fname + ".txt"
    fout_name = target_language + "_" + fname + ".tex"
    with open(fin_name, "r") as fin:
        story = translate_single_file(fin)
    with open(fout_name, "w") as fout:
        latex_alternating(story, fout)


if __name__ == "__main__":
    translate_file()

    
