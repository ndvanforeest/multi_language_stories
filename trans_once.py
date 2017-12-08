"""
Add another language to the source files. 

The problem was like this. I had google translate english stories into dutch, or the other way around. It did not, however, add a Turkish translation to it. With this program I added a Turkish translation.

Add other languages can be done likewise.
"""


from googletrans import Translator
translator = Translator()


files = [
]

def translate_story(story):
    res = []
    sentences = story.split(r"\\")
    for sentence in sentences:
        if len(sentence) <= 2:
            continue
        print(sentence)
        nl, en, tr = sentence.split("&")
        tr = translator.translate(en, src="en", dest="tr").text
        res.append("{}&{}&\n{}\n\\\\".format(nl, en, tr))
        #es = translator.translate(en, src="en", dest="es").text
        #res = "{}&{}&\n{}&\n{}\n\\\\".format(nl, en, tr, es)
    return "".join(res)

def translate_all():
    for fname in files:
        fin = open(r"source_files/{}".format(fname), 'r')
        story = "".join(list(fin))
        story = translate_story(story)
        fin.close()
        fout = open(r"source_files/{}".format(fname), 'w')
        fout.write(story)
        fout.close()

if __name__ == "__main__":
    translate_all()
