import count_vowels

def test_count_0():
    total = count_vowels.count("bcdfghjklmnpqrstvwxy")
    for vowel in total:
        assert total[vowel] == 0

def test_count_1():
    total = count_vowels.count("aeiou")
    for vowel in total:
        assert total[vowel] == 1
