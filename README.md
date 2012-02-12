
Minimum Viable Ipsum 
====================

An MVP for generating MVP-related terminology for using as placeholder text.

## Usage 

If you'd like help, just use the `-h` to see the "minimal" options available:

    $ ./mvipsum -h 

Output:

    Usage: mvipsum [-w=#][-s=#]

    Options:
        -h, --help    show this help message and exit
        -w WORDS      Number of words to generate
        -s SENTENCES  Number of sentences to generate

You can specify the number of words generated from the lexicon file. 

     $ ./mvipsum -w 19

Output:

     customer development metrics early adopters vanity metric prototyping minimum viable product super-limited version of your product Eric Rees business leaders lean easier way to learn RVR success criteria process continual learning lessons pivot MVP features

You can specify the number of sentences generated from the lexicon file. Sentences are generated based on the average number of words in an English sentence (default word count per sentence is 14). 

     $ ./mvipsum -s 3

Output:

     ROI avoidable expense of time and money batch size RVR trotted out A/B Testing failure criteria least effort metrics features idea generation validate assumptions vanity metric CRM system pivoting pivot learning and cycle time value minimum viable product iterative early adopters process lean validated learning risky assumptions non-viable business leaders super-limited version of your product emerge success criteria build-measure-learn loop early prototype prototyping customer focused just-in-time direction continual learning product vision low-hanging fruit Eric Rees lukewarm MVP

If both `-w` & `-s` are used, the maximum number of words will be used. 

## Lexicon 

The terminology used is in the lexicon file, `lexicon.ndy`.  

If new terms are needed, edit this file. 

