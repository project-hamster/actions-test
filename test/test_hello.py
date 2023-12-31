import pytest
from app import hello



def test_echo_hello():
    actual = hello.echo_hello()
    expect = "hllo"
    assert actual == expect
