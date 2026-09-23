# csci6032-hw2-rlindsay03
csci 6032 homework 2 repo
ethan lindsay
windows 11
gonna be using this to constrain a host agent, do some stuff with a docker container, and all that other good stuff.

## Text statistics

Run the command-line program with a UTF-8 text file:

```text
python src/text_stats.py sample.txt
```

It prints JSON containing the number of `lines`, `words`, and `characters`:

```json
{"lines": 5, "words": 14, "characters": 66}
```

To include the two most frequent words, use the optional `--top N` argument:

```text
python src/text_stats.py sample.txt --top 2
```

The output includes a `top` array of word/count objects. Words are compared
case-insensitively and ties are ordered alphabetically:

```json
{"lines": 5, "words": 14, "characters": 66, "top": [{"word": "67", "count": 1}, {"word": "beat", "count": 1}]}
```

Run the tests with Python's built-in `unittest` framework:

```text
python -m unittest discover -s tests
```