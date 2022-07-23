#!/bin/bash

from="% \\\\includeonly{chapters\/1"
to="\\\\includeonly{chapters\/"
chmod +x latexdiff-so
git checkout $2
rm -r chapters
git checkout chapters
python3 generate_chapters_from_toc.py
sed "s/$from/$to$1/" main.tex > "chapter${1}prev.tex";
python3 expandmacros.py "chapter${1}prev.tex" > "chapter${1}prevso.tex"
git checkout $3
rm -r chapters
git checkout chapters
python3 generate_chapters_from_toc.py
sed "s/$from/$to$1/" main.tex > "chapter${1}.tex";
python3 expandmacros.py "chapter${1}.tex" > "chapter${1}so.tex"
./latexdiff-so "chapter${1}prevso.tex" "chapter${1}so.tex" > "chapter${1}diff.tex"
