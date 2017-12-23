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

#target_language="nl"
target_language="es"

files = [
    "airport"
    #"the_traveling_musicians"
    #"the_merchant_and_the_jinnie.tex",
    #"ali_baba_2.tex",
    #"jack_beanstalk.tex",
    #"elephant_and_friends.tex"
    #"the_traveling_musicians.tex",
    ]

def translate_single_file(fin):
    res = []
    for line in fin:
        if line[:4] != "<en>":
            continue
        source = re.sub(r'&', "", line[4:])
        target = translator.translate(source, src="en", dest=target_language).text
        # google translate sometimes adds weird characters to the
        # target translation. The line below removes such weird
        # characters.
        target = re.sub(r' ​​', " ", target)
        res.append([source, target])
    return res


latex_header = r"""
\documentclass[12pt]{article}
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
    
    #template = "\\begin{{samepage}}\\noindent\n{}\\newline\n{}\n\\end{{samepage}}\n\n\\vspace{{2mm}}\n"
    for line in story:
        fout.write("\\begin{samepage}\n\\noindent\n")
        fout.write("{} \\newline\n{}".format(line[0].strip(), line[1]))
        fout.write("\n\\end{samepage}\n\\vspace{2mm}\n\n")
        #fout.write(template.format(line[0], line[1]))
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
