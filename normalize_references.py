import re
import argparse
import os


def remove_separators(m):
    print(m)
    firstauthor = re.sub(r"[_:\-]", "", m["firstauthor"])
    firstword = re.sub(r"[_:\-]", "", m["firstword"])
    r = f"{m['beginning']}{firstauthor}{m['year']}{firstword}{m['ending']}"
    print(r)
    return f"{m['beginning']}{firstauthor}{m['year']}{firstword}{m['ending']}"


def zotero_to_google_id(m):
    print(m)
    return f"{m['beginning']}{m['firstauthor']}{m['year']}{m['firstword']}{m['ending']}"


def replace_nonenglish_letters(old):
    """Removes common nonenglish characters."""

    new = re.sub(r"[ÀÁÂÃÄÅĀĄ]", "A", old)
    new = re.sub(r"[ÈÉÊËĘȨ]", "E", new)
    new = re.sub(r"[ÌÍÎÏ]", "I", new)
    new = re.sub(r"[ÒÓÔÕÖØ]", "O", new)
    new = re.sub(r"[ÙÚÛÜ]", "U", new)
    new = re.sub(r"[àáâãäåāą]", "a", new)
    new = re.sub(r"[èéêëęȩ]", "e", new)
    new = re.sub(r"[ìíîï]", "i", new)
    new = re.sub(r"[òóôõöø]", "o", new)
    new = re.sub(r"[ùúûü]", "u", new)
    new = re.sub(r"[Æ]", "AE", new)
    new = re.sub(r"[ÇĊ]", "C", new)
    new = re.sub(r"[Ð]", "D", new)
    new = re.sub(r"[Ł]", "l", new)
    new = re.sub(r"[Ñ]", "N", new)
    new = re.sub(r"[æ]", "ae", new)
    new = re.sub(r"[çċ]", "c", new)
    new = re.sub(r"[ð]", "d", new)
    new = re.sub(r"[ł]", "l", new)
    new = re.sub(r"[ñ]", "n", new)
    new = re.sub(r"[ß]", "ss", new)
    return new


def cli():
    parser = argparse.ArgumentParser(
        description="Normalize the format of the references."
    )
    parser.add_argument(
        "file",
        help="a file to normalize",
    )
    return parser.parse_args()


if __name__ == "__main__":
    args = cli()
    zoteroformat = re.compile(
        r"(?P<beginning>\{|,\s?)"
        + r"(?P<firstauthor>[A-Za-z_\-\:]+)_"
        + r"(?P<firstword>[A-Za-z\-\:]+)_"
        + r"(?P<year>\d{2}|\d{4})"
        + r"(?P<ending>\}|,)"
    )
    googleformat = re.compile(
        r"(?P<beginning>\{|,\s?)"
        + r"(?P<firstauthor>[A-Za-z_\-\:]+)"
        + r"(?P<year>\d{2}|\d{4})"
        + r"(?P<firstword>[A-Za-z_\-\:]+)"
        + r"(?P<ending>\}|,)"
    )
    for root, _, filename in os.walk("."):
        latex = [
            f for f in filename if f.endswith(".tex") or f.endswith(".bib")
        ]
        print(root, latex)
        for f in latex:
            with open(os.path.join(root, f)) as fd:
                contents = fd.read()
            contentsEN = replace_nonenglish_letters(contents)
            google = re.sub(zoteroformat, zotero_to_google_id, contentsEN)
            re.sub(googleformat, remove_separators, google)
