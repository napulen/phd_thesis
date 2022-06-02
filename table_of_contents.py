introduction = """
1-introduction
    motivation for roman numeral analysis
    challenges
        main challenges
            tonal tasks overlap
                the boundary between chords and keys
                pitch spelling
            ambiguous annotations
            scarcity of data
                comparison against mnist annotations
                expert-annotated data
                more time consuming
        progress
            predict tasks simultaneously
            provide better representations
            applying music-theory domain knowledge
        remaining challenges
            segmentation
            data scarcity
        short-term goal: better models
        long-term goal: better music theories
    outline of thesis contributions
        additional tonal tasks
        artificial training examples
        improved data operations (MLOps) and data hygiene
        alternative ways to reconstruct roman numeral labels
        original input representation of pitch spelling
        original layout of neural network
    thesis structure
"""

roman_numerals = """
2-introduction to roman numeral analysis
    roman numeral analysis and chord labels
    a brief history of roman numeral analysis
        early precedents and the weber syntax
        adoption of the weber syntax
        chord inversions and figured bass
        neapolitans, augmented sixths, and other special chords
        applied chords and tonicization
    digitization of roman numeral annotations
        digital standards
            humdrum(**harm)
            romantext
            the dcml standard
            harmalysis
"""

background = """
3-background
    music representation
        symbolic music formats
            humdrum(**kern)
                origin of **kern
                applications of **kern
                humdrum in roman numeral analysis
            mei
                origin of mei
                applications of mei
                mei in roman numeral analysis
            midi
                origin of midi
                applications of midi
                midi in roman numeral analysis
            musicxml
                origin of musicxml
                applications of musicxml
                musicxml in roman numeral analysis
    deep neural networks
        supervised learning
        feed forward networks
        convolutional neural networks
            1d, 2d, and 3d convolutions
            residual connections
        recurrent neural networks
            lstm
            gru
        transformer networks
    music information retrieval
        key estimation
            global-key estimation models
                symbolic inputs
                audio inputs
            local-key estimation
                local keys
                modulation
                tonicization
            local-key estimation models
        automatic chord recognition
        automatic pitch spelling
            pitch-spelling models
        automatic roman numeral analysis
            roman numeral analysis models
                pioneering works
                the melisma music analyzer
                probabilistic and grammar-based models
                deep learning models
"""

data_acquisition = """
4-data acquisition and preparation
    roman numeral analysis datasets
    available datasets
        annotated beethoven corpus
            format of ABC
                version 1
                version 2
        beethoven piano sonatas
            format of BPS
            accompanying scores
                no scores provided
                aligning scores is not trivial
        haydn ``sun'' string quartets
            format of HaydnSun
        mozart piano sonatas
            format of MPS
        theme and variation encodings with roman numerals
            format of TAVERN
        when in rome
            format of WiR
                romantext
            converted corpora
                TAVERN
                HaydnSun
                converted ABC
            original corpora
                OpenScore lieder
                well-tempered clavier
                bach chorales
                monteverdi madrigals
                miscellaneous pieces
    data preparation
        problems of diverse datasets
            examples of misalignment in BPS
            mislabeled annotations
            different spellings
            diverging chord vocabularies
        data-curation tools
            alignment of scores
            verifying pitch content
        aligning a score and an annotation file
        standardizing the notation between datasets
    data augmentation
        synthesis of artificial examples
            texturization patterns
                alberti bass
                bass split
                syncopation
            data-driven texturization
"""

model_design = """
5-model design
    input
        symbolic score
            musicxml inputs
            humdrum inputs
        frames
            32nd note frames
            640 frames
        encoding pitch spelling
            19 two-hot encoding
                advantages of 19
                example plot with 19 two-hot
            35 one-hot encoding
                advantages of 35
                example plot with 35 one-hot
    the bass and chroma convolutional blocks
        convolutional layers
            6-layer configuration
            power-of-two shapes
                increasing convolution window
                decreasing filters
        bass convolutional block
            encoding of the bass
                example plot of a bass input
        chroma convolutional block
            encoding of the chroma
                example plot of a chroma input
        merging the blocks
            concatenation of the blocks
            adding the blocks
    dense and recurrent layers
        dense layer 1
        dense layer 2
        recurrent layers
            gru layers
            lstm layers
            bidirectional
    multitask learning configurations
        six conventional tasks
            local key
                number of classes
                encoding
                examples
            primary degree
            secondary degree
            quality
            inversion
            root
        five additional tasks
            common roman numerals
            harmonic rhythm
            bass
            tonicization
            pitch class set
    implementation
        dataset repositories
            when-in-rome repo
            tavern repo
            abc repo
            haydnsun repo
            bps repo
        recursive submodules
            map of score-annotation pairs
            listing of all data used
        mlops
            data quality metrics
                alignment
                pitch content
                wrong inversion
            unit tests
                standard modules
        texturization patterns
            source code of texturization pattern
            examples of texturization patterns
        dataframe of score
            columns
        code
            diagram
                diagram blocks and modules
            github repository
                readme
                releases
                zenodo archive
                api documentation
                github pages
            demos
"""

experimental_evaluation = """
6-experimental evaluation
    artificial texturization of augmented data
        heuristic texturization
        data-driven texturization
    model configurations
        with additional tasks
        without additional tasks
        with artificial examples
        without artificial examples
    choosing the best configuration
        average accuracy across individual datasets
        augmentednet11+
    comparison against state-of-the-art
        models considered
            chen and su (2018, 2019, 2021)
            micchi et al.
        datasets considered
            bps test set
            wtc test set
            all other test sets
        training procedure
            data splits
            epochs
            computing time
        hyperparameters
            training epochs and weight selection
            learning schedule and learning rate
    evaluation procedure
        baselines
            chen and su 2018
            chen and su 2019
            chen and su 2021
            micchi et al. 2020
        accuracy of individual tasks
            conventional tasks
            additional tasks
        roman numeral accuracy
            conventional
            alternative method
    results
    discussion
"""

conclusions = """
7-conclusions
    summary
        chapters 1--3
        chapter 4
        chapter 5
        chapter 6
    future work
"""
