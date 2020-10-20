"""Dunder exercises"""


class ReverseView:
    """Lazily operate on a sequence in reverse."""
    def __init__(self, main_seq):
        self._main_seq = main_seq
        self._length = len(main_seq)
    def __getitem__(self, index):
        return self._main_seq[-(index + 1)]
    def __len__(self):
        return len(self._main_seq)
    def __str__(self):
        rslt = "["
        for i in range(0, self._length):
            rslt += str(self._main_seq[-(i+1)])
            rslt += ", "
        return rslt[:-2] + "]"
    def apend(self, i):
        self._main_seq.append(i)




class Comparator:
    """Object that is equal to a very small range of numbers."""


class RomanNumeral:
    """Class for treating Roman Numerals like numbers."""


class Timer:
    """Utility for timing the execution of code."""


class FancyDict:
    """Dictioray-like class supporting attribute lookups."""
