import re
import argparse
import logging
import os
import sys

NONENGLISH = (
    r"ÀÁÂÃÄÅĀĄÈÉÊËĘȨÌÍÎÏÒÓÔÕÖØÙÚÛÜàáâãäåāąèéêëęȩìíîïòóôõöøùúûüÆÇĊÐŁÑæçċðłñß"
)

ZOTEROLIKE = re.compile(
    r"(?P<beginning>\{|,?\s+)"
    + r"(?P<firstauthor>[A-Za-z_:"
    + NONENGLISH
    + r"-]+)_"
    + r"(?P<firstword>[A-Za-z0-9:"
    + NONENGLISH
    + r"-]+)_"
    + r"(?P<year>\d{2}|\d{4})"
    + r"(?P<ending>\}|,)"
)

GOOGLELIKE = re.compile(
    r"(?P<beginning>\{|,?\s+)"
    + r"(?P<firstauthor>[A-Za-z_:"
    + NONENGLISH
    + r"-]+)"
    + r"(?P<year>\d{2}|\d{4})"
    + r"(?P<firstword>[A-Za-z_:"
    + NONENGLISH
    + r"-]+)"
    + r"(?P<ending>\}|,)"
)


def remove_separators(m):
    original = "".join(m.groups())
    if (
        m["firstauthor"].startswith("tab:")
        or m["firstauthor"].startswith("fig:")
        or m["firstauthor"].startswith("sec:")
    ):
        return original
    firstauthor = replace_nonenglish_letters(m["firstauthor"]).lower()
    firstword = replace_nonenglish_letters(m["firstword"]).lower()
    firstauthor = re.sub(r"[_:\-]", "", firstauthor)
    firstword = re.sub(r"[_:\-]", "", firstword)
    ret = f"{m['beginning']}{firstauthor}{m['year']}{firstword}{m['ending']}"
    if ret != original:
        logging.info(f"\t\t{original} -> {ret}")
    return ret


def zotero_to_google_id(m):
    original = "".join(m.groups())
    ret = f"{m['beginning']}{m['firstauthor']}{m['year']}{m['firstword']}{m['ending']}"
    logging.info(f"\t\t{original} -> {ret}")
    return ret


def replace_nonenglish_letters(old):
    """Replaces common nonenglish characters."""

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
    new = re.sub(r"[Ł]", "L", new)
    new = re.sub(r"[Ñ]", "N", new)
    new = re.sub(r"[æ]", "ae", new)
    new = re.sub(r"[çċ]", "c", new)
    new = re.sub(r"[ð]", "d", new)
    new = re.sub(r"[ł]", "l", new)
    new = re.sub(r"[ñ]", "n", new)
    new = re.sub(r"[ß]", "ss", new)
    return new


def sort(data):
    # end the file with exactly one trailing newline
    data = data.strip() + "\n"
    entries = data.split("},\n}\n")
    ids = [x.split("{", 1)[1].split(",", 1)[0] for x in entries if x]
    sortbyid = sorted(zip(entries, ids), key=lambda x: x[1])
    sortedentries = [x[0] for x in sortbyid]
    sorteddata = "},\n}\n".join(sortedentries) + "},\n}\n"
    return sorteddata


def run(modify=False, tex=False, bib=True, verbose=True):
    loglevel = logging.INFO if verbose else logging.WARNING
    logging.basicConfig(stream=sys.stdout, level=loglevel)
    for root, _, filenames in os.walk("."):
        for f in filenames:
            _, ext = os.path.splitext(f)
            if ext not in [".tex", ".bib"]:
                continue
            if ext == ".tex" and not tex:
                continue
            if ext == ".bib" and not bib:
                continue
            path = os.path.join(root, f)
            logging.info(path)
            with open(path) as fd:
                contents = fd.read()
            logging.info("\tTurning zotero-like ids into google-scholar-like")
            google = re.sub(ZOTEROLIKE, zotero_to_google_id, contents)
            # normalize everything else (dashes, colons, compound names, etc.)
            logging.info("\tNormalizing dashes, colons, etc. in identifiers")
            subs = re.sub(GOOGLELIKE, remove_separators, google)
            if f.endswith(".bib"):
                logging.info("\tSorting the bibtex file")
                subs = sort(subs)
            if modify:
                with open(path, "w") as fd:
                    fd.write(subs)
    if not modify:
        logging.warning("Dry-run mode. All suggestions were ignored.")
        logging.warning("Add --modify to make changes permanent.")


def cli():
    parser = argparse.ArgumentParser(
        description="Normalize the format of the references."
    )
    parser.add_argument(
        "--modify",
        action="store_true",
        help="update the changes in the files (CAREFUL!)",
    )
    parser.add_argument(
        "-v", "--verbose", action="store_true", help="verbose output"
    )
    parser.add_argument(
        "-t", "--tex", action="store_true", help="Process .tex files"
    )
    parser.add_argument(
        "-b", "--bib", action="store_true", help="Process .bib files"
    )
    return parser


if __name__ == "__main__":
    parser = cli()
    args = parser.parse_args()
    run(**vars(args))
