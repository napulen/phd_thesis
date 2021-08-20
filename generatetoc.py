contents = """
1 Introduction
1.1 Motivation
1.2 Thesis structure
2 Background
2.1 Music theory
2.1.1 A brief history of Roman numeral analysis
2.1.2 Digitization of Roman numeral annotations
2.2 Music Information Retrieval
2.2.1 Automatic chord and key estimation
2.2.2 Multitask tonal analysis
3 Data acquisition and preparation
3.1 Available datasets
3.1.1 Annotated Beethoven Corpus (ABC)
3.1.2 Beethoven Piano Sonatas (BPS)
3.1.3 Haydn “Sun” String Quartets (HaydnSun)
3.1.4 Mozart Piano Sonatas (MPS)
3.1.5 Theme and Variation Encodings with Roman Numerals (TAVERN)
3.1.6 Schubert Winterreise (SW)
3.1.7 When-in-Rome (WiR)
3.2 Data preparation
3.2.1 Aligning a score and an annotation file
3.2.2 Standardizing the notation between datasets
3.3 Data augmentation
3.3.1 Synthesis and artificial texturization of scores
4 Model design
4.1 Inputs
4.1.1 Encoding pitch spelling
4.2 The bass and chroma convolutional blocks
4.3 Dense and recurrent layers
4.4 Multitask learning configurations
4.4.1 Six conventional tonal tasks
4.4.2 Five additional tonal tasks
5 Experimental evaluation
5.1 Training procedure
5.2 Hyperparameters
5.2.1 Training epochs and weight selection
5.2.2 Learning schedule and learning rate
5.3 Evaluation procedure
5.4 Results
5.5 Discussion
6 Conclusions"""


def formatsection(s):
    return s.replace(".", "_")

def formatname(s):
    return '_'.join([c.lower() for c in s.split(" ")])

for line in contents.split("\n")[1:]:
    # print(line)
    section, name = line.split(" ", 1)
    level = section.count(".")
    fsection = formatsection(section)
    fname = formatname(name)
    print(level, fsection, fname)
