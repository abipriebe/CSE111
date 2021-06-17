from names import make_full_name, \
    extract_given_name, extract_family_name
from names import extract_family_name, extract_given_name, make_full_name
import pytest

def test_make_full_name():
    assert(make_full_name("Abigail Rose", "Cluff-Priebe") == "Cluff-Priebe;Abigail Rose")
    assert(make_full_name("McKinley", "Woodin") == "Woodin;McKinley")
    assert(make_full_name("Zach", "Young") == "Young;Zach")
    assert(make_full_name("Dal-lin", "Talbot") == "Talbot;Dal-lin")

def test_extract_family_name():
    assert(extract_family_name("Young;Zach") == "Young")
    assert(extract_family_name("Cluff-Priebe;Abigail Rose") == "Cluff-Priebe")
    assert(extract_family_name("Woodin;McKinley") == "Woodin")
    assert(extract_family_name("Talbot;Dal-lin") == "Talbot")


def test_extract_given_name():
    assert(extract_given_name("Young;Zach") == "Zach")
    assert(extract_given_name("Woodin;McKinley") == "McKinley")
    assert(extract_given_name("Cluff-Priebe;Abigail Rose") == "Abigail Rose")
    assert(extract_given_name("Talbot;Dal-lin") == "Dal-lin")

pytest.main(["-v", "--tb=line", "-rN", "team activity 5.py"])