def validate(pushed, popped):
    # Проверка на длину последовательности
    if len(pushed) != len(popped):
        return False
    
    stack = []
    # Индекс для отслеживания позиции в popped
    j = 0

    for num in pushed:
        stack.append(num)
        # Пока стек не пуст и верхний элемент равен текущему элементу в popped
        while stack and j < len(popped) and stack[-1] == popped[j]:
            stack.pop()
            j += 1
    # Если все элементы из popped были обработаны, возвращаем True
    return j == len(popped)


def validate_tests():

    assert validate([1, 2, 3, 4, 5], [1, 3, 5, 4, 2]) == True
    assert validate([1, 2, 3], [3, 1, 2]) == False
    assert validate([], []) == True
    assert validate([1], [1]) == True
    assert validate([1], [2]) == False
    assert validate([1, 2, 3], [3, 2, 1]) == True
    assert validate([1, 2, 3, 4], [4, 3, 2, 1]) == True
    assert validate([2, 1, 0, 3], [0, 3, 2, 1]) == False
    assert validate([0, 1, 2, 3], [0, 2, 1, 3]) == True
    assert validate([1, 2, 3], [1, 2]) == False

    # Тест с большими данными
    n = 1000
    pushed = list(range(n))
    popped = list(range(n))
    assert validate(pushed, popped) == True

    print('Тесты пройдены')

if __name__ == '__main__':
    validate_tests()