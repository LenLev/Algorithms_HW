def palindrome(number):
    reversed_number = 0
    original = number  

    # Разворот числа
    while number > 0:
        digit = number % 10
        reversed_number = reversed_number * 10 + digit
        number = number // 10

    # Сравнение оргинального числа с перевернутым
    if original == reversed_number:
        return 'True'
    else:
        return 'False'

def test_palindrome():
    assert palindrome(31) == 'False'
    
    assert palindrome(131) == 'True'

    assert palindrome(123321) == 'True'

    assert palindrome(5) == 'True' # Число из одной цифры

    assert palindrome(0) == 'True' # Крайнее значение

    assert palindrome(99999999) == 'True' # Крайнее значение

    print('Тесты пройдены')

test_palindrome()