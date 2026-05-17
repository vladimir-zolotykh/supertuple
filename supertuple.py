#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# PYTHON_ARGCOMPLETE_OK
import operator


class TupleMeta(type):
    def __init__(cls, clsname, bases, clsdict):
        fields = clsdict.get("_fields", [])
        for n, name in enumerate(fields):
            setattr(cls, name, property(operator.itemgetter(n)))
        super().__init__(clsname, bases, clsdict)


class SuperTuple(tuple, metaclass=TupleMeta):
    def __new__(cls, *args):
        if len(args) != len(cls._fields):
            raise ValueError(f"Expected {len(cls._fields)} , got {len(args)}")
        return super().__new__(cls, args)

    def as_csv(self):
        return ", ".join(f"{name}={getattr(self, name)!r}" for name in self._fields)

    def _as_tuple(self) -> str:
        items = ", ".join(str(self.__getitem__(n)) for n in range(len(self)))
        return "(" + items + ")"

    def __repr__(self):
        return f"{self.__class__.__name__}(self._as_tuple())"


class Exercise(SuperTuple):
    _fields = ["name", "weight", "reps"]


if __name__ == "__main__":
    """
    >>> ex = Exercise("squat", 87.5, 3)
    >>> ex.as_csv()
    "name='squat', weight=87.5, reps=3"
    >>> repr(ex)
    'Exercise(self._as_tuple())'
    >>>
    """
    import doctest

    doctest.testmod()
