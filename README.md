# Parallel texts in multiple languages


This repo contains English stories translated to (currently) Dutch and Turkish. The structure is like this.

The source_files directory contains the source files. Each source file contains one story. A file consists of sets of lines, each starting with the country code in < > signs, like so <en>, <nl>, and so on.

- make_facing.py: makes a pdf file with two languages on facing pages.

- make_two_columsn.py: makes a pdf file with the two languages in columns one page.

- make_one_language.py: makes pdf file with just one languate, i.e., no translations.

The process works like this.

1. start with some .txt (plain ascii) file.

2. format_english_text.py: formates a raw txt file and split it into lines each of which starts with <en>

2. translate_to_target_language.py: have google translate the formated file to a draft translation. 

3. Edit the file translated by google by hand to improve the translation by hand (e.g., an ass is not always a donkey, but in the stories I included, the word ass only refers to a donkey.)

4. merge.py: merge the hand-edited file with the original source file. Copy the merged file to the source_files directory.

In case you like to add a language, or otherwise contribute to this project let me know. The idea is to take the English stories as leading, and translate those stories to a target language, in my case Dutch. The sentences in the target language 1) should be, foremost, natural to a native speaker, 2) try to stay as close as possible to the English source, both in word sequence as in meaning. It is evident that,  in general, it is impossible to translate the English in a one-to-one way to a target language. Hence, (once more), the most important criterion to meet is that the sentences in the target language are natural so that a learner of the target language gets a feeling for the language as used by natives.

If you plan to help add a language, please mind the structure of the source files. They are input into latex files, so the formatting is crucial.

An interesting extension would be to read the stories (by a native) and record them (with your mobile) to  mp3, and share the mp3. Like this, one can first read and study a story, and then later listen to it, while biking to work or so. 

So, why did I build this? In the first place, I dislike reading grammar books. Second, I find the stories in most  learners books very boring. I find them so boring in fact that I hate to read them twice, let alone multiple times. However, I don't mind reading a good stories multiple times, just to study the language. Third, memorizing words in a new language becomes, for me at least, much easier when they are used right away in a story; these words acquire meaning in this context. And finally, after having read a story a few times, so that I know what to expect, I like to listen to it while doing something else, like hanging out the wash.

