"""
Makes a text file, with fields separated by semicolons

>python3 anki_format.py > dummy.txt

Import dummy.txt in Anki, as a basic card, with field one as Front and field three as Back (in my case.)

"""


fname = r"source_files/my_daily_pattern.tex"
fp = open(fname, "r")


# translate & to ; and \\ to "space"
table = str.maketrans("&\\","; ")

string = ""
for line in fp:
    string += line.strip()
    if r"\\" in line:
        print(string.translate(table))
        string = ""
    

