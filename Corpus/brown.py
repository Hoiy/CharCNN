from nltk.corpus import brown

def raw():
    return brown.raw();
"""
def corpus(toLower=True, verbose=0):
    sents = brown.sents()
    words = brown.words()
    if verbose:
        print("Number of tokens: {}".format(len(words)))
        print("Number of sentences: {}".format(len(sents)))
        print("Longest sentences length: {}".format(max([len(sent) for sent in sents])))
    return sents, words
"""
if __name__=='__main__':
    pass
