introduction = """
1-Introduction
    Motivation for Roman numeral analysis
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
        Early precedents and the Weber syntax
        Adoption of the Weber syntax
        Chord inversions and figured bass
        Neapolitans, augmented sixths, and other special chords
        Applied chords and tonicization
    Digitization of roman numeral annotations
        Digital standards
            Humdrum(**harm)
            RomanText
            The DCML standard
            Harmalysis
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
    Deep neural networks
        Supervised learning
        Feed forward networks
        Convolutional neural networks
            1D, 2D, and 3D convolutions
            Residual connections
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
        Automatic pitch spelling
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
    Available datasets
        Annotated Beethoven Corpus
            Format of ABC
            Revisions
                Version 1
                Version 2
        Beethoven Piano Sonatas
            Format of BPS
            Accompanying scores
                No scores provided
                Aligning scores is not trivial
        Haydn ``Sun'' String Quartets
            Format of HaydnSun
        Mozart Piano Sonatas
            Format of MPS
                DCML standard in MPS
        Theme and Variation Encodings with Roman numerals
            Format of TAVERN
        When-in-Rome
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
    Comparison against state-of-the-art
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
