################################################################################
# guilty-party: Andrew J Lenards <http://github.com/lenards>
# date: Saturday, February 11, 2012 09:01 PM
# purpose: generate placeholder text for lean startup organizations & MVPs
################################################################################

"""
We'll be using optparse until we determine what are Python versions are.

We are assuming that we would like to target Python version 2.4, 2.5, 2.6 with
this script - and not force any Python EGGs to be installed in order to execute.

optparse has been deprecated since Python 2.7.* and new development has move to
the argparse module.

"""

import os.path
import random
# Yes - I know ``optparse`` is deprecated (see above rant)
from optparse import OptionParser

LEXICON_FILE = 'lexicon.ndy'
AVE_WORDS_PER_SENT = 14

def read_in_lexicon():
    fh = open(LEXICON_FILE, 'r')
    lines = fh.readlines()

    lines.pop(0)  # get rid of the heading line
    
    # clean up the new-lines and spaces 
    for i in range(0, len(lines)):
        lines[i] = lines[i].strip()

    return lines

def generate(lines, wordCount):
    if (wordCount > len(lines)):
        tmp = ' '.join(random.sample(lines, len(lines)))
        tmp += ' '.join(random.sample(lines, wordCount - len(lines)))
        return tmp
    else:
        return ' '.join(random.sample(lines, wordCount))

def main():
    """
    Script execution entry point. 
    """ 

    usage = ''.join(["usage: mvipsum [-w=#]", "[-s=#]"])

    parser = OptionParser(usage=usage)
    parser.add_option("-w", action="store", dest="words",
                      help="Number of words to generate")
    parser.add_option("-s", action="store", dest="sentences",
                      help="Number of sentences to generate")

    (options, args) = parser.parse_args()

    if os.path.exists(LEXICON_FILE):
        lexicon = read_in_lexicon()
        wordCount = 0
        if (options.words != None and options.sentences != None):
            wordCount = max(int(options.words), 
                            int(options.sentences) * AVE_WORDS_PER_SENT)
        elif (options.sentences != None):
            wordCount = int(options.sentences) * AVE_WORDS_PER_SENT
        elif (options.words != None):
            wordCount = int(options.words)
        else:
            exit("\n The number of words or sentences should be stated...\n")
        print generate(lexicon, wordCount)
    else:
        exit("\n Bummer! The lexicon file is missing...\n")

if __name__ == '__main__':
    main()
