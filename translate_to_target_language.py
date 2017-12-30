#!/usr/bin/env python3 
"""
This script translates an english source text to a target language and turns it into an easy to correct latex file.

en: English
tr: Turkish
nl: Dutch
es: Spanish

first activate the virtualenv. This contains the modules for google translate.

"""

import re
from googletrans import Translator
translator = Translator()

spanish = [
    "flying",
    "swimming",
    "traffic",
]

turkish = [
    "hercules"
]

# first format the english file with format_single_file.py.

dutch = [
    "the_emperors_new_clothes"
    #"aladdin_2"
    #"ali_baba_2",
    #"jack_beanstalk",
    ]


target_language, files ="nl", dutch
#target_language, files ="es", spanish
#target_language, files ="tr", turkish

def translate_single_file(fin):
    res = []
    for line in fin:
        if line[:4] != "<en>":
            continue
        #source = re.sub(r'&', "", line[4:])
        source = line[4:]
        target = translator.translate(source, src="en", dest=target_language).text
        # google translate sometimes adds weird characters to the
        # target translation. The line below removes such weird
        # characters.
        target = re.sub(r' ​​', " ", target)
        target = re.sub(r"(\. ')", '."', target)
        target = re.sub(r'(\. ")', '."', target)
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

latex_footer = r"""
\end{document}
"""

def latex_alternating(story, fout):
    fout.write(latex_header)
    for line in story:
        #fout.write("\\begin{samepage}\n\\noindent\n")
        fout.write("\\vbox{\n\\noindent\n")
        fout.write("{} \\newline\n{}".format(line[0].strip(), line[1]))
        #fout.write("\n\\end{samepage}\n\\vspace{3mm}\n\n")
        fout.write("\n}\n\\vspace{3mm}\n\n")
    fout.write(latex_footer)


def translate_files():
    for fname in files:
        fin_name = r"source_files/" + fname + ".tex"
        fout_name = target_language +"_" + fname + ".tex"
        with open(fin_name, "r") as fin:
            story = translate_single_file(fin)
        with open(fout_name, "w") as fout:
            latex_alternating(story, fout)

if __name__ == "__main__":
    translate_files()

    
