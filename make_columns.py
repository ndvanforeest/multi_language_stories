import os

import config


def read_story_and_vocab(lang, fname):
    lang_string = f"<{lang}>"
    # with open(f"source_files/{fname}".format(fname)) as fp:
    with open(f"source_files/{fname}", "r") as fp:
        story = []
        words = []
        for line in fp:
            if line[:-1] == config.vocabulary[lang]:
                words = [line[4:].strip()]
                break
            if line[:4] == lang_string:
                story.append(line[4:].strip())
        for line in fp:
            if line[:4] == lang_string:
                words.append(line[4:].strip())
    return story, words


def merge_story_and_vocab(lang_left, lang_right, fname):
    story_left, words_left = read_story_and_vocab(lang_left, fname)
    story_right, words_right = read_story_and_vocab(lang_right, fname)

    if len(story_left) == 0 or len(story_right) == 0:
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

    story = [[lang_left, lang_right]]
    story += [[l, r] for l, r in zip(story_left, story_right)]
    words = [[l, r] for l, r in zip(words_left, words_right)]
    return story, words


def make_two_columns(story, words):
    lang_left = config.language[story[0][0]]
    lang_right = config.language[story[0][1]]

    title = story[1]
    print(r"\begin{paracol}{2}")
    print(f"\selectlanguage{{{lang_left}}}")
    print(f"\section{{{title[0]}}}")
    print(r"\switchcolumn")
    print(f"\selectlanguage{{{lang_right}}}")
    print(f"\section*{{{title[1]}}}")
    print(r"\switchcolumn*")

    for line in story[2:]:
        print(f"\selectlanguage{{{lang_left}}}")
        print(line[0])
        print(r"\switchcolumn")
        print(f"\selectlanguage{{{lang_right}}}")
        print(line[1])
        print(r"\switchcolumn*")
    print(r"\end{paracol}")

    if not words:
        print("\\clearpage")
        return

    print(r"\vspace{0.5cm}")

    print(r"\begin{paracol}{2}")
    print(f"\selectlanguage{{{lang_left}}}")
    print(r"\textbf{" + words[0][0] +"}")
    print(r"\switchcolumn")
    print(f"\selectlanguage{{{lang_right}}}")
    print(r"\textbf{" + words[0][1] +"}")
    print(r"\switchcolumn*")
    for line in words[1:]:
        print(f"\selectlanguage{{{lang_left}}}")
        print(line[0])
        print(r"\switchcolumn")
        print(f"\selectlanguage{{{lang_right}}}")
        print(line[1])
        print(r"\switchcolumn*")
    print(r"\end{paracol}")


def make_all_doc(lang_left, lang_right):
    for fname in config.files:
        if not os.path.isfile("./source_files/" + fname):
            continue
        stories, words = merge_story_and_vocab(lang_left, lang_right, fname)
        if stories is None:
            continue
        make_two_columns(stories, words)
        # return


if __name__ == "__main__":
    # make_all_doc("tr", "en")
    # make_all_doc("nl", "en")
    # make_all_doc("en", "nl")
    make_all_doc("es","en")
