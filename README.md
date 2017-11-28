# multi_language_stories


This repo contains English stories translated to (currently) Dutch and Turkish. The structure is like this.

The source_files directory contains the source files. Each source file contains one story. A file consists of sets of lines, separated by ampersands (&), the first line of a set is Dutch, the second English, the third is Turkish. The last line of a set ends with a double slash (\\\\).

The python file `make_docs.py` processes the source files into latex files, that in turn are processed (by a call to  pdf_latex) into pdf files. The other python file `test_single_source_file.tex` allows to test single source files and various ways of formatting. 

The pdf files speak for themselves, I guess.

In case you like to add a language, or otherwise contribute to this project let me know. The idea is to take the English stories as leading, and translate those stories to a target language, in my case Dutch. The sentences in the target language should be 1) simple and (very important) natural, and once this is ensured, 2) try to stay as close as possible to the English source. It is evident that is in general impossible to translate the English in a one-to-one way to a target language. Hence, (once more), the most important criterion to meet is that the sentences in the target language are simple and natural (from a native's point of view.)

If you plan to help add a language, please mind the structure of the source files. They are input into latex files, so the formatting is crucial.

An interesting extension would be to read the stories (by a native) and record them (with your mobile) to  mp3, and share the mp3. Like this, one can first read and study a story, and then later listen to it, while biking to work or so. BTW, I don't know whether this is ok with github. 

