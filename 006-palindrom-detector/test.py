from main import detectPalindromes
import pytest

def test_correct():
    assert detectPalindromes("Madam") == True
    assert detectPalindromes("Level") == True
    assert detectPalindromes("Deed") == True
    assert detectPalindromes("Civic") == True
    assert detectPalindromes("1221") == True
    assert detectPalindromes("6996") == True


def test_incorrect():
    assert detectPalindromes("Knight") == False
    assert detectPalindromes("Tavern") == False
    assert detectPalindromes("Castle") == False
    assert detectPalindromes("1234") == False
    assert detectPalindromes("8773") == False


def test_invalid():
    pass
