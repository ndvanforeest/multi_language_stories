#!/usr/bin/python3
import os
import re

import config
from config import Lang

files = [
    "cinderella_2.tex",
    "the_enchanting_horse_2.tex",
    "the_little_mermaid.tex",
    "the_princess_and_the_pea.tex",
    "the_story_of_the_baked_head.tex",
]

files = [
    "cinderella_2.tex",
    ]

if len(files) == 0:
    files = config.all_files


def check_if_all_files_are_included():
    # check whether all files in source_files are included in the list
    # of files above
    list1 = set(config.all_files)
    list2 = set(os.listdir("./source_files"))
    missing = list2 - list1
    print(missing)
    quit()

#check_if_all_files_are_included()



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

def section_title(t1, t2):
    if "footnote" in t1:
        t1 = re.sub(r'\\footnote{.*}', "", t1)
    if "footnote" in t2:
        t2 = re.sub(r'\\footnote{.*}', "", t2)
    return "\section{{ {} / {} }}".format(t1, t2)
    
        
def latex_parallel(story, vocab, col1, col2):
    # latex output for translation next to each other

    #table_format = "\\begin{longtable}{L||R}\\toprule"
    table_format = "\\begin{longtable}{L||L}\\toprule"
    res = [] # list of latex strings
    #print(story)
    title = section_title(story[0][col1],story[0][col2])
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


def latex_alternating(story, vocab, col1, col2):
    # latex output for alternating translations 
    template = "\\noindent\n{}\\newline\n{}\n\\vspace{{1mm}}\n"
    res = []
    for line in story:
        res.append(template.format(line[col1], line[col2]))
    
    include_vocab = True
    if include_vocab is False:
        res.append("\\clearpage")
        return "\n".join(res)

    # word list
    for line in vocab:
        res.append(template.format(line[col1], line[col2]))

    # trailer
    res.append("\\clearpage")

    return "\n".join(res)


def make_all_docs(lang_left, lang_right, fname):
    res = []
    for f in files:
        story, vocab = select_story_and_vocab(f)
        res.append(latex_parallel(story, vocab, lang_left, lang_right))
    res = config.doc_template.format("\n".join(res))
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
        res.append(latex_alternating(story, vocab, lang_left, lang_right))
    res = config.doc_template.format("\n".join(res))
        
    fp = open(fname+".tex", "w")
    fp.write(res)
    fp.close()
    os.system("pdflatex {}.tex".format(fname))
    #os.system("rm {}.tex".format(fname))
    os.system("rm {}.aux".format(fname))
    os.system("rm {}.log".format(fname))
    os.system("rm {}.toc".format(fname))




if __name__ == "__main__":
    if len(files) <=10:
        make_test_doc(Lang.ENGLISH, Lang.DUTCH, "test_english_dutch")
        #make_test_doc(Lang.TURKISH, Lang.DUTCH, "test_turkish_dutch")
    else:
        make_all_docs(Lang.TURKISH, Lang.DUTCH, "turkish_dutch")
        make_all_docs(Lang.DUTCH, Lang.ENGLISH, "dutch_english")
        make_all_docs(Lang.ENGLISH, Lang.DUTCH, "english_dutch")
