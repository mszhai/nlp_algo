# -*- coding: utf-8 -*-
"""
=====================
nltk test
=====================


"""
from nltk import word_tokenize
from nltk import Text


if __name__ == '__main__':
    tokens = word_tokenize("Here is some not very interesting text")
    text = Text(tokens)