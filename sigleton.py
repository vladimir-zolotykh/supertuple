#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# PYTHON_ARGCOMPLETE_OK


class Singleton(type):
    _instances = {}

    def __call__(cls):
        if cls in Singleton._instances:
            return Singleton._instances[cls]
        obj = super().__call__()
        Singleton._instances[cls] = obj
        return obj


class Logger(metaclass=Singleton):
    def __init__(self):
        print(f"{self} is being initialized")


if __name__ == "__main__":
    log1 = Logger()
    log2 = Logger()
    assert log1 is log2
