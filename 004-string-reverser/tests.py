from main import reverseString3
import pytest

def test_basic():
    assert reverseString3("hello") == "olleh"
    assert reverseString3("hello world") == "dlrow olleh"

def test_empty():
    assert reverseString3("") == ""

def test_whitespaces():
    assert reverseString3("  a ") == " a  "

def test_unicode():
    assert reverseString3("🔥cat") == "tac🔥"

