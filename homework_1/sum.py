def max_sum_even(numbers):
    # Инициализация массива
    array = list(map(int, numbers.split()))

    # Решение через делимость на два
    even_sum = sum(digit for digit in array if digit % 2 == 0)

    odd_numbers = [digit for digit in array if digit % 2 == 1]

    odd_numbers.sort(reverse=True)

    # Берем максимальную сумму четного количества нечетных чисел
    odd_sum = 0
    for i in range(0, len(odd_numbers) - len(odd_numbers) % 2, 2):
        odd_sum += odd_numbers[i] + odd_numbers[i + 1]

    return even_sum + odd_sum

def test_max_sum_even():
    assert max_sum_even('5 7 13 2 14') == 36

    assert max_sum_even('3') == 0 # Одна нечетная цифра

    assert max_sum_even('2 4 6') == 12 #все четные

    assert max_sum_even('1 3 5') == 8 # 3,5

    assert max_sum_even('1 1 1') == 2 # Повторяющиеся цифры

    assert max_sum_even('') == 0 # Крайнее значение

    assert max_sum_even('1000000 999999') == 1000000  # Крайнее значение

    print('Тесты пройдены')

test_max_sum_even()