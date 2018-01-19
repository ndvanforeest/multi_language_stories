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
        print(len(story_left))
        print(len(story_right))
        for x, y in zip(story_left, story_right):
            print(x)
            print(y)
        quit()

    if len(words_left) != len(words_right):
        print("left and right word lists are not of the same length")
        quit()

    return story_left, story_right

def latex_one_page(story, lang, left):
    res = []
    res.append(r"\begin{pages}")
    if left == True:
        res.append(r"\begin{Leftside}")
        res.append(r"\selectlanguage{{{}}}".format(config.language[lang]))
    else:
        res.append(r"\begin{Rightside}")
        res.append(r"\selectlanguage{{{}}}".format(config.language[lang]))
    #res.append(r"\selectlanguage{greek}")
    res.append(r"\beginnumbering")
    res.append(r"\pstart[\section{{{}}}]".format(story[0]))
    for line in story[1:]:
        if len(line) == 0:
            res.append(r"\pend")
            res.append(r"\pstart")
        else:
            res.append(line)
    res.append(r"\pend")
    res.append(r"\endnumbering")
    if left == True:
        res.append(r"\end{Leftside}")
    else:
        res.append(r"\end{Rightside}")
    res.append(r"\end{pages}")
    return "\n".join(res)


def make_header_and_trailer(lang_left, lang_right):
    left = config.language[lang_left]
    right = config.language[lang_right]
    res = []
    res.append(r"""
    \documentclass[a5paper]{article}
    \usepackage[margin=5mm]{geometry}
    """)
    res.append(r"\usepackage[{},{}]{{babel}}".format(left, right))
    res.append(r"""
    \usepackage[T1]{fontenc}
    \usepackage[utf8]{inputenc}
    \usepackage{tgheros}
    \usepackage{url}
    \usepackage[series={A},noend,nocritical,noeledsec]{reledmac}
    \usepackage[]{reledpar}
    \maxhnotesX{0.2\textheight}
    \beforenotesX{5pt}
    \setgoalfraction{0.95}
    \numberlinefalse
    \author{en-nl: Nicky van Foreest\\
    en-tr: Onur Kilic\\
    en-es: Cesar Sala
    }""")
    res.append(r"\title{{Parallel translations ({}-{})}}".format(left, right))
    res.append(r"""
    \begin{document}
    \maketitle
    \tableofcontents
    """)
    header = "\n".join(res)
    trailer = r"\end{document}"
    return header, trailer

def make_all_doc(lang_left, lang_right, out_file):
    header, trailer = make_header_and_trailer(lang_left, lang_right)
    res = [header]
    for fname in config.files:
        if not os.path.isfile("./source_files/"+fname):
            continue
        #if "baked" not in fname:
        #    continue
        story_left, story_right = select_story_and_vocab(lang_left, lang_right, fname)
        if story_left is None:
            continue
        res.append(latex_one_page(story_left, lang_left, left=True))
        res.append(latex_one_page(story_right, lang_right, left=False))
        res.append(r"\Pages")
        #res.append(r"\clearpage")
    res.append(trailer)
    res = "\n".join(res)
    with open("dummy.tex", "w") as fp:
        fp.write(res)
    os.system("pdflatex dummy.tex")
    os.system("pdflatex dummy.tex")
    os.system("pdflatex dummy.tex")
    #os.system("pdflatex dummy.tex")
    os.system("mv dummy.pdf pdf_files/{}.pdf".format(out_file))
    os.system("rm dummy.*")

if __name__ == "__main__":
    make_all_doc("en", "nl", "english_dutch_facing")
    #make_all_doc("nl", "en", "dutch_english_facing")
    #make_all_doc("tr", "en", "turkish_english_facing")
    #make_all_doc("es", "en", "spanish_english_facing")
