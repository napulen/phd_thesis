# Automatic Roman numeral analysis in symbolic music representations

Author: Néstor Nápoles López. Supervisor: Ichiro Fujinaga

Each chapter is a standalone document in the `chapters/` folder. Each chapter contains all of its figures as well.

The main file (`main.tex`) compiles each chapter and puts them together into a full document.

Individual chapters can be compiled if

```latex
\def\compilechapter{2}
```

is set up. Otherwise, the full document will be compiled.

The document is laid out automatically thanks to different macros that automate some operations (e.g., inserting a figure, starting a section, etc).

The custom macros include:

- `\phdinput`: a replacement of `\input` used to insert a `.tex` document inside a chapter
- `\phdchapter`: create a new chapter, `\label` it automatically
- `\phdsection`: create a new section, `\label` it automatically
- `\phdsubsection`: create a new subsection, `\label` it automatically
- `\phdsubsubsection`: create a new subsubsection, `\label` it automatically
- `\phdfigure`: create a new figure, `\caption` it automatically
- `\refchap`: use `hyperref` to reference a chapter
- `\refsec`: use `hyperref` to reference a section
- `\reffig`: use `hyperref` to reference a figure
- `\reftab`: use `hyperref` to reference a table
- `\refeq`: use `hyperref` to reference an equation


## Normalizing reference identifiers in bibtex

Often it'll be necessary to move into different formats of references.
I like the convention adoped by Google scholar for publication identifiers: `<firstauthor><year><firstword>`

The script `normalize_references.py` will automatically navigate through the `.tex` and `.bib` files to standardize
every reference with this convention.

```
usage: normalize_references.py [-h] [--modify] [-v]

Normalize the format of the references.

optional arguments:
  -h, --help  show this help message and exit
  --modify    update the changes in the files (CAREFUL!)
  -v          verbose output
```

If run as

```python
python3 normalize_references.py -v
```

the script will make suggestions (i.e., *dry-run* mode). If run as
```python
python3 normalize_references.py -v --modify
```

the script will proceed with the changes to all files, according to the reference format.
