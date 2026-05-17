# test_cachedmeta.py

import pytest

from cachedmeta import CachedMeta, Exercise


@pytest.fixture(autouse=True)
def clear_cache():
    """
    Ensure test isolation by clearing the metaclass cache
    before each test.
    """
    CachedMeta._cached.clear()


def test_exercise_creation():
    ex = Exercise("squat", 87.5, 3)

    assert ex.name == "squat"
    assert ex.weight == 87.5
    assert ex.reps == 3


def test_repr():
    ex = Exercise("bench", 100, 5)

    assert repr(ex) == "Exercise(bench, 100, 5)"


def test_same_arguments_return_same_object():
    ex1 = Exercise("squat", 87.5, 3)
    ex2 = Exercise("squat", 87.5, 3)

    assert ex1 is ex2


def test_different_arguments_return_different_objects():
    ex1 = Exercise("squat", 87.5, 3)
    ex2 = Exercise("squat", 90.0, 2)

    assert ex1 is not ex2


def test_cache_contains_created_instance():
    ex = Exercise("deadlift", 180, 1)

    key = ("deadlift", 180, 1)

    assert key in CachedMeta._cached[Exercise]
    assert CachedMeta._cached[Exercise][key] is ex


def test_init_called_only_once_for_same_arguments(capsys):
    ex1 = Exercise("squat", 87.5, 3)
    ex2 = Exercise("squat", 87.5, 3)

    captured = capsys.readouterr()

    assert ex1 is ex2

    # __init__ should only print once
    assert captured.out.count("initialized") == 1


def test_init_called_for_different_arguments(capsys):
    Exercise("squat", 87.5, 3)
    Exercise("squat", 90.0, 2)

    captured = capsys.readouterr()

    assert captured.out.count("initialized") == 2


def test_cache_is_per_class():
    class Another(metaclass=CachedMeta):
        def __init__(self, value):
            self.value = value

    ex = Exercise("squat", 87.5, 3)
    other = Another("squat")

    assert ex is not other

    assert ("squat", 87.5, 3) in CachedMeta._cached[Exercise]
    assert ("squat",) in CachedMeta._cached[Another]


def test_mutating_cached_instance_affects_all_references():
    ex1 = Exercise("bench", 100, 5)
    ex2 = Exercise("bench", 100, 5)

    ex1.reps = 10

    assert ex2.reps == 10


def test_cache_key_depends_on_argument_order():
    ex1 = Exercise("squat", 87.5, 3)
    ex2 = Exercise(87.5, "squat", 3)

    assert ex1 is not ex2
