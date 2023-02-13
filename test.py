import pytest
from .dep_graph import construct_graph

def test_answer(capfd):
    construct_graph("./dep_graph/test.json")

    expected = "-pkg1\n -pkg2\n  -pkg3\n -pkg3\n-pkg2\n -pkg3\n-pkg3"

    out, err = capfd.readouterr()
    assert out == expected
