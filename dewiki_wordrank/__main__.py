import sys
import re
import html
from pathlib import Path

"""
Iterates over text files compiled by "WikiExtractor" and counts word occurrences.

Run with:

$ poetry run python -m dewiki_wordrank <path-to-wikiextractor-output-directory>
"""


if len(sys.argv) <= 1:
    print('Please provide a path to the WikiExtractor output')
    sys.exit()

min_word_len = 2
result = {}
package_path = Path(__file__).parent.absolute()
wikipedia_text_path = Path(sys.argv[1])

print(f'Processing files in {wikipedia_text_path} and its subdirectories')


def clean_text(text):
    text = html.unescape(text)
    text = re.sub(r'<[^>]+>', ' ', text)  # strip comments, <ref> and other tags etc.
    text = text.strip()

    return text


for directory in wikipedia_text_path.iterdir():
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
            for word in [w.lower() for w in re.findall(r'\w+', line) if len(w) >= min_word_len and re.match(r'^\d+$', w) is None]:
                result[word] = result.get(word, 0) + 1

# save output
output = [f'{x[0]}\t{x[1]}' for x in sorted(result.items(), reverse=True, key=lambda x: x[1])]
with open(package_path.joinpath('result.txt'), mode='w') as f:
    f.write('\n'.join(output))
