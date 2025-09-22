def palindrome(number):
    reversed_number = 0
    #исключение ошибок в случае отрицательных чисел
    if number < 0:
        number = -number
    #сохранение оригинального числа для проверки
    original = number
    
    while number > 0:
        digit = number % 10
        reversed_number = reversed_number * 10 + digit
        number = number // 10
    if original == reversed_number:
        return 'True'
    else:
        return 'False'

def test_palindrome():
    assert palindrome(31) == 'False'
    
    assert palindrome(131) == 'True'

    assert palindrome(5) == 'True'

    assert palindrome(0) == 'True'

    assert palindrome(-31) == 'False'

    assert palindrome(-808) == 'True'

test_palindrome()