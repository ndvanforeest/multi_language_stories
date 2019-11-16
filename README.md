# Parallel texts in multiple languages


This repo contains English stories translated to (currently) Dutch, Turkish and Spanish.  

So, why did I build this? In the first place, I dislike reading
grammar books. Second, I find the stories in most language learners
books very boring, so boring in fact that I hate to read them twice,
let alone multiple times. However, I don't mind reading a good story
multiple times, and studying a language in the mean time. Third,
memorizing words in a new language becomes, for me at least, much
easier when they are used right away in a story; these words acquire
meaning in the context.


In case you like to add a language, or otherwise contribute to this
project let me know. The idea is to take the English stories as
leading, and translate those stories to a target language, in my case
Dutch. Mind that the target audience is a language learner. Thus, the
sentences in the target language 1) should be natural to a native
speaker, 2) but at the same time, try to stay as close as possible to
the English source, both in word sequence as in meaning. If you
deviate too much from the English original, it will often become too
hard to understand for somebody new to the language. Of course, in
general it is impossible to translate the English in a one-to-one way
to a target language. However, we should aim for it at least.


The structure is of the repo like this:

- The pdf files with the dual language texts can be found [here]](https://github.com/ndvanforeest/parallel-translations/tree/master/pdf_files).

- The source_files/ directory contains the source files. Each source file contains one story. A file consists of sets of lines, each starting with the country code in &lt; &gt; signs, like so &lt;en&gt;, &lt;nl&gt;, and so on.



Then there is an example file 

- The python program make_facing.py makes a pdf file with two languages, each on a facing page.

- make_one_language.py makes pdf file for just one languate, i.e., no translations.

The process works like this.

1. start with some .txt (plain ascii) file.

2. format_english_text.py: formates a raw txt file and splits it into lines each of which starts with '&lt;en&gt;'.

2. translate_to_target_language.py: have google translate the formated file to a draft translation. 

3. Then, edit the file translated by google by hand to improve the translation (e.g., an ass is not always a donkey, but in the stories I included, the word ass only refers to a donkey.) This step takes the most time. The other are more or less automatic.

4. merge.py: merge the hand-edited file with the original source file. Copy the merged file to the source_files directory.


An interesting extension would be to read the stories (by a native) and record them (with your mobile) to  mp3, and share the mp3. Like this, one can first read and study a story, and then later listen to it, while biking to work,  hanging out the wash, or something similar.


