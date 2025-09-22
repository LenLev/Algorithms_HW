def prime(number):
    if number <= 2:
        return 0
    
    # Инициализация
    is_prime = [True] * number
    is_prime[0] = is_prime[1] = False

    # Решение через решето Эратосфена
    for i in range(2, int(number**0.5) + 1):
        if is_prime[i]:
            for j in range(i*i, number, i):
                is_prime[j] = False
    
    return sum(is_prime)

def test_prime():
    assert prime(10) == 4 # 2,3,5,7

    assert prime(2) == 0 # Крайнее значение

    assert prime(3) == 1 # 2

    assert prime(100) == 25 

    print('Тесты пройдены')

test_prime()