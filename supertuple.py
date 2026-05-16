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


class Exercise(SuperTuple):
    _fields = ["name", "weight", "reps"]


if __name__ == "__main__":
    st = Exercise("squat", 87.5, 3)
    print(st.name, st.weight, st.reps)
