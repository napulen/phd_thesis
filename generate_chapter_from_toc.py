import os
import table_of_contents as toc

CHAPTER = 0
SECTION = 1
SUBSECTION = 2
SUBSUBSECTION = 3
ITEMIZE = 4


def formatname(s):
    return "_".join([c.lower() for c in s.split(" ")])


def formattext(s):
    return s.replace("_", " ").replace("*", "").replace("-", "")


def getTOC(contents):
    tocd = {}
    chapter, section, subsec, subsubsec, item = 0, 0, 0, 0, 0
    for line in contents.split("\n"):
        if not line:
            continue
        name = line.strip()
        level = line.count("    ")  # or line.count("\t")
        fname = formatname(name)
        if level == CHAPTER:
            chapter += 1
            section, subsec, subsubsec, item = 0, 0, 0, 0
            tocd[chapter] = {"name": fname}
        if level == SECTION:
            section += 1
            subsec, subsubsec, item = 0, 0, 0
            tocd[chapter][section] = {"name": fname}
        elif level == SUBSECTION:
            subsec += 1
            subsubsec, item = 0, 0
            tocd[chapter][section][subsec] = {"name": fname}
        elif level == SUBSUBSECTION:
            subsubsec += 1
            item = 0
            tocd[chapter][section][subsec][subsubsec] = {"name": fname}
        elif level == ITEMIZE:
            item += 1
            tocd[chapter][section][subsec][subsubsec][item] = {"name": fname}
    return tocd


def treeheader(name, level):
    fname = name.replace("_", " ")
    header = "% Copyright 2021 Néstor Nápoles López\n\n"
    if level == CHAPTER:
        header += f"\\phdchapter{{{fname}}}\n\n"
    else:
        text = formattext(fname)
        if SECTION <= level <= SUBSUBSECTION:
            sec = "sec"
        else:
            sec = "parag"
        nospace = fname.replace(" ", "")
        header += f"""\
This is \\ref{sec}{{{nospace}}},
which introduces the \\titlecap{{{fname}}}.\n
"""
    return header


def registerchild(name, path, level):
    fname = name.replace("_", " ")
    if CHAPTER < level < ITEMIZE:
        trimpath = path.split("/", 3)[-1]
        trimpath = trimpath.replace(".tex", "")
        ind = "\t" * level
        sub = "sub" * (level - 1)
        return f"{ind}\\phd{sub}section{{{fname}}}\\phdinput{{{trimpath}}}\n"
    elif level == ITEMIZE:
        return f"\\phdparagraph{{{fname}}}\n"
    return ""


def treefooter(name, level):
    return ""


def chaptertree(root, rootfd, treename, children, level):
    treedir = os.path.join(root, treename)
    treefile = os.path.join(root, f"{treename}.tex")
    rootfd.write(registerchild(treename, treefile, level))
    if level < ITEMIZE:
        if level < SUBSUBSECTION:
            os.makedirs(treedir, exist_ok=True)
        treefd = open(treefile, "w")
        treefd.write(treeheader(treename, level))
        for child, gc in children.items():
            if child == "name":
                continue
            childname = gc["name"]
            newrootfd = treefd if level == SUBSUBSECTION else rootfd
            chaptertree(treedir, newrootfd, childname, gc, level + 1)
        treefd.write(treefooter(treename, level))
        treefd.close()


if __name__ == "__main__":
    root = "."
    contents = toc.introduction + toc.roman_numerals + toc.background
    tocdict = getTOC(contents)
    for chapter, c in tocdict.items():
        chaptername = c["name"]
        chapterdir = os.path.join(root, "_chapters", chaptername)
        chapterfile = os.path.join(chapterdir, "main.tex")
        os.makedirs(chapterdir, exist_ok=True)
        chapterfd = open(chapterfile, "w")
        chapterfd.write(treeheader(chaptername, CHAPTER))
        for section, s in c.items():
            if section == "name":
                continue
            sectionname = s["name"]
            chaptertree(chapterdir, chapterfd, sectionname, s, SECTION)
        chapterfd.write(treefooter(chaptername, CHAPTER))
        chapterfd.close()
