#!/usr/bin/python3
import os  
from enum import IntEnum


files = [
]

if len(files) == 0:
    files = [
        "fire.tex",
        "flying.tex",
        "everyday.tex",
        "traffic.tex",
        "airport.tex",
        "swimming.tex",
        "my_daily_pattern.tex",
        "elephant_and_friends.tex",
        "lion_and_mouse.tex",
        "elephant_and_mouse.tex",
        "nessie_the_monster_of_lochess.tex",
        "cinderella.tex",
        "the_frog_prince.tex",
        "the_lost_ring.tex",
        "the_rabbit_and_the_tortoise.tex",
        "the_shepherd_boy.tex",
        "the_kings_nightingale.tex",
        "rabbit.tex",
        "the_hidden_treasure.tex",
        "act_as_the_others.tex",
        "siege_of_vienna.tex",
        "gulliver.tex",
        "ali_baba.tex",
        "the_moon_in_the_well.tex",
        "the_donkey_that_could_sing.tex",
        "romeo_and_juliet.tex",
        "the_fox_who_got_caught_in_the_tree_trunk.tex",
        "the_sleeping_beauty.tex",
        "a_wise_counting.tex",
        "birbals_sweet_reply.tex",
    ]



class Lang(IntEnum):
    DUTCH = 0
    ENGLISH = 1
    TURKISH = 2
    SPANISH = 3


def select_story_and_vocab(fname):
    fname = r"source_files/{}".format(fname)
    fp = open(fname, "r")
    story = ""
    for line in fp:
        if "%words" in line:
            break
        story += line.strip()

    words = ""
    for line in fp:
        words += line.strip()

    lines = story.split(r"\\")
    story = []
    for line in lines:
        if len(line) < 3:  # minimal length of sensible sentence
            continue
        #print(line)
        # split line into sentences, one for each language
        sentences = [s.strip() for s in line.split("&")]
        story.append(sentences)
    
    words = words.split(r"\\")
    vocab = []
    for word in words:
        if len(word) < 3:  # minimal length of sensible sentence
            continue
        #print(word)
        w = [w.strip() for w in word.split("&")]
        vocab.append(w) 
    
    return story, vocab

def make_latex_string(story, vocab, col1, col2):
    #table_format = "\\begin{longtable}{L||R}\\toprule"
    table_format = "\\begin{longtable}{L||L}\\toprule"
    res = [] # list of latex strings
    # section title 
    res.append("\section{{ {} / {} }}".format(story[0][col1],story[0][col2]))
    # start story table 
    res.append(table_format)
    # header of table
    res.append("{} & {} \\\\ \midrule".format(story[0][col1], story[0][col2]))
    # story itself
    for line in story[1:]:
        res.append("{} & {} \\\\".format(line[col1], line[col2]))
    # trailer
    res.append("\\bottomrule \\end{longtable}")

    include_vocab = True
    if include_vocab is False:
        res.append("\\clearpage")
        return "\n".join(res)

    # word list
    res.append(table_format)
    for line in vocab:
        res.append("{} & {} \\\\".format(line[col1], line[col2]))

    # trailer
    res.append("\\bottomrule \\end{longtable}")
    res.append("\\clearpage")

    return "\n".join(res)


template = r"""
\documentclass[12pt]{{article}}
\usepackage{{ctable}} % for toprule
\usepackage{{a4wide}}
\usepackage[T1]{{fontenc}}
\usepackage[utf8]{{inputenc}}
\usepackage{{fouriernc}}
\usepackage{{longtable}}
\usepackage{{marginnote}}
\usepackage{{manfnt}}

\newcommand{{\oak}}[1]{{{{\leavevmode\color{{red}}#1}}\marginnote{{\dbend}}}}
\newcommand{{\nvf}}[1]{{{{\leavevmode\color{{red}}#1}}\marginnote{{\dbend}}}}
\newcolumntype{{L}}{{>{{\raggedright\arraybackslash}}p{{7.5cm}}}}
\newcolumntype{{R}}{{>{{\raggedleft\arraybackslash}}p{{7.5cm}}}}

\begin{{document}}

\tableofcontents
\clearpage

{}

\end{{document}}
"""

def make_doc(lang_left, lang_right, fname):
    res = []
    for f in files:
        story, vocab = select_story_and_vocab(f)
        res.append(make_latex_string(story, vocab, lang_left, lang_right))
    res = template.format("\n".join(res))
        
    fp = open(fname+".tex", "w")
    fp.write(res)
    fp.close()
    os.system("pdflatex {}.tex".format(fname))
    os.system("pdflatex {}.tex".format(fname))
    os.system("pdflatex {}.tex".format(fname))
    os.system("rm {}.aux".format(fname))
    os.system("rm {}.log".format(fname))
    os.system("rm {}.tex".format(fname))
    os.system("rm {}.toc".format(fname))

make_doc(Lang.TURKISH, Lang.DUTCH, "turkish_dutch")
make_doc(Lang.DUTCH, Lang.ENGLISH, "dutch_english")
make_doc(Lang.ENGLISH, Lang.DUTCH, "english_dutch")
