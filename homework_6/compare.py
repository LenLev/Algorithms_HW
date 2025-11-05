import time
from random import randint

def timing_decorator(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        wrapper.execution_time = end - start
        return result
    return wrapper

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)

def mergesort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = mergesort(arr[:mid])
    right = mergesort(arr[mid:])
    
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

@timing_decorator
def quicksort_timed(arr):
    return quicksort(arr)

@timing_decorator
def mergesort_timed(arr):
    return mergesort(arr)

# Тесты
def tests():
    test_cases = [
        [3, 1, 4, 1, 5, 9, 2, 6],
        [],
        [1],
        list(range(100)),
        list(range(100, 0, -1))
    ]
    
    for test in test_cases:
        expected = sorted(test)
        assert quicksort(test[:]) == expected
        assert mergesort(test[:]) == expected
    
    print("Производительность:")
    
    # Случайные данные
    random_data = [randint(0, 10000) for _ in range(10000)]
    quicksort_timed(random_data[:])
    mergesort_timed(random_data[:])
    print(f"Случайные: Q={quicksort_timed.execution_time:.4f}, M={mergesort_timed.execution_time:.4f}")
    
    # Отсортированные данные
    sorted_data = list(range(10000))
    quicksort_timed(sorted_data[:])
    mergesort_timed(sorted_data[:])
    print(f"Отсортированные: Q={quicksort_timed.execution_time:.4f}, M={mergesort_timed.execution_time:.4f}")

if __name__ == "__main__":
    tests()