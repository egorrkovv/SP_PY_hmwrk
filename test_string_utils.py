import pytest
from string_utils import StringUtils 

stringutils = StringUtils()

@pytest.mark.parametrize( 'word1, word2', [ ("skypro", "Skypro"), ( " ", " "), ( "", ""), ("123","123"), ("1 2 3", "1 2 3"), ("None", "None") ] )
def test_capitalize(word1, word2):
    stringutils = StringUtils()
    res = stringutils.capitilize(word1)
    assert res == word2

@pytest.mark.parametrize( 'word1, word2', [ (" skypro", "skypro"), ( " ", ""), ( "", ""), ("123","123"), ("1 2 3", "1 2 3"), ("None", "None") ] )
def test_trim(word1, word2):
    stringutils = StringUtils()
    res = stringutils.trim(word1)
    assert res == word2

@pytest.mark.parametrize( 'word1, word2', [ ("skypro", ["skypro"]), ( " ", []), ( "", []), ("123",["123"]), ("1 2 3", ["1 2 3"]), ("None", ["None"]) ] )
def test_to_list(word1, word2):
    stringutils = StringUtils()
    res = stringutils.to_list(word1)
    assert res == word2

@pytest.mark.parametrize( 'word1, word2, word3', [ ("skypro", "s", True), ( " ", " ", True), ( "", "", True), ("123","123", True), ("1 2 3", "1 2 3", True), ("None", "None", True) ] )
def test_contains(word1, word2, word3):
    stringutils = StringUtils()
    res = stringutils.contains(word1, word2)
    assert res == word3

@pytest.mark.parametrize( 'word1, word2, word3', [ ("skypro", "s", "kypro"), ( " ", " ", ""), ( "", "", ""), ("123","123", ""), ("1 2 3", "1 2 3", ""), ("None", "None", "") ] )
def test_delete_symbol(word1, word2, word3):
    stringutils = StringUtils()
    res = stringutils.delete_symbol(word1, word2)
    assert res == word3

@pytest.mark.parametrize( 'word1, word2, word3', [ ("skypro", "s", "kypro"), ( " ", " ", ""), ( "", "", ""), ("123","123", ""), ("1 2 3", "1 2 3", ""), ("None", "None", "") ] )
def test_starts_with(word1, word2, word3):
    stringutils = StringUtils()
    res = stringutils.starts_with(word1, word2)
    assert res == word3

@pytest.mark.parametrize( 'word1, word2, word3', [ ("skypro", "o", True), ( " ", " ", True), ( "", "", True), ("123","123", True), ("1 2 3", "1 2 3", True), ("None", "None", True) ] )
def test_end_with(word1, word2, word3):
    stringutils = StringUtils()
    res = stringutils.end_with(word1, word2)
    assert res == word3

@pytest.mark.parametrize( 'word1, word2', [ ("skypro", False), ( " ", True), ( "", True), ("123", False), ("1 2 3", False), ("None", False) ] )
def test_is_empty(word1, word2):
    stringutils = StringUtils()
    res = stringutils.is_empty(word1)
    assert res == word2

@pytest.mark.parametrize( 'word1, word2', [ (["Sky", "Pro"], "Sky, Pro"), ( [" "], " "), ( [""], ""), (["123", "123"], "123, 123"), (["1 2 3", "1 2 3"], "1 2 3, 1 2 3"), (["None"], "None") ] )
def test_list_to_string(word1, word2):
    stringutils = StringUtils()
    res = stringutils.is_empty(word1)
    assert res == word2