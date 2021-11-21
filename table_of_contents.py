
# What's important in an introduction?
introduction = """
1-Introduction
    Motivation
    Thesis structure
"""

roman_numerals = """
2-Introduction to Roman numeral analysis
    Roman numeral analysis and chord labels
    A brief history of roman numeral analysis
        The Roman numeral timeline
    Digitization of roman numeral annotations
        The standard syntax of Roman numeral analysis
            The lack of a standard
            The need for a standard in digital representations
        Digital standards
            Humdrum(**harm)
            RomanText
            The DCML standard
            Harmalysis
        Current challenges
"""

background = """
3-Background
    Music Representation
        Types of representation
        Symbolic music formats
            Humdrum(**kern)
                Origin of **kern
                Applications of **kern
            MEI
                Origin of MEI
                Applications of MEI
            MIDI
                Origin of MIDI
                Applications of MIDI
            MusicXML
                Origin of MusicXML
                Applications of MusicXML
            MNX
                Origin of MNX
                Applications of MNX
            Others
                Lilypond
                ABC
                Plain-and-easy
        Symbolic vs audio representations
            Chroma-based features
            Pitch spelling
    Deep neural networks
        Feed forward networks
        Convolutional neural networks
        Recurrent neural networks
            LSTM
            GRU
        Transformer networks
    Music Information Retrieval
        Key estimation
            The key-estimation task
            Global-key estimation
            Local-key estimation
                Local key
                Modulation
                Tonicization
            Perception of key
            Ambiguity of key annotations
            Key inter-annotator agreement
            Key-estimation models
        Chord recognition
            The chord recognition task
            Chord syntax
            Chord vocabulary
            Perception of chords
            Ambiguity of chord annotations
            Chord inter-annotator agreement
            Chord recognition models
        Automatic pitch spelling
            The MIDI pitch-spelling task
            Relationship to key and chord estimation
            Relationship to Roman numeral analysis
            Pitch-spelling models
        Automatic Roman numeral analysis
            The Roman numeral analysis task
                Beyond chords and keys
            Grammar-based approaches
            Reductionist approaches
            Roman numeral analysis models
"""

data_acquisition = """
4-Data acquisition and preparation
    Roman numeral analysis datasets
        Definition
        Other types of datasets
            Chord label datasets
                McGill Billboard
            Figured bass datasets
                Ju 2020
            Key estimation datasets
                Giantsteps Key
                Giantsteps MTG Key
    Available datasets
        Annotated Beethoven Corpus (ABC)
            Description of ABC
                Neuwirth et al. (2018)
            Format of ABC
                DCML standard in ABC
            Revisions
                Version 1
                Version 2
            Statistical analysis of ABC
                Number of annotations in ABC
                Chord distributions in ABC
                Global key distribution in ABC
                Modulation distribution in ABC
                Tonicization distribution in ABC
        Beethoven Piano Sonatas (BPS)
            Description of BPS
                Chen and Su (2018)
            Format of BPS
                Tabular format of BPS
                Limitations of format
            Accompanying scores
                No scores provided
                Aligning scores is not trivial
            Statistical analysis of BPS
                Number of annotations in BPS
                Chord distribution in BPS
                Global key distribution in BPs
                Modulation distribution in BPS
                Tonicization distribution in BPS
        Haydn ``Sun'' String Quartets (HaydnSun)
            Description of HaydnSun
                N\'apoles L\'opez (2017)
            Format of HaydnSun
                Humdrum(**harm) in HaydnSun
            Statistical analysis of HaydnSun
                Number of annotations in HaydnSun
                Chord distribution in HaydnSun
                Global key distribution in HaydnSun
                Modulation distribution in HaydnSun
                Tonicization distribution in HaydnSun
        Mozart Piano Sonatas (MPS)
            Description of MPS
                Hentschel et al. (2021)
            Format of MPS
                DCML standard in MPS
            Statistical analysis of MPS
                Number of annotations in MPS
                Chord distribution in MPS
                Global key distribution in MPS
                Modulation distribution in MPS
                Tonicization distribution in MPS
        Theme and Variation Encodings with Roman numerals (TAVERN)
            Description of TAVERN
            Format of TAVERN
                Humdrum(**harm) in TAVERN
            Statistical analysis of TAVERN
                Number of annotations in TAVERN
                Chord distribution in TAVERN
                Global key distribution in TAVERN
                Modulation distribution in TAVERN
                Tonicization distribution in TAVERN
        Schubert Winterreise (SW)
            Description of SW
                Weiss et al. (2021)
            Format of SW
                Borderline not Roman numeral analysis
                Tabular format of SW
            Statistical analysis of SW
                Number of annotations in SW
                Chord distribution in SW
                Global key distribution in SW
                Modulation distribution in SW
                Tonicization distribution in SW
        When-in-Rome (WiR)
            Description of WiR
                Tymoczko et al. (2019)
                Gotham et al. (2021)
            Format of WiR
                RomanText
            Converted corpora
                TAVERN
                HaydnSun
                Converted ABC
            Original corpora
                OpenScore Lieder
                Well-Tempered Clavier
                Bach Chorales
                Monteverdi Madrigals
                Miscellaneous pieces
            Statistical analysis of WiR
                Number of annotations of WiR
                Chord distribution of WiR
                Global key distribution of WiR
                Modulation distribution of WiR
                Tonicization distribution of WiR
    Data preparation
        Problems of diverse datasets
            Examples of misalignment in BPS
            Mislabeled annotations
            Different spellings
            Diverging chord vocabularies
        Data-curation tools
            Alignment of scores
            Verifying pitch content
        Aligning a score and an annotation file
        Standardizing the notation between datasets
    Data augmentation
        Synthesis of artificial examples
            Texturization patterns
                Alberti bass
                Bass split
                Syncopation
        Retrieving tonal tasks from Roman numeral annotations
"""

model_design = """
5-Model design
    Inputs
        Encoding pitch spelling
    The bass and chroma convolutional blocks
    Dense and recurrent layers
    Multitask learning configurations
        Six conventional tasks
        Five additional tasks
"""

experimental_evaluation = """
6-Experimental evaluation
    Training procedure
    Hyperparameters
        Training epochs and weight selection
        Learning schedule and learning rate
    Evaluation procedure
    Results
    Discussion
"""

conclusions = """
7-Conclusions
    Summary
    Future work
"""
