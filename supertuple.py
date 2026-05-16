#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# PYTHON_ARGCOMPLETE_OK


class TupleMeta(type):
    pass


class SuperTuple(metclass=TupleMeta):
    pass


if __name__ == "__main__":
    st = SuperTuple(1, "asdf", 23.5)
    print(st)
