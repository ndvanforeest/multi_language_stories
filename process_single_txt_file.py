import nltk.data

#nltk.download()

tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')
fp = open("story.txt")
data = fp.read()
for t in tokenizer.tokenize(data):
    print("&\n{}&\n\\\\".format(t))
#print('\n-----\n'.join(tokenizer.tokenize(data)))

