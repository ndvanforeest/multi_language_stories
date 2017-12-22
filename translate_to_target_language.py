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


files = [
    "the_traveling_musicians"
    ]

target_language="nl"


def translate_single_file(fname):
    fin = open(r"source_files/" + fname +".tex", 'r')
    res = []
    for line in fin:
        if line[:4] != "<en>":
            continue
        source = re.sub(r'&', "", line[5:])
        #target = translator.translate(token, src="en", dest=target_language).text
        target = "jaap"
        res.append([source, target])
    return res


latex_header =
r"""
\documentclass[12pt]{{article}}
\usepackage{{a4wide}}
\usepackage[T1]{{fontenc}}
\usepackage[utf8]{{inputenc}}
\usepackage{{fouriernc}}
\usepackage{{longtable}}

\begin{{document}}

\tableofcontents
\clearpage

\clearpage
"""

latex_trailer =
r"""
\end{{document}}
"""


def latex_alternating(story, fout):
    # latex output for alternating translations 
    template = "\\noindent\n{}\\newline\n{}\n\\vspace{{1mm}}\n"
    for line in story:
        fout.write(template.format(line[0], line[1]))


def translate_files():
    for fname in files:
        story = translate_single_file(fname)
        fout_name = ""
        with open(fname + r"_tranlated.tex", "w") as fout:
            latex_alternating(story, fout)

if __name__ == "__main__":
    translate_files()
