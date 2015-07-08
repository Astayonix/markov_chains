import sys, random


def make_chains(corpus):
    """Takes input text as string; returns dictionary of markov chains."""

    open_file = open(corpus)
    words = []
    for line in open_file:
        words.extend(line.split())
    markov_dict = {}

    for i in range(len(words)-2):
        markov_key = (words[i], words[i+1])
        markov_dict[markov_key] = []
    for i in range(len(words)-2):
        markov_key = (words[i], words[i+1])
        markov_dict[markov_key].append(words[i+2])
    return markov_dict

def make_text(chains):
    """Takes dictionary of markov chains; returns random text."""
    #getting an error at line 31 because of tuple ('I','am?') try .get function on line 30 
    #or while loop on line 29 in lieu of for loop
    first_bigram = random.choice(chains.keys())
    w1, w2 = first_bigram
    markov_text_as_list = []

    for i in range(len(chains.keys())):
        markov_text_as_list.append(w1)
        w1, w2 = w2, random.choice(chains[w1,w2])
        print w1,w2
        if w2 == "":
            break

    return " ".join(markov_text_as_list)

# Change this to read input_text from a file, deciding which file should
# be used by examining the `sys.argv` arguments (if neccessary, see the
# Python docs for sys.argv)

# Get a Markov chain
chain_dict = make_chains("green-eggs.txt")
print chain_dict
# Produce random text
random_text = make_text(chain_dict)

print random_text

# opened_file = open("green-eggs.txt")

# print sys.argv[0]
# print len(sys.argv)
# print str(sys.argv)