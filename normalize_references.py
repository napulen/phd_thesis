import re
import argparse
import logging
import os
import sys

ZOTEROLIKE = re.compile(
    r"(?P<beginning>\{|,\s?)"
    + r"(?P<firstauthor>[A-Za-z_\-\:]+)_"
    + r"(?P<firstword>[A-Za-z\-\:]+)_"
    + r"(?P<year>\d{2}|\d{4})"
    + r"(?P<ending>\}|,)"
)

GOOGLELIKE = re.compile(
    r"(?P<beginning>\{|,\s?)"
    + r"(?P<firstauthor>[A-Za-z_\-\:]+)"
    + r"(?P<year>\d{2}|\d{4})"
    + r"(?P<firstword>[A-Za-z_\-\:]+)"
    + r"(?P<ending>\}|,)"
)


def remove_separators(m):
    original = ''.join(m.groups())
    if (
        m["firstauthor"].startswith("tab:")
        or m["firstauthor"].startswith("fig:")
        or m["firstauthor"].startswith("sec:")
    ):
        return original
    firstauthor = re.sub(r"[_:\-]", "", m["firstauthor"])
    firstword = re.sub(r"[_:\-]", "", m["firstword"])
    ret = f"{m['beginning']}{firstauthor}{m['year']}{firstword}{m['ending']}"
    if ret != original:
        logging.info(f"\t\t{original} -> {ret}")
    return ret

def zotero_to_google_id(m):
    original = ''.join(m.groups())
    ret = f"{m['beginning']}{m['firstauthor']}{m['year']}{m['firstword']}{m['ending']}"
    logging.info(f"\t\t{original} -> {ret}")
    return ret


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
        "--modify",
        action="store_true",
        help="update the changes in the files (CAREFUL!)",
    )
    parser.add_argument("-v", action="store_true", help="verbose output")
    return parser.parse_args()


if __name__ == "__main__":
    args = cli()
    loglevel = logging.INFO if args.v else logging.WARNING
    logging.basicConfig(level=loglevel)
    for root, _, filenames in os.walk("."):
        for f in filenames:
            if not f.endswith(".tex") and not f.endswith(".bib"):
                # logging.info(f"Ignoring file {f}")
                continue
            path = os.path.join(root, f)
            logging.info(path)
            with open(path) as fd:
                contents = fd.read()
            # homogenize non-English names and words
            logging.info("\tHomogenizing non-English characters")
            contentsEN = replace_nonenglish_letters(contents)
            # turn all zotero-like identifiers into google-scholar-like ones
            logging.info("\tTurning zotero-like ids into google-scholar-like")
            google = re.sub(ZOTEROLIKE, zotero_to_google_id, contentsEN)
            # normalize everything else (dashes, colons, compound names, etc.)
            logging.info("\tNormalizing dashes, colons, etc. in identifiers")
            subs = re.sub(GOOGLELIKE, remove_separators, google)
            if args.modify:
                with open(path, "w") as fd:
                    fd.write(subs)
    if not args.modify:
        logging.warning("Dry-run mode. All suggestions were ignored.")
        logging.warning("Add --modify to make changes permanent.")
