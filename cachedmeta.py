#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# PYTHON_ARGCOMPLETE_OK
from collections import defaultdict
from dataclasses import dataclass


class CachedMeta(type):
    _cached = defaultdict(dict)

    def __call__(cls, *args):
        tup = tuple(args)
        if tup not in type(cls)._cached[cls]:
            obj = super().__call__(*args)
            type(cls)._cached[cls][tup] = obj
        return type(cls)._cached[cls][tup]


@dataclass
class Exercise(metaclass=CachedMeta):
    name: str
    weight: float
    reps: int

    def __repr__(self):
        return f"Exercise({self.name}, {self.weight}, {self.reps})"


if __name__ == "__main__":
    ex1 = Exercise("squat", 87.5, 3)
    ex2 = Exercise("squat", 87.5, 3)
    ex3 = Exercise("squat", 90.0, 2)
    print(ex1, ex2, ex3)
    assert ex1 is ex2
    assert ex3 is not ex2
