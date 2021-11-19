
# What's important in an introduction?
introduction = """
Introduction
    Motivation
    Thesis structure
"""

roman_numerals = """
Introduction to Roman numeral analysis
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
Background
    Music Representation
        Types of representation
        Symbolic music formats
            Humdrum(**kern)
                Origin
                Applications
            MEI
                Origin
                Applications
            MIDI
                Origin
                Applications
            MusicXML
                Origin
                Applications
            MNX
                Origin
                Applications
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
            Task description
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
            Task description
            Chord syntax
            Chord vocabulary
            MIR algorithms
            Perception of chords
            Ambiguity of chords
            Inter-annotator agreement
            MIR models
        Automatic pitch spelling
            Task description
            Relationship to key and chord estimation
            Relationship to Roman numeral analysis
            MIR models
        Automatic Roman numeral analysis
            Task description
                Beyond chords and keys
            Grammar-based approaches
            Reductionist approaches
            MIR models
"""

data_acquisition = """
Data acquisition and preparation
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
            Description
                Neuwirth et al. (2018)
            Format
                DCML standard
            Revisions
                Version 1
                Version 2
            Statistical analysis
                Number of annotations
                Chord distribution
                Global key distribution
                Modulation distribution
                Tonicization distribution
        Beethoven Piano Sonatas (BPS)
            Description
                Chen and Su (2018)
            Format
                Tabular format
                Limitations of format
            Accompanying scores
                No scores provided
                Aligning scores is not trivial
            Statistical analysis
                Number of annotations
                Chord distribution
                Global key distribution
                Modulation distribution
                Tonicization distribution
        Haydn ``Sun'' String Quartets (HaydnSun)
            Description
                N\'apoles L\'opez (2017)
            Format
                Humdrum(**harm)
            Statistical analysis
                Number of annotations
                Chord distribution
                Global key distribution
                Modulation distribution
                Tonicization distribution
        Mozart Piano Sonatas (MPS)
            Description
                Hentschel et al. (2021)
            Format
                DCML standard
            Statistical analysis
                Number of annotations
                Chord distribution
                Global key distribution
                Modulation distribution
                Tonicization distribution
        Theme and Variation Encodings with Roman numerals (TAVERN)
            Description
            Format
            Statistical analysis
                Number of annotations
                Chord distribution
                Global key distribution
                Modulation distribution
                Tonicization distribution
        Schubert Winterreise (SW)
            Description
                Weiss et al. (2021)
            Format
                Borderline not Roman numeral analysis
                Tabular format
            Statistical analysis
                Number of annotations
                Chord distribution
                Global key distribution
                Modulation distribution
                Tonicization distribution
        When-in-Rome (WiR)
            Description
                Tymoczko et al. (2019)
                Gotham et al. (2021)
            Format
                RomanText
            Converted corpora
                TAVERN
                HaydnSun
                ABC
            Original corpora
                OpenScore Lieder
                Well-Tempered Clavier
                Bach Chorales
                Monteverdi Madrigals
                Miscellaneous pieces
            Statistical analysis
                Number of annotations
                Chord distribution
                Global key distribution
                Modulation distribution
                Tonicization distribution
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
Model design
    Inputs
        Encoding pitch spelling
    The bass and chroma convolutional blocks
    Dense and recurrent layers
    Multitask learning configurations
        Six conventional tasks
        Five additional tasks
"""

experimental_evaluation = """
Experimental evaluation
    Training procedure
    Hyperparameters
        Training epochs and weight selection
        Learning schedule and learning rate
    Evaluation procedure
    Results
    Discussion
"""

conclusions = """
Conclusions
    Summary
    Discussion
    Future work
"""
