def two_sum(arr, k):
    num_indices = {}
    
    for i, num in enumerate(arr):
        complement = k - num
        
        if complement in num_indices:
            return sorted([num_indices[complement], i])
        
        num_indices[num] = i
    
    return []

# Тесты
def test_two_sum():
    assert two_sum([1, 3, 4, 10], 7) == [1, 2]
    
    assert two_sum([5, 5, 1, 4], 10) == [0, 1]
    
    # Отрицательные числа
    assert two_sum([-3, 1, 8, 13], 5) == [0, 2]
    
    # Пара в конце массива
    assert two_sum([1, 2, 3, 7, 8], 15) == [3, 4]
    
    # Нули
    assert two_sum([0, 4, 3, 0], 0) == [0, 3]
    
    print("Успех")

if __name__ == "__main__":
    test_two_sum()
