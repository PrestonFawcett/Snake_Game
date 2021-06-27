#!/usr/bin/env python3

import pickle, random

def write():
    high_score = list()

def read():
    with open('game_data.pickle', 'rb') as fh:
        high_score = pickle.load(fh)
    print(high_score)

if __name__ == '__main__':
    write()
    read()