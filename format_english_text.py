#!/usr/bin/env python3

"""
This script splits an english text into single sentences. These sentences have to be improved by hand. such that the final latex output becomes nice. .

Include the txt file, without its ".txt" extension. Then move the translated tex file to the source_files. 
"""

import os
import re

# The regular expressions below work better for my purposes than the nltk algorithms.
#import nltk.data
#from nltk.tokenize import sent_tokenize
#nltk.download()
#tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')

fname = "./raw_material/the_story_of_greek_king.txt"
#"aladdin_2"
#"jack_beanstalk"
#"the_pink_fairy_book",
#"arabian_nights"

def format_single_file_raw(fname):
    story = []
    with open(fname, 'r') as fin:
        for line in fin:
            story.append(line.strip())
    story = "\n".join(story)
    story = re.sub(r'(\n\n)', r'<par>', story)
    story = re.sub(r'(\n)', r' ', story)
    story = re.sub(r'<par>', r'\n\n', story)
    story = re.sub(r'([\?\!\.,])"', r"\1'", story)
    story = re.sub(r'"(\w)', r"`\1", story)
    story = re.sub(r'([\.;]) ', r"\1\n", story)
    story = re.sub(r' `', r"\n`", story)
    story = re.sub(r"' ", r"'\n", story)
    #story = re.sub(r'(; )', r';\n', story)
    #story = re.sub(r'(\. )', r'.\n', story)
    #story = re.sub(r'(\.")', r".'\n", story)
    #story = re.sub(r'(\?")', r"?'\n", story)
    #story = re.sub(r'(\? )', r'?\n', story)
    #story = re.sub(r'(\!")', r"!'\n", story)
    #story = re.sub(r'(\! )', r'!\n', story)
    #story = re.sub(r'(," )', r",'\n", story)
    #story = re.sub(r'(, ")', r',\n`', story)
    #story = re.sub(r'(: ")', r':\n`', story)
    story = re.sub(r'(\n )', r'\n', story)
    story = re.sub(r'(\n\n\n)', r'\n\n', story)


    res = story.split("\n")
    with open(fname[15:], "w") as fout:
        for line in res:
            fout.write("<en>{}\n".format(line))
    #for token in tokenizer.tokenize(fin.read()):
    #for token in sent_tokenize(fin.read()):
    #    res = "<en>{}\n".format(token)
    #    fout.write(res)


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

def format_single_file_sourcefile(fname):
    # make a latex file to read the file by itself as a pdf file. I
    # don't use this often.
    fin = open(fname + r".txt", 'r')
    fout = open(fname + r".tex", "w")
    fout.write(latex_header)
    for i, line in enumerate(fin):
        if line[:4] != "<en>":
            print(i, line)
            quit()
        fout.write("\\vbox{\n\\noindent\n")
        fout.write("{}".format(line[4:].strip()))
        #fout.write("}\\vspace{5mm}\n\n")
        fout.write("}\n")
    fout.write(latex_footer)
    fout.close()
    os.system("pdflatex {}.tex".format(fname))
    #os.system("pdflatex {}.tex".format(latex_file))
    os.system("rm {}.aux".format(fname))
    os.system("rm {}.log".format(fname))
    os.system("rm {}.tex".format(fname))



format_single_file_raw(fname)
#format_single_file_sourcefile(fname)
