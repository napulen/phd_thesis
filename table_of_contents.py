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
            RomanText
            the DCML standard
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
            MEI
                origin of MEI
                applications of MEI
                MEI in roman numeral analysis
            MIDI
                origin of MIDI
                applications of MIDI
                MIDI in roman numeral analysis
            MusicXML
                origin of MusicXML
                applications of MusicXML
                MusicXML in roman numeral analysis
    deep neural networks
        supervised learning
        feed forward networks
        convolutional neural networks
            1D, 2D, and 3D convolutions
            residual connections
        recurrent neural networks
            LSTM
            GRU
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
    roman numeral analysis data
    available datasets
        annotated beethoven corpus (ABC)
            format of ABC
                version 1
                version 2
        beethoven piano sonatas (BPS)
            format of BPS
            acquiring matching symbolic scores
        haydn ``sun'' string quartets (HaydnSun)
            format of HaydnSun
        mozart piano sonatas (MPS)
        theme and variation encodings with roman numerals (TAVERN)
            format of TAVERN
        when in rome (WiR)
            format of WiR
            converted corpora
                TAVERN
                HaydnSun
                ABC
            original corpora
                OpenScore lieder
                well-tempered clavier
                bach chorales
                monteverdi madrigals
                miscellaneous pieces
    aggregating all available datasets
        standardizing the notation between datasets
        data-curation metrics
            alignment between scores and annotations
            pitch correspondence between chord annotations and scores
            bass correspondence between chord annotations and scores
        generating training, validation, and test splits
        aggregated dataset summarized
    data augmentation
        synthesis of artificial examples
            texturization patterns
                alberti bass
                bass split
                syncopation
"""

model_design = """
5-model design
    input
        symbolic score
            format support
            required information in file
        sampling of the score
            32nd note frames
            640 frames
        encoding pitch spelling
            35 one-hot encoding
            19 two-hot encoding
        encoding duration
        input representations
            lowest sounding note
            all sounding notes
            measure and note onsets
    the bass and chroma convolutional blocks
        convolutional layers
            kernel size
            number of filters
            6-layer configuration
        merging the blocks
    dense and recurrent layers
        dense layers
        recurrent layers
    multitask learning configurations
        conventional tasks
            local key
            primary degree
            secondary degree
            inversion
            quality
            root
        proposed tasks
            Bass35
            Tenor35
            Alto35
            Soprano35
            LocalKey38
            TonicizationKey38
            PitchClassSet121
            RomanNumeralNumerator31
            HarmonicRhythm7
    reconstruct roman numeral labels
        conventional method
        common roman numerals
        proposed method
    implementation
        code diagram
        dataset source repositories
        dataframe structures
            annotation
            score
            joint
"""

experimental_evaluation = """
6-experimental evaluation
    ablation studies
        input representations
            pitch spelling encoding method
                35-one-hot encoding
            onset information
                no onset information
                measure onset only
                note onset only
        convolutional layers
            number of convolutional blocks
                one block
                four blocks
            filters-kernel ratio
                same filters, growing kernel
            number of convolutional layers
                no convolutional layers
                five layers
                seven layers
        dense layers
            number of layers
                one dense layer
                three dense layers
            linear and nonlinear layers
                linear layers
        recurrent layers
            number of layers
                no GRU layers
                one GRU layer
                three GRU layers
            layer type
                unidirectional
        data augmentation
            transposition
                no transposition
            synthesis
                no texturization
                texturization per file
                texturization per transposition
    best performing model configuration
    best strategy for final roman numeral reconstruction
        PitchClassSet121 only
        CommonRomanNumerals31 only
        SATB only
    evaluation against previous models
        experimental set up
            hyperparameters
                number of epochs
                optimizer
                learning schedule and learning rate
            data splits
            computing time
        baseline models
            chen and su (2018, 2019, 2021)
            micchi et al. (2020, 2021)
            mcleod and rohrmeier (2021)
    results
        accuracy on individual tasks
        roman numeral accuracy
        performance on difficult chords
    discussion
"""

conclusions = """
7-conclusions
    summary of contributions
    github repository
        readme
        releases
        zenodo archive
        API documentation
        github pages
    demos
    future work
"""
