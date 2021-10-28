from os import replace
import re
import argparse


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


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Normalize the format of the references."
    )
    parser.add_argument(
        "file",
        help="a file to normalize",
    )
    args = parser.parse_args()
    zotero = (
        r"(?P<beginning>\{|,\s?)"
        + r"(?P<firstauthor>[A-Za-z_\-\:]+)_"
        + r"(?P<firstword>[A-Za-z\-\:]+)_"
        + r"(?P<year>\d+)"
        + r"(?P<ending>\}|,)"
    )
    google = (
        r"(?P<beginning>\{|,\s?)"
        + r"(?P<firstauthor>[A-Za-z_\-\:]+)"
        + r"(?P<year>\d+)"
        + r"(?P<firstword>[A-Za-z_\-\:]+)"
        + r"(?P<ending>\}|,)"
    )
    with open(args.file) as fd:
        contents = fd.read()
    contentsEN = replace_nonenglish_letters(contents)
    googleformat = re.sub(zotero, zotero_to_google_id, contentsEN)
    re.sub(google, remove_separators, googleformat)
