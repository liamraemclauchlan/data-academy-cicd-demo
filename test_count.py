import count_vowels

def test_count_0():
    total = count_vowels.count("bcdfghjklmnpqrstvwxy")
    for vowel in total:
        assert total[vowel] == 0

def test_count_1():
    total = count_vowels.count("aeiou")
    for vowel in total:
        assert total[vowel] == 1

def test_count_x():
    total = count_vowels.count("Hello World")
    assert total["a"] == 0
    assert total["e"] == 1
    assert total["i"] == 0
    assert total["o"] == 2
    assert total["u"] == 0
