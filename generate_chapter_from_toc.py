import os

# Needs to be tab (\t) indented, otherwise it won't work
contents = """
Background
    Music Representation
        Types of representation
        Symbolic music formats
            Humdrum(**kern)
            MEI
            MIDI
            MusicXML
            MNX
            Others
        Symbolic vs audio representations
    Deep neural networks
        Feed forward networks
        Convolutional neural networks
        Recurrent neural networks
            LSTM
            GRU
        Transformer networks
    Music Information Retrieval
        Key estimation
            Global-key estimation
            Local-key estimation
                Local key
                Modulation
                Tonicization
            Perception of key
            Ambiguity of key
            Inter-annotator agreement
            MIR models
        Chord recognition
            Chord syntax
            Chord vocabulary
            MIR algorithms
            Perception of chords
            Ambiguity of chords
            Inter-annotator agreement
            MIR models
        Automatic Roman numeral analysis
            Beyond chords and keys
            Grammar-based approaches
            Reductionist approaches
            MIR models
"""

root = ""

CHAPTER = 0
SECTION = 1
SUBSECTION = 2
SUBSUBSECTION = 3
ITEMIZE = 4


def formatname(s):
    return "_".join([c.lower() for c in s.split(" ")])


def getTOC():
    toc = {}
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
            toc[chapter] = {"name": fname}
        if level == SECTION:
            section += 1
            subsec, subsubsec, item = 0, 0, 0
            toc[chapter][section] = {"name": fname}
        elif level == SUBSECTION:
            subsec += 1
            subsubsec, item = 0, 0
            toc[chapter][section][subsec] = {"name": fname}
        elif level == SUBSUBSECTION:
            subsubsec += 1
            item = 0
            toc[chapter][section][subsec][subsubsec] = {"name": fname}
        elif level == ITEMIZE:
            item += 1
            toc[chapter][section][subsec][subsubsec][item] = {"name": fname}
    return toc


def treeheader(name, level):
    fname = name.replace("_", " ")
    if level == CHAPTER:
        return f"\\phdchapter{{{fname}}}\n\n"
    else:
        return f"{fname}\n"


def registerchild(name, path, level):
    fname = name.replace("_", " ")
    if CHAPTER < level < ITEMIZE:
        trimpath = path.split("/", 2)[-1]
        trimpath = trimpath.replace(".tex", "")
        ind = "\t" * level
        sub = "sub" * (level - 1)
        return f"{ind}\\phd{sub}section{{{fname}}}\\phdinput{{{trimpath}}}\n"
    elif level == ITEMIZE:
        return f"\\paragraph{{{fname}}}\n"
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
    toc = getTOC()
    for chapter, c in toc.items():
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


# toc = getTOC()
# for chapter, c in toc.items():
#     chaptername = c["name"]
#     chapterdir = os.path.join(root, "_chapters", chaptername)
#     chapterfile = os.path.join(chapterdir, "main.tex")
#     os.makedirs(chapterdir, exist_ok=True)
#     chapterfd = open(chapterfile, "w")
#     chapterfd.write(chapterheader(chaptername))
#     for section, s in c.items():
#         if section == "name":
#             continue
#         sectionname = s["name"]
#         sectiondir = os.path.join(chapterdir, f"{sectionname}")
#         os.makedirs(sectiondir, exist_ok=True)
#         sectionfile = os.path.join(chapterdir, f"{sectionname}_intro.tex")
#         sectionfd = open(sectionfile, "w")
#         sectionfd.write(sectionheader(sectionname))
#         sectionfd.close()
#         chapterfd.write(chaptersection(sectionname, sectionfile))
#         for subsection, ss in s.items():
#             if subsection == "name":
#                 continue
#             subsectionname = ss["name"]
#             subsectiondir = os.path.join(sectiondir, f"{subsectionname}")
#             os.makedirs(subsectiondir, exist_ok=True)
#             subsectionfile = os.path.join(sectiondir, f"{subsectionname}.tex")
#             subsectionfd = open(subsectionfile, "w")
#             subsectionfd.write(subsectionheader(subsectionname))
#             subsectionfd.close()
#             chapterfd.write(chaptersubsection(subsectionname, subsectionfile))
#             for subsubsec, sss in ss.items():
#                 if subsubsec == "name":
#                     continue
#                 subsubsectionname = sss["name"]
#                 subsubsectionfile = os.path.join(
#                     subsectiondir, f"{subsubsectionname}.tex"
#                 )
#                 subsubsectionfd = open(subsubsectionfile, "w")
#                 subsubsectionfd.write(subsubsectionheader(subsubsectionname))
#                 subsubsectionfd.close()
#                 chapterfd.write(
#                     chaptersubsubsection(subsubsectionname, subsubsectionfile)
#                 )
#     chapterfd.close()
