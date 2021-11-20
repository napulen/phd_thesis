import os
import table_of_contents as toc

CHAPTER = 0
SECTION = 1
SUBSECTION = 2
SUBSUBSECTION = 3
ITEMIZE = 4

# Use a counter to avoid \labels with the same name
duplicatesections = {}


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
        header += f"\\phdchapter{{{fname}}}\n\n\\phdinput{{chapter_intro}}\n"
    else:
        nospace = fname.replace(" ", "")
        sub = "sub" * (level - 1)
        header += f"""\
This is \\ref{sub}sec{{{nospace}}},
which introduces the {{{fname}}}.\n
"""
    return header


def chapterintroheader(name):
    fname = name.replace("_", "")
    header = f"""\
% Copyright 2021 Néstor Nápoles López

This is the introduction to \\refchap{{{fname}}},
which goes before any of its sections.
"""
    return header


def disambiguateduplicates(name, level):
    identifier = (name, level)
    if identifier not in duplicatesections:
        duplicatesections[identifier] = 1
        return ""
    index = duplicatesections[identifier]
    duplicatesections[identifier] += 1
    return str(index)


def registerchild(name, path, level):
    fname = name.replace("_", " ")
    idx = disambiguateduplicates(name, level)
    if CHAPTER < level < ITEMIZE:
        trimpath = path.split("/", 3)[-1]
        trimpath = trimpath.replace(".tex", "")
        ind = "\t" * level
        sub = "sub" * (level - 1)
        return (
            f"{ind}\\phd{sub}section{{{fname}{idx}}}\\phdinput{{{trimpath}}}\n"
        )
    elif level == ITEMIZE:
        return f"\\phdparagraph{{{fname}{idx}}}\n"
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
    contents = (
        toc.introduction
        + toc.roman_numerals
        + toc.background
        + toc.data_acquisition
        + toc.model_design
        + toc.experimental_evaluation
        + toc.conclusions
    )
    tocdict = getTOC(contents)
    for chapter, c in tocdict.items():
        chaptername = c["name"]
        chapterdir = os.path.join(root, "_chapters", chaptername)
        os.makedirs(chapterdir, exist_ok=True)
        chapterintro = os.path.join(chapterdir, "chapter_intro.tex")
        with open(chapterintro, "w") as introfd:
            introfd.write(chapterintroheader(chaptername))
        chaptermain = os.path.join(chapterdir, "main.tex")
        chapterfd = open(chaptermain, "w")
        chapterfd.write(treeheader(chaptername, CHAPTER))
        for section, s in c.items():
            if section == "name":
                continue
            sectionname = s["name"]
            chaptertree(chapterdir, chapterfd, sectionname, s, SECTION)
        chapterfd.write(treefooter(chaptername, CHAPTER))
        chapterfd.close()
