#!/usr/bin/python3
import os
import re

import config

def read_story_and_vocab(lang, fname):
    lang_string = "<{}>".format(lang)
    with open(r"source_files/{}".format(fname)) as fp:
        story = []
        for line in fp:
            if line[:-1] == config.vocabulary[lang]:
                break
            if line[:4] == lang_string:
                story.append(line[4:].strip())
        words = []
        for line in fp:
            if line[:4] == lang_string:
                words.append(line[4:].strip())
    return story, words
    

def select_story_and_vocab(lang_left, lang_right, fname):
    story_left, words_left = read_story_and_vocab(lang_left, fname)
    story_right, words_right = read_story_and_vocab(lang_right, fname)

    if len(story_left)==0 or len(story_right)==0:
        # the left or right language story is not in the file
        return None, None

    if len(story_left) != len(story_right):
        print("left and right stories are not of the same length")
        quit()

    if len(words_left) != len(words_right):
        print("left and right word lists are not of the same length")
        print(words_left)
        print(words_right)
        quit()

    story = [[l, r] for l, r in zip(story_left, story_right)]
    words = [[l, r] for l, r in zip(words_left, words_right)]
    return story, words

def section_title(t1, t2):
    if "footnote" in t1:
        t1 = re.sub(r'\\footnote{.*}', "", t1)
    if "footnote" in t2:
        t2 = re.sub(r'\\footnote{.*}', "", t2)
    include_print_section_numbers = False
    if include_print_section_numbers:
        res = "\section{{ {} / {} }}".format(t1, t2)
    else:
        res = "\section*{{{}}}".format(t1)
        res += r"\addcontentsline{toc}{section}{\protect\numberline{}" + t1 + "}"
    return res
    
        
def latex_parallel(story, words):
    # latex output for translation next to each other

    #table_format = "\\begin{longtable}{L||R}\\toprule"
    table_format = "\\begin{longtable}{L||L}\\toprule"
    res = [] # list of latex strings
    #print(story)
    title = section_title(story[0][0],story[0][1])
    res.append(title)
    # start story table 
    table_format = "\\begin{longtable}{L||L}\\toprule"
    res.append(table_format)
    # header of table
    res.append("{} & {} \\\\ \midrule".format(story[0][0], story[0][1]))
    # story itself
    for line in story[1:]:
        res.append("{} & {} \\\\".format(line[0], line[1]))
    # trailer
    res.append("\\bottomrule \\end{longtable}")

    if words:
        res.append(table_format)
    for line in words:
        res.append("{} & {} \\\\".format(line[0], line[1]))
    if words:
        res.append("\\bottomrule \\end{longtable}")
    
    res.append("\\clearpage")
    return "\n".join(res)


doc_template2 = r"""
\documentclass[12pt]{{article}}
\usepackage{{ctable}} % for toprule
\usepackage{{a4wide}}
\usepackage[T1]{{fontenc}}
\usepackage[utf8]{{inputenc}}
\usepackage{{fouriernc}}
\usepackage{{longtable}}
\usepackage{{marginnote}}
\usepackage{{manfnt}}
\usepackage{{url}}

\newcommand{{\oak}}[1]{{{{\leavevmode\color{{red}}#1}}\marginnote{{\dbend}}}}
\newcommand{{\nvf}}[1]{{{{\leavevmode\color{{red}}#1}}\marginnote{{\dbend}}}}
\newcolumntype{{L}}{{>{{\raggedright\arraybackslash}}p{{8cm}}}}
\newcolumntype{{R}}{{>{{\raggedleft\arraybackslash}}p{{8cm}}}}

\author{{en-nl: Nicky van Foreest\\
en-tr: Onur Kilic\\
en-es: Cesar Sala
}}
\title{{Parallel translations ({}-{}) }}

\begin{{document}}
\maketitle

\tableofcontents
\clearpage

\clearpage

{}

\end{{document}}
"""
#\input{{introduction}}


doc_template = r"""
\documentclass[a5paper]{{article}}
\usepackage[margin=5mm]{{geometry}}
\usepackage[T1]{{fontenc}}
\usepackage{{ctable}} % for toprule
\usepackage[utf8]{{inputenc}}
\usepackage{{tgheros}}
\usepackage{{longtable}}
\usepackage{{url}}
\usepackage{{multicol}}

\newcommand{{\oak}}[1]{{{{\leavevmode\color{{red}}#1}}\marginnote{{\dbend}}}}
\newcommand{{\nvf}}[1]{{{{\leavevmode\color{{red}}#1}}\marginnote{{\dbend}}}}
\newcolumntype{{L}}{{>{{\raggedright\arraybackslash}}p{{6.5cm}}}}

\author{{en-nl: Nicky van Foreest\\
en-tr: Onur Kilic\\
en-es: Cesar Sala
}}
\title{{Parallel translations ({}-{}) }}

\begin{{document}}
\maketitle

\begin{{multicols}}{{2}}
  \tableofcontents
\end{{multicols}}

\clearpage

{}

\end{{document}}
"""


def make_all_doc(lang_left, lang_right, latex_file):
    res = []
    for fname in config.files:
        if not os.path.isfile("./source_files/"+fname):
            continue
        story, words = select_story_and_vocab(lang_left, lang_right, fname)
        if story is None:
            continue
        res.append(latex_parallel(story, words))
    res = doc_template.format(lang_left, lang_right, "\n".join(res))
    with open(latex_file+".tex", "w") as fp:
        fp.write(res)
    try:
        # quit if an error occurs, rather than trying to pdflatex the
        # file a few times.
        os.system("pdflatex {}.tex".format(latex_file))
    except:
        quit()
    os.system("pdflatex {}.tex".format(latex_file))
    #os.system("pdflatex {}.tex".format(latex_file))
    os.system("rm {}.aux".format(latex_file))
    os.system("rm {}.log".format(latex_file))
    os.system("rm {}.tex".format(latex_file))
    os.system("rm {}.toc".format(latex_file))

if __name__ == "__main__":
    make_all_doc("tr", "en", "turkish_english")
    make_all_doc("nl", "en", "dutch_english")
    #make_all_doc("en", "nl", "english_dutch")
    make_all_doc("es","en", "spanish_english")
