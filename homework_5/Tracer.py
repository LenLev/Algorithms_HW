def tracer(func):
    depth = 0
    def wrapper(*args, **kwargs):
        nonlocal depth
        print('  ' * depth + f'-> {func.__name__}({args[0]})')
        depth += 1
        result = func(*args, **kwargs)
        depth -= 1
        print('  ' * depth + f'<- {result}')
        return result
    return wrapper

@tracer
def factorial(n):
    return 1 if n == 0 else n * factorial(n - 1)

@tracer
def fibonacci(n):
    return n if n <= 1 else fibonacci(n - 1) + fibonacci(n - 2)

def test_tracer():
    assert factorial(5) == 120
    assert fibonacci(7) == 13
    print('Успех')

if __name__ == "__main__":
    test_tracer()
