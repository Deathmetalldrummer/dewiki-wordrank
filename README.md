# dewiki-wordrank

Tab-delimited word frequency list compiled from the German Wikipedia.

XML dump file read with [WikiExtractor](https://github.com/attardi/wikiextractor)

Results are in form of a tab-delimited txt file inside [results.zip](https://github.com/gambolputty/dewiki-wordrank/raw/master/results.zip)

Example:
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

Wikipedia dump from _2019-05-20_

## Extract text from Wikipedia dump
`python -m wikiextractor.WikiExtractor <Wikipedia dump file> --output <output path>`