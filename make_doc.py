#!/usr/bin/python3
import os
import re

import config

def select_story_and_vocab(lang_left, lang_right, fname):
    lang_left = "<{}>".format(lang_left)
    lang_right = "<{}>".format(lang_right)
    left = []
    with open(r"source_files/{}".format(fname)) as fp:
        for line in fp:
            if line[:4] == lang_left:
                left.append(line[4:].strip())

    right = []
    with open(r"source_files/{}".format(fname)) as fp:
        for line in fp:
            if line[:4] == lang_right:
                right.append(line[4:].strip())

    if len(left)==0 or len(right)==0:
        # the source or target language is not in the file
        return None

    if len(left) != len(right):
        print("left and right are not of the same length")
        quit()

    story = [[l, r] for l, r in zip(left, right)]
    return story

def section_title(t1, t2):
    if "footnote" in t1:
        t1 = re.sub(r'\\footnote{.*}', "", t1)
    if "footnote" in t2:
        t2 = re.sub(r'\\footnote{.*}', "", t2)
    return "\section{{ {} / {} }}".format(t1, t2)
    
        
def latex_parallel(story):
    # latex output for translation next to each other

    #table_format = "\\begin{longtable}{L||R}\\toprule"
    table_format = "\\begin{longtable}{L||L}\\toprule"
    res = [] # list of latex strings
    #print(story)
    title = section_title(story[0][0],story[0][1])
    res.append(title)
    # start story table 
    res.append(table_format)
    # header of table
    res.append("{} & {} \\\\ \midrule".format(story[0][0], story[0][1]))
    # story itself
    for line in story[1:]:
        res.append("{} & {} \\\\".format(line[0], line[1]))
    # trailer
    res.append("\\bottomrule \\end{longtable}")
    res.append("\\clearpage")
    return "\n".join(res)


def make_all_doc(lang_left, lang_right, latex_file):
    res = []
    for fname in config.files:
        if not os.path.isfile("./source_files/"+fname):
            continue
        story = select_story_and_vocab(lang_left, lang_right, fname)
        if story is None:
            continue
        res.append(latex_parallel(story))
    res = config.doc_template.format(lang_left, lang_right, "\n".join(res))
    with open(latex_file+".tex", "w") as fp:
        fp.write(res)
    try:
        # quit if an error occurs, rather than trying to pdflatex the
        # file a few times.
        os.system("pdflatex {}.tex".format(latex_file))
    except:
        quit()
    os.system("pdflatex {}.tex".format(latex_file))
    os.system("pdflatex {}.tex".format(latex_file))
    os.system("rm {}.aux".format(latex_file))
    os.system("rm {}.log".format(latex_file))
    os.system("rm {}.tex".format(latex_file))
    os.system("rm {}.toc".format(latex_file))

if __name__ == "__main__":
    make_all_doc("tr", "en", "turkish_english")
    #make_all_doc("nl", "en", "dutch_english")
    make_all_doc("en", "nl", "english_dutch")
    #make_all_doc("es","en", "spanish_english")
