import re

files = [
    "mbe_p1.txt",
    "mbe_p2.txt",
    "mbe_p3.txt",
    "mbf_p1.txt",
    "mbf_p2.txt",
    "mbf_p3.txt",
         ]

for f in files:
    with open(f, "r") as fp:
        story = "".join([l for l in fp])

    story = re.sub(r'\n(\n)+', r'<par>', story)
    story = re.sub(r'(\n)', r' ', story)
    story = re.sub(r'<par>', r'\n\n', story)

    with open(f, "w") as fp:
        fp.write(story)
