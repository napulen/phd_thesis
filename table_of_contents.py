introduction = """
1-Introduction
    Motivation
        Musical analysis
            Why Analyze Music
                Highlights ``important'' information
                Lossy compression of the music around that information
            Why Analyzing Chords
                Intelligibility of simultaneous sounds
            Why Analyzing Key Changes
                Because they often occur in common-practice music
                And those changes are important
            Why Roman numeral analysis
                Because it summarizes several analytical dimensions
    Challenges
        Main challenges
            Tonal tasks overlap
                The boundary between chords and keys
                Pitch spelling
            Ambiguous annotations
            Scarcity of data
                Comparison against MNIST annotations
                Expert-annotated data
                More time consuming
        Progress
            Predict tasks simultaneously
            Provide better representations
            Applying music-theory domain knowledge
        Remaining challenges
            Segmentation
            Data scarcity
        Short-term goal: better models
        Long-term goal: better music theories
    Outline of thesis contributions
        Additional tonal tasks
        Artificial training examples
        Improved data operations (MLOps) and data hygiene
        Alternative ways to reconstruct Roman numeral labels
        Original input representation of pitch spelling
        Original layout of neural network
    Thesis structure
"""

roman_numerals = """
2-Introduction to Roman numeral analysis
    Roman numeral analysis and chord labels
    A brief history of roman numeral analysis
        The Roman numeral timeline
            The beginnings
            The Weber syntax
            Adoption of the Weber syntax
            Chord inversions
            Special chords
            Applied chords and tonicization
            Examples of modern syntax
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
        Symbolic music formats
            Humdrum(**kern)
                Origin of **kern
                Applications of **kern
                Humdrum in Roman numeral analysis
            MEI
                Origin of MEI
                Applications of MEI
                MEI in Roman numeral analysis
            MIDI
                Origin of MIDI
                Applications of MIDI
                MIDI in Roman numeral analysis
            MusicXML
                Origin of MusicXML
                Applications of MusicXML
                MusicXML in Roman numeral analysis
            Others
                ABC
                Lilypond
                MNX
                Plaine-and-Easy
        Symbolic vs audio representations
            Chroma-based features
            Pitch spelling
    Deep neural networks
        Supervised learning
        Feed forward networks
        Convolutional neural networks
            1D and 2D convolutions
            Residual connections
            Pointwise convolution
        Recurrent neural networks
            LSTM
            GRU
        Transformer networks
    Music Information Retrieval
        Key estimation
            Global-key estimation models
                Symbolic inputs
                Audio inputs
            Local-key estimation
                Local keys
                Modulation
                Tonicization
            Local-key estimation models
        Automatic chord recognition
            Chord recognition models
        Automatic pitch spelling
            Relevance of pitch spelling to tonal analysis
            Pitch-spelling models
        Automatic Roman numeral analysis
            Roman numeral analysis models
                Pioneering works
                The Melisma Music Analyzer
                Probabilistic and grammar-based models
                Deep learning models
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
                Global key distribution in BPS
                Modulation distribution in BPS
                Tonicization distribution in BPS
        Haydn ``Sun'' String Quartets (HaydnSun)
            Description of HaydnSun
                Napoles Lopez (2017)
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
                Devaney et al. (2015)
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
            Data-driven texturization
        Retrieving tonal tasks from Roman numeral annotations
"""

model_design = """
5-Model design
    Input
        Symbolic score
            MusicXML inputs
            Humdrum inputs
        Frames
            32nd note frames
            640 frames
        Encoding pitch spelling
            19 two-hot encoding
                advantages of 19
                example plot with 19 two-hot
            35 one-hot encoding
                advantages of 35
                example plot with 35 one-hot
    The bass and chroma convolutional blocks
        Convolutional layers
            6-layer configuration
            Power-of-two shapes
                Increasing convolution window
                Decreasing filters
        Bass convolutional block
            Encoding of the bass
                example plot of a bass input
        Chroma convolutional block
            Encoding of the chroma
                example plot of a chroma input
        Merging the blocks
            Concatenation of the blocks
            Adding the blocks
    Dense and recurrent layers
        Dense layer 1
        Dense layer 2
        Recurrent layers
            GRU layers
            LSTM layers
            Bidirectional
    Multitask learning configurations
        Six conventional tasks
            Local key
                Number of classes
                Encoding
                Examples
            Primary degree
            Secondary degree
            Quality
            Inversion
            Root
        Five additional tasks
            Common Roman numerals
            Harmonic Rhythm
            Bass
            Tonicization
            Pitch class set
    Implementation
        Dataset repositories
            When-in-Rome repo
            TAVERN repo
            ABC repo
            HaydnSun Repo
            BPS repo
        Recursive submodules
            Map of score-annotation pairs
            Listing of all data used
        MLOps
            Data quality metrics
                Alignment
                Pitch content
                Wrong inversion
            Unit tests
                Standard modules
        Texturization patterns
            Source code of texturization pattern
            Examples of texturization patterns
        DataFrame of score
            Columns
        Code
            Diagram
                Diagram blocks and modules
            GitHub Repository
                README
                Releases
                Zenodo archive
                API documentation
                GitHub pages
            Demos
"""

experimental_evaluation = """
6-Experimental evaluation
    Artificial texturization of augmented data
        Heuristic texturization
        Data-driven texturization
    Model configurations
        With additional tasks
        Without additional tasks
        With artificial examples
        Without artificial examples
    Choosing the best configuration
        Average accuracy across individual datasets
        AugmentedNet11+
    Comparison against SOTA
        Models considered
            Chen and Su (2018, 2019, 2021)
            Micchi et al.
        Datasets considered
            BPS test set
            WTC test set
            All other test sets
        Training procedure
            Data splits
            Epochs
            Computing time
        Hyperparameters
            Training epochs and weight selection
            Learning schedule and learning rate
    Evaluation procedure
        Baselines
            Chen and Su 2018
            Chen and Su 2019
            Chen and Su 2021
            Micchi et al. 2020
        Accuracy of individual tasks
            Conventional tasks
            Additional tasks
        Roman numeral accuracy
            Conventional
            Alternative method
    Results
    Discussion
"""

conclusions = """
7-Conclusions
    Summary
        Chapters 1--3
        Chapter 4
        Chapter 5
        Chapter 6
    Future work
"""
