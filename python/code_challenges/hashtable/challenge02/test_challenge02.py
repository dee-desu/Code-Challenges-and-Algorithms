# Write your test here

from challenge02 import firstRepeatedWord
import pytest


def test1():
    sentence = "ASAC is a department at LTUC. ASAC teaches programming in LTUC."
    assert firstRepeatedWord(sentence) == 'ASAC'


def test2():
    sentence = "I am learning programming at ASAC."
    assert firstRepeatedWord(sentence) == 'No Repetition'