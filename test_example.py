import pytest
from project.example import soma, subtracao, multiplicacao


def test_soma():
    assert soma(10, 5) == 15


def test_subtracao():
    assert subtracao(10, 5) == 5


def test_multiplicacao():
    assert multiplicacao(10, 5) == 50
