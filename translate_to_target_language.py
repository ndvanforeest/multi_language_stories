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
import click


translator = Translator()


def translate_single_file(fin, target_language):
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
        target = re.sub(r'([\.\?\!,]) "', r"\1'", target)
        target = re.sub(r'"(\w)', r"`\1", target)
        target = re.sub(r"'(\w)", r"`\1", target)
        target = re.sub(r'([\.\?\!,])"', r"\1'", target)
        target = re.sub(r"([\.\?\!,]) '", r"\1'", target)
        #target = re.sub(r"'(\w)", r"`\1", target)
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


@click.command()
@click.argument('filename')
@click.argument('target_language')
def translate_file(filename, target_language):
    """Translate filename in source_files to a target language.

    Example:

    ./translate_to_target_language.py source_files/second_calendar.txt nl 

    This generates second_calendar.tex in the directory in which
    ./translate_to_target_language.py is run.

    """

    fin_name = filename
    fout_name = target_language + "_" + filename[13:-4] + ".tex"
    with open(fin_name, "r") as fin:
        story = translate_single_file(fin, target_language)
    with open(fout_name, "w") as fout:
        latex_alternating(story, fout)


if __name__ == "__main__":
    translate_file()

    
