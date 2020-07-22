What is a modulation? An approach from computational music theory.

Introduction
	Music theories should be supported by proof (data).
    Music theories should comply the basic scrutiny that we hold for all science.
    This is possible nowadays thanks to computational methods, that allow us to scrutinize large amounts of data that would be impossible for human analysts.
    Hence, this work is a bridge between music theory and computer science.

    A word on "music theories" and "rules"
        There is no "true" modulation theory, as there is no true "harmony" or "counterpoint" theory.
        There can only be a "better theory" than the one we know.
        A better theory generalizes better than the preceding theory. That is, it demonstrates with data (or some other mean) that, in fact, the theory is able to describe, characterize, or summarize the music composed for a particular period.
        Many ideas taken as a baseline for this dissertation are the best-known theories in modulation and harmony, which have been adopted by many theorists, taught in college-level music curricula, and achieve good (but imperfect) generalization in common-practice music.
        Examples of these theories and workflows include roman numeral analysis and Riemannian-theory.
        Other theories (Schenkerian, GTTM) have not achieved widespread reach as to replace them in the core textbooks and resources used in music education institutions.

    Cognition of tonality is elusive, culturally-dependent, and for the most part, an open research question. 
    It is expected that music cognition will help answering many questions about the topics discussed here, however, the knowledge in this area is far from able to replace the theories that are taught to aspiring musicians, composers, theorists, and scholars.

    Cognitive theories of tonality are briefly discussed, but they are not at the core of this work.

    A word on music theories in comparison to machine learning algorithms
        A very basic and opinionated way in which I like to think about music theories is in a similar way than modern machine learning algorithms. There are many parameters that have been achieved and fine-tuned by iteration, approximation, and correction. In the case of machine learning algorithms, a computer is responsible of performing these iterations and converging toward a solution of the problem. In music theory, the iterations are hundreds of years of fine-tuning and human analysis, which have resulted in our Western music theory. Roman numerals are applied to music composed a hundred years ago, not because composers thought that way, but because the roman numerals are those "parameters" that human analysts have fine-tuned over the years to generalize their understanding and explicability of the music they study.
    
    This work deals with two basic domains: music theory and data science.
    
Literature review
    History of modulation
        The origin of the term "modulation"
            When was the word "modulation" introduced?
                (Peter Schubert said that the word was really old, I expect to find explicit references in the renaissance to what "modulation" meant back then)
            What is a modulation?
                (Introduce the change of meaning here)
            When was the word "modulation" used to denote a "change of key" for the first time?
                (Probably around the late eighteenth century, as I found out explicit references recently)
            How has the meaning of the word "modulation" changed over time?
                Structural definitions (i.e., PAC, change of key signature, etc.)
                Distributional definitions (i.e., length of change of key, keyscapes, etc.)  

        The origin of the term "tonicization"
            When was the word "tonicization" first introduced?
            What is a tonicization?

        The origin of the term "secondary dominant"
            When was the term "secondary dominant" first introduced?
            Is it the same that a "tonicization"?        

        The origin of the term "applied chord/secondary chord"
            When was the term "applied chord" first introduced?
            Is it the same that a "tonicization"?

        The origin of the term "modal mixture/modal borrowing"
            When was the term "modal mixture" first introduced?
            Is it the same that a "tonicization"?

        The origin of the term "local key"
            When was the term "local key" first introduced?
            How does it relate to modulation and tonicization?

        A summarized comparison of modulation, tonicization, secondary chords, modal mixture, and local keys
    
    Modulation in Music Information Retrieval (MIR)
        Global key-estimation models
        Local key-estimation models

    Modulation in Music Cognition
        Perception of musical keys
        Perception of modulations
        Perception of tonicizations
        Perception of musical keys compared to predictions of key-estimation algorithms
        Unanswered questions
        Closing remarks on tonality and music cognition

Computing modulation
    Pitch classes
        justkeydding
    Symbolic and Audio
        justkeydding
    Harmony and key analysis
        pitch class sets
    Structural cues of modulation
        PAC
        Motivic analysis

Quantifying modulation
    Modulation and tonicization MIR tasks
    MIREX
    Key distance
    Weber diagrams
    Krumhansl key distance model
    Lerdahl's Tonal Pitch Space    

Applications of a key modulation model
    Categorizing music using pitch-class sets
    Assigning roman numeral analysis labels
    MIDI pitch spelling

