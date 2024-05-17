import pytest
from string_utils import StringUtils 

stringutils = StringUtils()

@pytest.mark.parametrize( 'word1, word2', [ ("skypro", "Skypro"), ("123","123"), ("1 2 3", "1 2 3") ] )
def test_capitalize(word1, word2):
    stringutils = StringUtils()
    res = stringutils.capitilize(word1)
    assert res == word2

@pytest.mark.parametrize( 'word1, word2', [ ( " ", " "), ( "", ""), (None, None) ] )
@pytest.mark.xfail
def test_capitalize_negative(word1, word2):
    stringutils = StringUtils()
    res = stringutils.capitilize(word1)
    assert res == word2

@pytest.mark.parametrize( 'word1, word2', [ (" skypro", "skypro"),("123","123"), ("1 2 3", "1 2 3") ] )
def test_trim(word1, word2):
    stringutils = StringUtils()
    res = stringutils.trim(word1)
    assert res == word2

@pytest.mark.parametrize( 'word1, word2', [ ( " ", ""), ( "", ""), (None, None) ] )
@pytest.mark.xfail
def test_trim_negative(word1, word2):
    stringutils = StringUtils()
    res = stringutils.trim(word1)
    assert res == word2

@pytest.mark.parametrize( 'word1, word2', [ ("skypro", ["skypro"]), ("123",["123"]), ("1 2 3", ["1 2 3"]) ] )
def test_to_list(word1, word2):
    stringutils = StringUtils()
    res = stringutils.to_list(word1)
    assert res == word2

@pytest.mark.parametrize( 'word1, word2', [ ( " ", []), ( "", []), (None, [None]) ] )
@pytest.mark.xfail
def test_to_list_negative(word1, word2):
    stringutils = StringUtils()
    res = stringutils.to_list(word1)
    assert res == word2

@pytest.mark.parametrize( 'word1, word2, word3', [ ("skypro", "s", True), ("123","123", True), ("1 2 3", "1 2 3", True)] )
def test_contains(word1, word2, word3):
    stringutils = StringUtils()
    res = stringutils.contains(word1, word2)
    assert res == word3

@pytest.mark.parametrize( 'word1, word2, word3', [ ( " ", " ", True), ( "", "", True), (None, None, True) ] )
@pytest.mark.xfail
def test_contains_negative(word1, word2, word3):
    stringutils = StringUtils()
    res = stringutils.contains(word1, word2)
    assert res == word3

@pytest.mark.parametrize( 'word1, word2, word3', [ ("skypro", "s", "kypro"), ("123","123", ""), ("1 2 3", "1 2 3", "") ] )
def test_delete_symbol(word1, word2, word3):
    stringutils = StringUtils()
    res = stringutils.delete_symbol(word1, word2)
    assert res == word3

@pytest.mark.parametrize( 'word1, word2, word3', [ ( " ", " ", ""), ( "", "", ""), (None, None, "") ] )
@pytest.mark.xfail
def test_delete_symbol_negative(word1, word2, word3):
    stringutils = StringUtils()
    res = stringutils.delete_symbol(word1, word2)
    assert res == word3

@pytest.mark.parametrize( 'word1, word2, word3', [ ("skypro", "s", True), ("123","123", True), ("1 2 3", "1 2 3", True) ] )
def test_starts_with(word1, word2, word3):
    stringutils = StringUtils()
    res = stringutils.starts_with(word1, word2)
    assert res == word3

@pytest.mark.parametrize( 'word1, word2, word3', [ ( " ", " ", True), ( "", "", True), (None, None, True) ] )
@pytest.mark.xfail
def test_starts_with_negative(word1, word2, word3):
    stringutils = StringUtils()
    res = stringutils.starts_with(word1, word2)
    assert res == word3

@pytest.mark.parametrize( 'word1, word2, word3', [ ("skypro", "o", True), ("123","123", True), ("1 2 3", "1 2 3", True) ] )
def test_end_with(word1, word2, word3):
    stringutils = StringUtils()
    res = stringutils.end_with(word1, word2)
    assert res == word3

@pytest.mark.parametrize( 'word1, word2, word3', [ ( " ", " ", True), ( "", "", True), (None, None, True) ] )
@pytest.mark.xfail
def test_end_with_negative(word1, word2, word3):
    stringutils = StringUtils()
    res = stringutils.end_with(word1, word2)
    assert res == word3

@pytest.mark.parametrize( 'word1, word2', [ ("skypro", False), ("123", False), ("1 2 3", False) ] )
def test_is_empty(word1, word2):
    stringutils = StringUtils()
    res = stringutils.is_empty(word1)
    assert res == word2

@pytest.mark.parametrize( 'word1, word2', [  ( " ", True), ( "", True), (None, False) ] )
@pytest.mark.xfail
def test_is_empty_negative(word1, word2):
    stringutils = StringUtils()
    res = stringutils.is_empty(word1)
    assert res == word2

@pytest.mark.parametrize( 'word1, word2', [ (["Sky", "Pro"], "Sky, Pro"), (["123", "123"], "123, 123"), (["1 2 3", "1 2 3"], "1 2 3, 1 2 3") ] )
def test_list_to_string(word1, word2):
    stringutils = StringUtils()
    res = stringutils.list_to_string(word1)
    assert res == word2

@pytest.mark.parametrize( 'word1, word2', [ ( [" "], " "), ( [""], ""), ([None], None) ] )
@pytest.mark.xfail
def test_list_to_string_negative(word1, word2):
    stringutils = StringUtils()
    res = stringutils.list_to_string(word1)
    assert res == word2
