import argparse
import os
import re

regex = {
    # matching strings
    "includeonly": re.compile(r"\\includeonly\{(?P<includeonly>[\w/\.-]+)\}"),
    "changecwd": re.compile(r"\\changecwd\{(?P<changecwd>[\w/]+)\}.*"),
    "cwd": re.compile(r".*(?P<cwd>\\cwd).*"),
    "include": re.compile(r".*\\include\{(?P<include>[\\\w/\.-]+)\}"),
    "input": re.compile(r".*\\input\{(?P<input>[\\\w/\.-]+)\}"),
    # substitution strings
    "includesub": re.compile(r"\\include\{[\\\w/\.-]+\}"),
    "changecwdsub": re.compile(r"\\changecwd\{[\w/]+\}"),
    "cwdsub": re.compile(r"\\cwd"),
    "inputsub": re.compile(r"\\input\{[\\\w/\.-]+\}"),
}


def reMatch(regexname, s, default=""):
    m = re.match(regex[regexname], s)
    d = m.groupdict() if m else {}
    return d.get(regexname, default)


def recurse(path, cwd, includeonly):
    mainfd = open(path)
    for line in mainfd.readlines():
        lineout = True
        recursepath = ""
        ret = reMatch("includeonly", line)
        if ret and not includeonly:
            includeonly = ret
            print(f"% includeonly: ", ret)
        ret = reMatch("changecwd", line)
        if ret:
            cwd = ret
            print(f"% changecwd: ", ret)
        ret = reMatch("cwd", line)
        if ret:
            line = re.sub(regex["cwdsub"], cwd, line)
        ret = reMatch("include", line)
        if ret:
            line = re.sub(regex["includesub"], "", line)
            if includeonly and ret != includeonly:
                if ret != includeonly:
                    print(f"% ignoring {ret}")
            else:
                print(f"% recursing over {ret}")
                if not ret.endswith(".tex"):
                    recursepath = f"{ret}.tex"
                else:
                    recursepath = ret
        ret = reMatch("input", line)
        if ret:
            print(f"% recursing over {ret}")
            line = re.sub(regex["inputsub"], "", line)
            if not ret.endswith(".tex"):
                recursepath = f"{ret}.tex"
            else:
                recursepath = ret
        if line and lineout:
            print(line, end="")
        if recursepath:
            recurse(recursepath, cwd, includeonly)
    mainfd.close()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Expand macros manually.")
    parser.add_argument("main_file", help="path to the main LaTeX file.")
    args = parser.parse_args()
    path = os.path.join(args.main_file)
    recurse(path, ".", "")
