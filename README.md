# dewiki-wordrank

Tab-delimited word frequency list compiled from the German Wikipedia.

Words were converted to lowercase before being counted.

The list can be found here: [result.zip](https://github.com/gambolputty/dewiki-wordrank/blob/main/result.zip) (compressed txt-file)

Example output:
```
öpnv   3547
sylvia   3547
gewonnene   3546
milde   3546
deal   3546
amy   3546
mittelgewicht   3546
gegenspieler   3545
...
```

Date of Wikipedia dump file: _02-Nov-2021_

## Compiling the list

To compile the list yourself, you need Python 3.8+ and [Poetry](https://python-poetry.org/) installed.

### 1. Clone the repository and install dependencies with [Poetry](https://python-poetry.org/):

```shell
$ git clone git@github.com:gambolputty/dewiki-wordrank.git
$ cd dewiki-wordrank
$ poetry install
```

### 2. Extract Wikipedia pages

Extract the Wikipedia pages from the XML dump file with [WikiExtractor](https://github.com/attardi/wikiextractor):

```shell
$ poetry run python -m wikiextractor.WikiExtractor /path-to-xml-file.xml.bz2 --output /path-to-output-directory
```

### 3. Count word occurrences

Run the script in this repository to compile the list of word occurrences:

```shell
$ poetry run python -m dewiki_wordrank /path-to-wikiextractor-output-directory
```

The result will be saved in the [dewiki_wordrank](/dewiki_wordrank) directory.

----

[![License: CC BY-SA 4.0](https://img.shields.io/badge/License-CC%20BY--SA%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by-sa/4.0/)
