#!/usr/bin/python3
import os
import re

import config
from config import Lang

"""

@ oak:

Just unquote the files one by one as you go. I = nvf might add some files to the end of it, when I tackled a few more stories, but that will not be problem. 

Don't unquote more. The code below contains a test on this. When there are more files unquoted, running the script will automatically make the parallel texts version. 

In case you see a case to make the alternating presentation also available, let me know. Then we'll make those too. As for now, I just made the alternating presentation to aid me in checking the translations.

"""

files = [
    "everyday.tex",
#     "my_daily_rhythm.tex",
#     "taking_a_shower.tex",
#     "shaving.tex",
#     "grandmas_soup.tex",
#     "a_walk_in_the_park.tex",
#     "fire.tex",
#     "flying.tex",
#     "traffic.tex",
#     "airport.tex",
#     "swimming.tex",
#     "hercules.tex",
#     "elephant_and_friends.tex",
#     "lion_and_mouse.tex",
#     "elephant_and_mouse.tex",
#     "nessie_the_monster_of_lochess.tex",
#     "cinderella.tex",
#     "the_frog_prince.tex",
#     "the_lost_ring.tex",
#     "the_rabbit_and_the_tortoise.tex",
#     "the_shepherd_boy.tex",
#     "the_kings_nightingale.tex",
#     "the_donkey_of_hodja.tex",
#     "rabbit.tex",
#     "hercules.tex",
#     "hodja_the_king.tex",
#     "hodja_and_ox.tex",
#     "hodja_and_the_scholar.tex",
#     "the_hidden_treasure.tex",
#     "sweet_quarrels.tex",
#     "the_relatives_of_the_donkey.tex",
#     "act_as_the_others.tex",
#     "siege_of_vienna.tex",
#     "gulliver.tex",
#     "ali_baba.tex",
#     "the_moon_in_the_well.tex",
#     "the_donkey_that_could_sing.tex",
#     "romeo_and_juliet.tex",
#     "the_fox_who_got_caught_in_the_tree_trunk.tex",
#     "the_sleeping_beauty.tex",
#     "half_the_reward.tex",
#     "making_a_difference.tex",
#     "birbal_shortens_the_road.tex",
#     "birbal_turns_tables.tex",
#     "a_wise_counting.tex",
#     "question_for_question.tex",
#     "birbals_sweet_reply.tex",
#     "birbal_the_servant.tex",
#     "birbal_the_wise.tex",
#     "the_sharpest_sword.tex",
#     "the_lazy_dreamer.tex",
#     "birbal_is_brief.tex",
#     "the_well_dispute.tex",
#     "list_of_blinds.tex",
#     "a_handfull_of_answers.tex",
#     "the_donkey_and_the_dog.tex",
#     "the_donkey_and_the_cotton.tex",
#     "the_cunning_bats.tex",
#     "the_clever_bull.tex",
#     "the_sleepy_teacher.tex",
#     "four_friends.tex",
#     "the_three_wisemen_and_the_camel.tex",
#     "the_princess_and_the_pea.tex",
#     "the_enchanting_horse.tex",
#     "the_old_man_with_the_two_black_dogs.tex",
#     "the_monkey_advisor.tex",
#     "cinderella_2.tex",
#     "the_enchanting_horse_2.tex",
#     "prince_omar.tex",
#     "the_little_mermaid.tex",
#     "bluebeard.tex",
]


if len(files) == 0:
    files = config.all_files


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

    title = section_title(story[0][col1],story[0][col2])
    res.append(title)

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
    if len(files) <=2:
        make_test_doc(Lang.ENGLISH, Lang.TURKISH, "test_english_turkish")
    else:
        make_all_docs(Lang.TURKISH, Lang.DUTCH, "turkish_dutch")
        make_all_docs(Lang.DUTCH, Lang.ENGLISH, "dutch_english")
