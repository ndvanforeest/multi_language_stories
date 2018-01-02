#!/usr/bin/env python3

import re

target_language, fname = "nl", "merchant.txt"
#target_language, fname = "es", "aladdin.txt"
#target_language, fname = "tr", "boys_will_be_boys.txt"

res = {}

fin = fname[:-3]+"tex"
with open("{}_{}".format(target_language, fin), "r") as fp:
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
translation = {en.strip(): ta for en, ta in zip(english, target)}

res = []
with open("source_files/"+fname, "r") as fp:
    for line in fp:
        if line[:4] == "<en>":
            sentence = line[4:].strip()
            trans = translation[sentence]
            res.append("<en>{}\n<{}>{}\n".format(sentence, target_language, trans))
        else:
            res.append(line)

with open("merged_file.txt", "w") as fp:        
    for r in res:
        fp.write(r)


