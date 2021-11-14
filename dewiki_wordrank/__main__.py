import re
import html
from pathlib import Path

"""
Iterates over text files compiled by "WikiExtractor" and counts word occurrences.
"""

PACKAGE_PATH = Path(__file__).parent.absolute()
WIKIPEDIA_TEXT_DIR = Path('/mnt/c/Users/gregor/Dropbox/Python/_data/WikipediaDe/text')

min_word_len = 2
result_normal_case = {}
result_lower_case = {}


def clean_text(text):
    text = text.strip()
    text = html.unescape(text)
    text = re.sub(r'<[^>]+>', ' ', text)  # strip comments, <ref> and other tags etc.

    return text


for directory in WIKIPEDIA_TEXT_DIR.iterdir():
    if directory.name.startswith('.') or not directory.is_dir():
        continue

    for text_file in directory.iterdir():
        if text_file.name.startswith('.'):
            continue

        # open file
        with open(text_file) as f:
            lines = f.readlines()

        for line in lines:
            if line.startswith(('<doc', '</doc>')):
                continue

            line = clean_text(line)
            if not line:
                continue

            # get words
            words = [w for w in re.findall(r'\w+', line) if len(w) >= min_word_len and re.match(r'^\d+$', w) is None]
            for word in words:
                result_normal_case[word] = result_normal_case.get(word, 0) + 1
                word_lower = word.lower()
                result_lower_case[word_lower] = result_lower_case.get(word_lower, 0) + 1

# save output
output_normal_case = [f'{x[0]}\t{x[1]}' for x in sorted(result_normal_case.items(), reverse=True, key=lambda x: x[1])]
with open(PACKAGE_PATH.joinpath('result_normal_case.txt'), mode='w') as f:
    f.write('\n'.join(output_normal_case))

output_lower_case = [f'{x[0]}\t{x[1]}' for x in sorted(result_normal_case.items(), reverse=True, key=lambda x: x[1])]
with open(PACKAGE_PATH.joinpath('result_lower_case.txt'), mode='w') as f:
    f.write('\n'.join(output_lower_case))
