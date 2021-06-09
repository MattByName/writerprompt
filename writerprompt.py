#!/usr/bin/env python
import random

GENRE_FILE = 'scifi-genre.txt'
PROMPT_FILE = 'scifi-words.txt'

def get_random_line_from_text_file(filename):
    f = open(filename,'r')
    lines = f.readlines()
    selection = random.randint(0,len(lines)-1)
    return lines[selection]

def get_sub_genre():
    return get_random_line_from_text_file(GENRE_FILE)


def get_prompt():
    return get_random_line_from_text_file(PROMPT_FILE)

if __name__ == "__main__":
    print("Subgenre: {}".format(get_sub_genre()))
    for i in range(0,4):
        print("Prompt {}: {}".format(i, get_prompt()))