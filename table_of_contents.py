introduction = """
1-introduction
    motivation for roman numeral analysis
    challenges
        main challenges
            tonal tasks overlap
                the boundary between chords and keys
                pitch spelling
            ambiguous annotations
            time-consuming annotations
        progress
            predict tasks simultaneously
            provide better representations
            applying music-theory domain knowledge
        remaining challenges
            segmentation
            data scarcity
        short-term goal: better models
        long-term goal: interpretability
    outline of thesis contributions
        additional tonal tasks
        artificial training examples
        data hygiene
        generating roman numeral labels from predictions
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
        summary of the findings
    standardization of roman numeral annotations
        digital representation of roman numerals
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
            multitask learning approaches
                local key
                primary degree
                secondary degree
                inversion
                quality
                root
"""

data_acquisition = """
4-data acquisition and preparation
    general preparation of the data
        standardizing the annotations
        detecting errors in the annotations
            common error patterns
                alignment between scores and annotations
                pitch correspondence between chord annotations and scores
                correspondence between lowest-sounding note and bass of the chord
        summary of the preparation
    publicly available datasets
        annotated beethoven corpus (ABC)
            format of ABC
                version 1
                version 2
            summary of the ABC dataset
        beethoven piano sonatas (BPS)
            format of BPS
            acquiring matching symbolic scores
            summary of the BPS dataset
        haydn ``sun'' string quartets (HaydnSun)
            format of HaydnSun
            summary of the HaydnSun dataset
        key modulations and tonicizations (KMT)
            format of KMT
            summary of the KMT dataset
        mozart piano sonatas (MPS)
            summary of the MPS dataset
        theme and variation encodings with roman numerals (TAVERN)
            format of TAVERN
            summary of the TAVERN dataset
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
            summary of the WiR dataset
    the aggregated dataset
    generating training, validation, and test splits   
    data augmentation
        synthesis of artificial training examples
            block chord sequences
            texturization patterns
                alberti bass
                bass split
                syncopation
"""

model_design = """
5-model design
    input
        importing a digital music score
            supported formats
        sampling of the score
            note duration of each timestep
            number of timesteps
        encoding the score
            encoding notes with spelling
                35 one-hot encoding
                19 two-hot encoding
            encoding measure, note, and chord onsets
        input representations
            lowest sounding note
            all sounding notes
            measure and note onsets
    the convolutional blocks
        1D convolutional layers inside a block
            kernel size
            number of filters
            number of convolutional layers
        merging the blocks
    dense and recurrent layers
        dense layers
        recurrent layers
    multitask learning outputs
        Bass35
        Tenor35
        Alto35
        Soprano35
        LocalKey38
        TonicizationKey38
        PitchClassSet121
        Numerator31
        HarmonicRhythm7
    from output predictions to roman numeral labels
        direct method
        indirect method
                resolving the numerator and tonicization
"""

experimental_evaluation = """
6-experimental evaluation
    ablation studies
        baseline model
        changing the input representations
            encoding pitch spelling with an alternative method
            no lowest-sounding note information
            no upper notes information
            no onset information
        changing the convolutional layers
            single convolutional block
            constant number of filters
            no convolutional layers
        single dense linear layer
        changing the recurrent layers
            removing the recurrent layers
            unidirectional recurrent layers
        summary of the ablation studies
    effects of data augmentation
        no data augmentation (baseline)
        synthesis
        transposition
        synthesis and transposition
        summary of the effects of data augmentation
    training on the aggregated dataset
    evaluation against previous models
        baseline models
            melisma (2003)
            chen and su (2021)
            micchi et al. (2021)
            McLeod and rohrmeier (2021)
        experimental set up
            standardizing the chord vocabulary
            evaluation procedure
    results
        time performance on inference
        accuracy on individual tasks
        roman numeral accuracy
            confusion matrix for melisma (2003)
            confusion matrix for chen and su (2021)
            confusion matrix for micchi et al. (2021)
            confusion matrix for McLeod and rohrmeier (2021)
            confusion matrix for AugmentedNet
            summary of performance on difficult chords
    discussion
"""

conclusions = """
7-conclusions
    summary of the dissertation
    summary of the contributions
    source code and reproducibility
        releases
        pretrained model
        preprocessed data
        experiment logs
        API documentation
    future work
        texturization
            data-driven texturization
            synthesizing nonchord tones
        extending the chord vocabulary
        standardization
            consistency in modulations and tonicizations
            consistency in chords and inversions
        audio support
        applications
            batch corpus analysis
            harmonic reduction
            melody harmonization
    closing remarks
"""

appendix = """
8-a method for systematic roman numeral analysis
    the structure of a roman numeral analysis label
    the vocabulary of roman numeral numerators
        chords of the major mode
            major-mode triads
            major-mode seventh chords
            major-mode augmented dominant
        chords of the minor mode
            minor-mode triads
            minor-mode seventh chords
        chords shared in both modes
            special chords
                augmented dominant
                neapolitan chord
                augmented sixth chords
    the vocabulary of roman numeral denominators
    the vocabulary of musical keys
    the vocabulary of arabic numeral inversions
    the vocabulary of pitch-class sets
    the numerator and tonicization estimation method
        retrieving the numerator
        forcing a tonicization
"""
