#!/usr/bin/env python3
""" File keeps track of score board and saves to pickle file """

import pickle

__author__ = 'Preston Fawcett'
__email__ = 'ptfawcett@csu.fullerton.edu'
__maintainer__ = 'PrestonFawcett'

def write(score):
    """ Save top 5 scores to a list """
    high_score = list(read())
    
    high_score.append(score)
    high_score.sort(reverse=True)
    del high_score[5:]
    with open('game_data.pickle', 'wb') as fh:
        pickle.dump(high_score, fh, pickle.HIGHEST_PROTOCOL)

def read():
    """ Return saved scores """
    with open('game_data.pickle', 'rb') as fh:
        high_score = pickle.load(fh)
        print(high_score)
        return high_score

if __name__ == '__main__':
    write()
    read()
