#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# PYTHON_ARGCOMPLETE_OK
from collections import defaultdict


class CachedMeta(type):
    _instances = {}

    def __call__(cls, *args):
        # cached = {}
        if cls in type(cls)._instances:
            cached = type(cls)._instances[cls]
        else:
            cached = type(cls)._instances[cls] = {}
        tup = tuple(args)
        if tup not in cached:
            obj = super().__call__(*args)
            cached[tup] = obj
        else:
            obj = cached[tup]
        return obj


class Exercise(metaclass=CachedMeta):
    def __init__(self, name, weight, reps):
        self.name = name
        self.weight = weight
        self.reps = reps
        print(f"{self} initialized")

    def __repr__(self):
        return f"Exercise({self.name}, {self.weight}, {self.reps})"


if __name__ == "__main__":
    ex1 = Exercise("squat", 87.5, 3)
    ex2 = Exercise("squat", 87.5, 3)
    ex3 = Exercise("squat", 90.0, 2)
    assert ex1 is ex2
    assert ex3 is not ex2
