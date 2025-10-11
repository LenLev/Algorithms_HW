def group_anagrams(strs):
    anagrams = {}
    
    for word in strs:
        sorted_words = ''.join(sorted(word))
        
        if sorted_words in anagrams:
            anagrams[sorted_words].append(word)
        else:
            anagrams[sorted_words] = [word]
    
    return list(anagrams.values())


# Тесты
def test_group_anagrams():
    
    result1 = group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
    expected1 = [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]]
    assert sorted([sorted(group) for group in result1]) == sorted([sorted(group) for group in expected1])
    
    # Пустой список
    result2 = group_anagrams([])
    assert result2 == []
    
    # Одно слово
    result3 = group_anagrams(["pizza"])
    assert result3 == [["pizza"]]
    
    # Слова разной длины
    result4 = group_anagrams(["a", "b", "ab", "ba", "abc"])
    expected4 = [["a"], ["b"], ["ab", "ba"], ["abc"]]
    assert sorted([sorted(group) for group in result4]) == sorted([sorted(group) for group in expected4])
    
    # Только анаграммы
    result5 = group_anagrams(["кот", "ток", "окт"])
    expected5 = [["кот", "ток", "окт"]]
    assert sorted(result5[0]) == sorted(expected5[0])
    
    print("Успех")


if __name__ == "__main__":
    test_group_anagrams()
