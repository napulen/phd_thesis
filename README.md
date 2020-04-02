### March 15, 2020

Today, I started the journey. I revised the theses from Gabriel Vigliensoni, Andrew Hankinson, and Ivan Franco. I was looking for a McGill PhD thesis template. What I found is that all these thesis have a different style (margins, font, layout, etc). There seems not to be a general template available.

I decided to recycle the project that I used for my comps.

I started writing some titles.

I realized how difficult it is to think of a title. Broad. I could write about anything and it sounds related to what I am doing. It is quite a good exercise, actually.

I ran a short estimation of the words in each of those theses. A succesful PhD dissertation in my program has around 80,000 to 90,000 words.

In the examples I saw, it seems that around 10% of the thesis' pages are blank pages, references, and table of contents. Around 90% of the pages comprise the main content of the work.

If I distributed those 80,000 words through the year, I would have to write 219 words each day to finish my thesis.

This text entry, from the begining to the end, has 271 words.

I will schedule myself ~250 words each day, about my current thoughts and concerns. It will be a good exercise for both, revisiting my thoughts in the future and getting into the habit of writing.

The next topic that I want to think about is the name and number of chapters in my dissertation. I foresee that this harmony and key duality will continue to be an issue until I put it to an end in writing.

### March 17, 2020

I sent a couple of internship project proposals to Avid. The first one is a harmonizer model. The second one, a pitch-spelling model.

Moreover, writing the proposals helped me to constrain my thesis research.

I have found myself more and more involved in Roman Numeral Analysis. That is obvious from reading my Masters and derived work. The topic is not obliged to interact with key estimation. Yet, they both feel very related to me.

At the end of the day, Temperley and Sleator computed their RNA output **inside** the key model of Melisma.

The way I see it, roman numerals are a compressed representation of key and harmony. This representation is time-varying, human-readable, ambiguous, among other things. It is very difficult to unpack it and understand what it actually represents. I hypothesize that is the reason why it has *stick* as a favorite tool of music theorists and analysts. It provides **much** information in a very small space. That space is also human-readable and moldable to interpretation, like language.

I foresee roman numerals as a bridge to produce more representations. Representations that are more **formal** and useful for machines.

I often think of roman numerals as a natural language describing harmonic change. I want to design the first of many formal languages of music. I want to enable machines to extract information from that natural language. Create lower-level representations that convey a part of that information to the machine.

I hope that will enabe the musically-aware models that researchers in my field strive for.

### March 23, 2020

Today, I was analyzing a short fragment from Tchaikovsky's Manual of Harmony. Example 185-a. 

Laurent Feisthauer and I are encoding these examples to collect a dataset of local key. We want to use such dataset to measure the performance of our algorithms.

In this example, 185-a, Tchaikovsky passes through the following keys: C major, D minor, E minor, F major, and Bb minor. Unlike most examples, there is no pivot chord connecting the keys. What Tchaikovsky denotes as the beginning of a new key, often does not refer to a tonic chord in that key. Moreover, the keys in this example, except for Bb minor, show a progression of diatonic degrees in C major. It is almost as Tchaikovsky is "tonicizing" the scale degrees ii, iii, and IV of C major.

It made me think about a possible idea for differentiating modulations from tonicizations.

In tonicizations, post-tonicization harmonies contradict the "tonal space" of the tonicized key. They support the "tonal space" of the main key. In other words, the harmonies after a tonicization bring the original key back.

In modulations, post-modulation harmonies support the "tonicized" key. They support the departure of the "tonal space" of the piece, away from its origin. In other words, the harmonies after a modulation disrupt the original key.

What is novel about this idea is that modulations and tonicizations are short-term. Modulation is not accomplished by the _length_ of the departure but by a **disruption** in the "tonal space". When that tonal space is not disrupted, we are observing a tonicization.

This sounds very close to what theorists say, but it somehow feels different in my mind. Like I am about to be able to quantify it.

### April 4, 2020

I was extracting useful references from the "Counterpoint by Convolution" (COCONET) paper.

I ended up with a compilation of 10 papers that I could investigate further. Most of the papers deal with Bach chorales. This is the best initial approach for me as well.

I went to give a brief look at the Bach chorales annotated by Craig Sapp on the Verovio Humdrum Viewer. I realized the quality of these files is very high. Craig annotated harmonies that coincided with cadences in a very systematic way. The rest of the notation is very close to `**harm` syntax. My `harmalysis` parser should be able to deal with this information with ease.

I noticed that the annotations often ignore passing tones and non-functional harmonies. Using this information to reduce the vocabulary of classes in the training process is a must. I can try both approaches, raw pitch-class sets (no annotation needed) and annotated. This will, for once, tell us if expert-curated data improves machine learning models.

I haven't revised the other papers collected from COCONET. I should start with Allan and Williams (2005), they used chord vocabularies.