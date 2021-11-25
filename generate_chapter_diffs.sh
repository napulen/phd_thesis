#!/bin/bash

chapters="1 2 3 4 5 6 7"
currenttag=$(git describe --abbrev=0 --tags)
prevtag=$(git describe --abbrev=0 --tags "$currenttag^")
from="% \\\\includeonly{chapters\/1"
to="\\\\includeonly{chapters\/"
git checkout $prevtag
for c in $chapters; do
    sed "s/$from/$to$c/" main.tex > "chapter${c}prev.tex";
done
git checkout $currenttag
for c in $chapters; do
    sed "s/$from/$to$c/" main.tex > "chapter${c}.tex";
done
chmod +x latexdiff-so
for c in $chapters; do
    python3 expandmacros.py "chapter${c}prev.tex" > "chapter${c}prevso.tex"
    python3 expandmacros.py "chapter${c}.tex" > "chapter${c}so.tex"
    ./latexdiff-so "chapter${c}prevso.tex" "chapter${c}so.tex" > "chapter${c}diff.tex"
done
