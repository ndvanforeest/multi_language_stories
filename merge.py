#!/usr/bin/env python3

import os
import re
import click


@click.command()
@click.argument('filename')
def merge(filename):
    """Merge a translated latex file with the target language indicated by the first two letters of the file with a file in source_files and label the translation with the target language.

    Example:

    ./merge.py nl_piet.tex

    merges nl_piet.tex with source_files/piet.txt and labels each translated line in piet.txt with <nl>.
    """
    target_language = filename[:2]
    fname = filename[3:-4]

    res = {}

    with open(filename, "r") as fp:
        res = []
        for line in fp:
            res.append(line.strip())

    #p = re.compile('noindent.*') #\\newline')

    res = "".join(res)

    #regex = r"([a-zA-Z]+) \d+"
    #matches = re.findall(regex, "June 24, August 9, Dec 12")
    #print(matches)
    #regex = r"noindent([a-zA-Z ]+"
    regex = r"noindent(.*?)\\newline"
    #re.search(r'Part 1\.(.*?)Part 3', s).group(1)
    english = re.findall(regex, res)

    regex = r"\\newline(.*?)}"
    target = re.findall(regex, res)

    if len(target) != len(english):
        print("parsing went wrong")
        quit()

    # we need to remove the trailing white space in the english sentences. 
    translation = {e.strip(): t for e, t in zip(english, target)}

    res = []
    with open("source_files/{}.txt".format(fname), "r") as fp:
        for line in fp:
            if line[:4] == "<en>":
                #sentence = line[4:].strip()
                #trans = translation[sentence]
                #res.append("<en>{}\n<{}>{}\n".format(sentence, target_language, trans))
                sentence = line[4:].strip()
                res.append("<en>{}".format(sentence))
                trans = translation[sentence]
                res.append("<{}>{}".format(target_language, trans))
            else:
                res.append(line)

    os.system("mv source_files/{}.txt source_files/{}_old.txt".format(fname, fname))

    with open("source_files/{}.txt".format(fname), "w") as fp:
        fp.write("\n".join(res))
        #for r in res:
        #    fp.write(r)

if __name__ == "__main__":
    merge()
