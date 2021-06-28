#!/usr/bin/env python3
""" File keeps track of score board and saves to pickle file """

import pickle

__author__ = 'Preston Fawcett'
__email__ = 'ptfawcett@csu.fullerton.edu'
__maintainer__ = 'PrestonFawcett'

def write(score):
    """ Save top 5 scores to a list """
    high_score = list()
    high_score.append()
    high_score.sort(reverse=True)
    high_score[:5]
    pickle.dump(high_score, open("save.p", "wb"))

def read():
    """ Return saved scores """
    high_score = pickle.load( open("save.p", "rb"))

if __name__ == '__main__':
    write()
    read()
