#!/usr/bin/python3
import os
import re
from enum import IntEnum


files = [
]

if len(files) == 0:
    files = [
        "everyday.tex",
        "my_daily_rhythm.tex",
        "taking_a_shower.tex",
        "shaving.tex",
        "grandmas_soup.tex",
        "a_walk_in_the_park.tex",
        "fire.tex",
        "flying.tex",
        "traffic.tex",
        "airport.tex",
        "swimming.tex",
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
        "the_donkey_of_hodja.tex",
        "rabbit.tex",
        "hodja_the_king.tex",
        "hodja_and_ox.tex",
        "hodja_and_the_scholar.tex",
        "the_hidden_treasure.tex",
        "sweet_quarrels.tex",
        "the_relatives_of_the_donkey.tex",
        "act_as_the_others.tex",
        "siege_of_vienna.tex",
        "gulliver.tex",
        "ali_baba.tex",
        "the_moon_in_the_well.tex",
        "the_donkey_that_could_sing.tex",
        "romeo_and_juliet.tex",
        "the_fox_who_got_caught_in_the_tree_trunk.tex",
        "the_sleeping_beauty.tex",
        "half_the_reward.tex",
        "making_a_difference.tex",
        "birbal_shortens_the_road.tex",
        "birbal_turns_tables.tex",
        "a_wise_counting.tex",
        "question_for_question.tex",
        "birbals_sweet_reply.tex",
        "birbal_the_servant.tex",
        "birbal_the_wise.tex",
        "the_sharpest_sword.tex",
        "the_lazy_dreamer.tex",
        "birbal_is_brief.tex",
        "the_well_dispute.tex",
        "list_of_blinds.tex",
        "a_handfull_of_answers.tex",
        "the_donkey_and_the_dog.tex",
        "the_donkey_and_the_cotton.tex",
        "the_cunning_bats.tex",
        "the_clever_bull.tex",
        "the_sleepy_teacher.tex",
        "four_friends.tex",
        "the_three_wisemen_and_the_camel.tex",
        "the_monkey_advisor.tex",
        "prince_omar.tex",
        "bluebeard.tex",
    ]

#for f in files:
#    print(r"%\input{{source_files/{}}}".format(f))
#quit()

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
    #print(fname)
    
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

def make_section_title(t1, t2):
    if "footnote" in t1:
        t1 = re.sub(r'\\footnote{.*}', "", t1)
    if "footnote" in t2:
        t2 = re.sub(r'\\footnote{.*}', "", t2)
    return "\section{{ {} / {} }}".format(t1, t2)
    
        
def make_latex_string(story, vocab, col1, col2):
    #table_format = "\\begin{longtable}{L||R}\\toprule"
    table_format = "\\begin{longtable}{L||L}\\toprule"
    res = [] # list of latex strings
    #print(story)
    title = make_section_title(story[0][col1],story[0][col2])
    res.append(title)
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
\usepackage{{url}}

\newcommand{{\oak}}[1]{{{{\leavevmode\color{{red}}#1}}\marginnote{{\dbend}}}}
\newcommand{{\nvf}}[1]{{{{\leavevmode\color{{red}}#1}}\marginnote{{\dbend}}}}
\newcolumntype{{L}}{{>{{\raggedright\arraybackslash}}p{{8cm}}}}
\newcolumntype{{R}}{{>{{\raggedleft\arraybackslash}}p{{8cm}}}}

\begin{{document}}

\tableofcontents
\clearpage

\clearpage

{}

\end{{document}}
"""
#\input{{introduction}}

def make_all_docs(lang_left, lang_right, fname):
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

def make_test_doc(lang_left, lang_right, fname):
    res = []
    for f in files:
        story, vocab = select_story_and_vocab(f)
        res.append(make_latex_string(story, vocab, lang_left, lang_right))
    res = template.format("\n".join(res))
        
    fp = open(fname+".tex", "w")
    fp.write(res)
    fp.close()
    os.system("pdflatex {}.tex".format(fname))
    #os.system("rm {}.tex".format(fname))
    os.system("rm {}.aux".format(fname))
    os.system("rm {}.log".format(fname))
    os.system("rm {}.toc".format(fname))

def check_if_all_files_are_included():
    # check whether all files in source_files are included in the list
    # of files above
    list1 = set(files)
    list2 = set(os.listdir("./source_files"))
    missing = list2 - list1
    print(missing)
    quit()

#check_if_all_files_are_included()

if __name__ == "__main__":
    if len(files) == 1:
        make_test_doc(Lang.ENGLISH, Lang.DUTCH, "test_english_dutch")
        #make_test_doc(Lang.TURKISH, Lang.DUTCH, "test_turkish_dutch")
    else:
        make_all_docs(Lang.TURKISH, Lang.DUTCH, "turkish_dutch")
        make_all_docs(Lang.DUTCH, Lang.ENGLISH, "dutch_english")
        make_all_docs(Lang.ENGLISH, Lang.DUTCH, "english_dutch")
