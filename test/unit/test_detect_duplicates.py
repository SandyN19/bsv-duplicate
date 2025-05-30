import pytest
from src.util.detector import detect_duplicates

# develop your test cases here

@pytest.mark.unit
def test_detect_duplicates():
    assert True

def test_less_than_two_articles():
    with pytest.raises(ValueError):
        detect_duplicates("")