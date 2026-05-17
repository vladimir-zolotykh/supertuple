# test_supertuple.py

import pytest

from supertuple import SuperTuple, Exercise


def test_exercise_creation():
    ex = Exercise("squat", 87.5, 3)

    assert isinstance(ex, tuple)
    assert isinstance(ex, SuperTuple)


def test_field_accessors():
    ex = Exercise("squat", 87.5, 3)

    assert ex.name == "squat"
    assert ex.weight == 87.5
    assert ex.reps == 3


def test_tuple_indexing():
    ex = Exercise("squat", 87.5, 3)

    assert ex[0] == "squat"
    assert ex[1] == 87.5
    assert ex[2] == 3


def test_as_csv_matches_doctest():
    ex = Exercise("squat", 87.5, 3)

    assert ex.as_csv() == "name='squat', weight=87.5, reps=3"


def test_repr_matches_doctest():
    ex = Exercise("squat", 87.5, 3)

    assert repr(ex) == "Exercise(self._as_tuple())"


def test_wrong_number_of_arguments_too_few():
    with pytest.raises(ValueError) as exc:
        Exercise("squat", 87.5)

    assert str(exc.value) == "Expected 3 , got 2"


def test_wrong_number_of_arguments_too_many():
    with pytest.raises(ValueError) as exc:
        Exercise("squat", 87.5, 3, "extra")

    assert str(exc.value) == "Expected 3 , got 4"


def test__as_tuple():
    ex = Exercise("bench", 100, 5)

    assert ex._as_tuple() == "(bench, 100, 5)"


def test_tuple_behavior():
    ex = Exercise("deadlift", 180, 1)

    assert len(ex) == 3
    assert tuple(ex) == ("deadlift", 180, 1)


def test_immutable():
    ex = Exercise("squat", 87.5, 3)

    with pytest.raises(AttributeError):
        ex.name = "bench"

    with pytest.raises(TypeError):
        ex[0] = "bench"
