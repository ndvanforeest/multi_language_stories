#!/usr/bin/python3
import os
import re

import config

def select_story_and_vocab(lang, fname):
    lang = "<{}>".format(lang)
    story = []
    with open(r"source_files/{}".format(fname)) as fp:
        for line in fp:
            if line[:-1] == "<en>Vocabulary":
                break
            if line[:4] == lang:
                story.append(line[4:].strip())
    return story

def section_title(t1):
    res = "\section*{{{}}}".format(t1)
    t1 = re.sub(r'\\footnote{.*}', "", t1)
    res += r"\addcontentsline{toc}{section}{\protect\numberline{}" + t1 + "}"
    return res
        
def make_latex(story):
    res = [] # list of latex strings
    title = section_title(story[0])
    res.append(title)
    for line in story[1:]:
        res.append(line)
    # trailer
    res.append("\\clearpage")
    return "\n".join(res)


doc_template = r"""
\documentclass[a5paper]{{article}}
\usepackage[margin=5mm]{{geometry}}
\usepackage[T1]{{fontenc}}
\usepackage[utf8]{{inputenc}}
\usepackage{{tgheros}}
\usepackage{{url}}
\usepackage{{multicol}}

\author{{en-nl: Nicky van Foreest\\
en-tr: Onur Kilic\\
en-es: Cesar Sala
}}
\title{{{}}}

\begin{{document}}
\maketitle

\begin{{multicols}}{{2}}
  \tableofcontents
\end{{multicols}}

\clearpage

{}

\end{{document}}
"""


def make_all_doc(lang, latex_file):
    res = []
    for fname in config.files:
        if not os.path.isfile("./source_files/"+fname):
            continue
        story = select_story_and_vocab(lang, fname)
        if len(story) == 0:
            continue
        res.append(make_latex(story))

    res = doc_template.format(lang, "\n".join(res))
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
    #make_all_doc("tr", "turkish")
    #make_all_doc("nl", "dutch")
    make_all_doc("en", "english")
    #make_all_doc("es", "spanish")
