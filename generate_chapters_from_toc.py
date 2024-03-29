import os
import shutil
import table_of_contents as toc

CHAPTER = 0
SECTION = 1
SUBSECTION = 2
SUBSUBSECTION = 3
PARAGRAPH = 4

# Use a counter to avoid duplicate \labels
duplicatelabels = {}


def rreplace(s, old, new, count):
    """Like str.replace() but right-to-left."""
    return new.join(s.rsplit(old, count))


class AllegedFile(object):
    """Maybe a file. It may be copied from an existing file instead."""

    _allfiles = []

    def __init__(self, path, mode):
        self._allfiles.append(path)
        self.realpath = rreplace(path, "/_", "/", 1)
        self.fd = open(path, mode)
        if os.path.exists(self.realpath):
            self.replaced = True
            print(f"replaced by real file... {path}")
            with open(self.realpath) as realfd:
                self.fd.write(realfd.read())
        else:
            self.replaced = False
            print(f"generating... {path}")

    def write(self, text):
        if self.replaced:
            return 0
        return self.fd.write(text)

    def close(self):
        self.fd.close()


def formatname(s):
    return "_".join([c for c in s.split(" ")])


def formattext(s):
    return s.replace("_", " ").replace("*", "").replace("-", "")


def getTOC(contents):
    toclist = []
    for line in contents.split("\n"):
        if not line:
            continue
        name = line.strip()
        level = line.count("    ")  # or line.count("\t")
        fname = formatname(name)
        if level == CHAPTER:
            toclist.append((fname, []))
        if level == SECTION:
            _, sections = toclist[-1]
            sections.append((fname, []))
        elif level == SUBSECTION:
            _, subsections = sections[-1]
            subsections.append((fname, []))
        elif level == SUBSUBSECTION:
            _, subsubsections = subsections[-1]
            subsubsections.append((fname, []))
        elif level == PARAGRAPH:
            _, paragraphs = subsubsections[-1]
            paragraphs.append((fname, []))
    return toclist


def treeheader(name, level):
    fname = name.replace("_", " ")
    header = "% Copyright 2022 Néstor Nápoles López\n\n"
    if level == CHAPTER:
        header += f"""\
\\phdchapter{{{fname}}}

\\input{{\\cwd/_chapter_intro}}
"""
    else:
        nospace = fname.replace(" ", "")
        sub = "sub" * (level - 1)
        header += f"""\
This is \\ref{sub}sec{{{nospace}}},
which introduces the {fname}.\n
"""
    return header


def chapterintroheader(name):
    fname = name.replace("_", "")
    header = f"""\
% Copyright 2022 Néstor Nápoles López

This is the introduction to \\refchap{{{fname}}},
which goes before any of its sections.
"""
    return header


def checkduplicate(name, level):
    label = (name, level)
    if label in duplicatelabels:
        print(f"WARNING: label of {label} will collide with another one!")
    duplicatelabels[label] = True


def registerchild(name, path, level):
    fname = name.replace("_", " ")
    checkduplicate(name, level)
    if level == PARAGRAPH:
        return f"\\phdparagraph{{{fname}}}\n"
    trimpath = path.split("/", 3)[-1]
    trimpath = trimpath.replace(".tex", "")
    ind = "\t" * level
    sub = "sub" * (level - 1)
    return f"{ind}\\phd{sub}section{{{fname}}}\\input{{\\cwd/{trimpath}}}\n"


def treefooter(name, level):
    return ""


def chaptertree(root, rootfd, treename, children, level):
    treedir = os.path.join(root, treename)
    treefile = os.path.join(root, f"_{treename}.tex")
    rootfd.write(registerchild(treename, treefile, level))
    if level < PARAGRAPH:
        if level < SUBSUBSECTION and children:
            os.makedirs(treedir, exist_ok=True)
        treefd = AllegedFile(treefile, "w")
        treefd.write(treeheader(treename, level))
        for child, grandchildren in children:
            newrootfd = treefd if level == SUBSUBSECTION else rootfd
            chaptertree(treedir, newrootfd, child, grandchildren, level + 1)
        treefd.write(treefooter(treename, level))
        treefd.close()


def getUnusedFiles(root):
    usedfiles = AllegedFile._allfiles
    unusedfiles = []
    for root, _, files in os.walk(os.path.join(root, "chapters")):
        if "figures" in root or "tables" in root:
            continue
        for f in files:
            if not f.startswith("_") and f.endswith(".tex"):
                path = os.path.join(root, f)
                if os.path.join(root, f"_{f}") not in usedfiles:
                    unusedfiles.append(path)
    return unusedfiles


if __name__ == "__main__":
    root = "."
    contents = (
        toc.introduction
        + toc.roman_numerals
        + toc.background
        + toc.data_acquisition
        + toc.model_design
        + toc.experimental_evaluation
        + toc.conclusions
        + toc.appendix
    )
    toclist = getTOC(contents)
    for chapter, sections in toclist:
        chapternumber, chaptername = chapter.split("-", 1)
        chapterdir = os.path.join(root, "chapters", chapternumber)
        os.makedirs(chapterdir, exist_ok=True)
        chapterfigures = os.path.join(chapterdir, "figures")
        os.makedirs(chapterfigures, exist_ok=True)
        shutil.copy("placeholder.png", chapterfigures)
        chapterintro = os.path.join(chapterdir, "_chapter_intro.tex")
        introfd = AllegedFile(chapterintro, "w")
        introfd.write(chapterintroheader(chaptername))
        introfd.close()
        chaptermain = os.path.join(chapterdir, "_main.tex")
        chapterfd = AllegedFile(chaptermain, "w")
        chapterfd.write(treeheader(chaptername, CHAPTER))
        for section, subsections in sections:
            chaptertree(chapterdir, chapterfd, section, subsections, SECTION)
        chapterfd.write(treefooter(chaptername, CHAPTER))
        chapterfd.close()
    unused = getUnusedFiles(root)
    if unused:
        warning = """\
Warning: The following files exist in the chapters directory, \
but do not seem to exist in the table of contents"""
        print(warning)
        print("\n".join(unused))
