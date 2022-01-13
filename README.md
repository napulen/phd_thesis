# Automatic Roman numeral analysis in symbolic music representations

**Author**: Néstor Nápoles López

**Supervisor**: Ichiro Fujinaga

**Co-supervisor**: Jonathan Wild

> Starting from `v35`, the `chapters/` folder is mostly auto-generated by `generate_chapters_from_toc.py`. This allows me to commit only the files that have been modified explicitly, filling up everything else in the thesis with auto-generated files.

Each chapter is a folder within the `chapters/` folder.
Each chapter contains all of its figures and tables.
However, because of the use of custom macros, chapters are **not** standalone documents.
They always need to be compiled from the `main.tex` file.

By default, the main file (`main.tex`) compiles all the chapters and puts them together into a full document.

Individual chapters can be compiled if the line

```latex
\includeonly{chapters/1/main}
```

is uncommented from the `main.tex` file, where `1` should be replaced with the number of the chapter to be compiled.

The document is laid out automatically thanks to different macros that automate some operations (e.g., inserting a figure, starting a section, etc).

The custom macros include:

- `\cwd`: a workaround for relative paths within chapters, so that `\input` commands can be used with relative paths
- `\phdchapter`: create a new chapter, `\label` it automatically
- `\phdsection`: create a new section, `\label` it automatically
- `\phdsubsection`: create a new subsection, `\label` it automatically
- `\phdsubsubsection`: create a new subsubsection, `\label` it automatically
- `\phdfigure`: create a new figure, `\caption` it automatically
- `\refchap`: use `hyperref` to reference a chapter
- `\refsec`: use `hyperref` to reference a section
- `\refsubsec`: use `hyperref` to reference a subsection
- `\refsubsubsec`: use `hyperref` to reference a subsubsection
- `\reffig`: use `hyperref` to reference a figure
- `\reftab`: use `hyperref` to reference a table
- `\refeq`: use `hyperref` to reference an equation

These are all located in the `phdmacros.sty` file.

## Normalizing reference identifiers in bibtex

Often it'll be necessary to move into different formats of references.
I like the convention adopted by Google scholar for publication identifiers: `<firstauthor><year><firstword>`

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

## Committing files and auto-generating the rest of the thesis layout

The workflow to write the thesis is as follows:

1. Work on a table of contents (`table_of_contents.py`) that will serve as the main structure of the thesis document
2. Run `python3 generate_chapters_from_toc.py` to generate all the latex structure (i.e., within the `chapters/` folder)
3. Modify the files with their content, changing their names from `_filename.tex` to `filename.tex`. This will indicate to `generate_chapters_from_toc.py` that this file should not be auto-generated.
4. Run `python3 generate_chapters_from_toc.py` to update the structure of the thesis with the new changes
5. Commit and push the changes
6. When a new version is ready, use `git tag vXX` to create the new tag
7. Github actions takes care of compiling the thesis and diffing this version against the previous tag
8. Repeat 3--7 until thesis is complete
9. Hopefully graduate.

## Convenience scripts

In order to save some time, I have been using scripts to quickly update my references and generate a pdf.

This is `refs.sh` which just runs the reference normalization script

```bash
#!/bin/bash

python3 normalize_references.py -v --modify
```

This is `flush.sh` which deletes old `chapters` and generates a new one.

```bash
#!/bin/bash

rm -R chapters
git checkout chapters
python3 generate_chapters_from_toc.py
```

> Note that any changes need to be committed before generating the new PDF, otherwise they'll be gone.
