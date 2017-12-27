from enum import IntEnum


class Lang(IntEnum):
    nl = 0
    en = 1
    tr = 2
    es = 3

# the lists below contain the stories that have been checked for a specific language. x

# dutch 
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
    "hercules.tex",
    "boys_will_be_boys",
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
    "hercules.tex",
    "hodja_the_king.tex",
    "hodja_and_ox.tex",
    "hodja_and_the_scholar.tex",
    "the_hidden_treasure.tex",
    "sweet_quarrels.tex",
    "the_relatives_of_the_donkey.tex",
    "act_as_the_others.tex",
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
    "the_dog_and_the_sparrow.tex",
    "the_sleepy_teacher.tex",
    "four_friends.tex",
    "siege_of_vienna.tex",
    "the_three_wisemen_and_the_camel.tex",
    "the_princess_and_the_pea.tex",
    "the_traveling_musicians.tex",
    "the_enchanting_horse.tex",
    "the_merchant_and_the_genie.tex",
    "the_old_man_with_the_two_black_dogs.tex",
    "the_monkey_advisor.tex",
    "cinderella_2.tex",
    "old_sultan.tex",
    "the_enchanting_horse_2.tex",
    "prince_omar.tex",
    "the_little_mermaid.tex",
    "the_ruined_man.tex",
    "the_lion_and_the_elephant.tex",
    "the_snow_queen.tex",
    "bluebeard.tex",
    "the_story_of_the_baked_head.tex",
]

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

\tableofcontents
\clearpage

\clearpage

{}

\end{{document}}
"""


