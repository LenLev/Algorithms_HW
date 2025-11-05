import time
from collections import deque

def timing_decorator(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        wrapper.execution_time = time.time() - start
        return result
    return wrapper

def quicksort_iterative(arr):
    if len(arr) <= 1:
        return arr
    
    stack = [(0, len(arr) - 1)]
    result = arr[:]
    
    while stack:
        low, high = stack.pop()
        if low >= high:
            continue
            
        pivot = result[high]
        i = low
        for j in range(low, high):
            if result[j] <= pivot:
                result[i], result[j] = result[j], result[i]
                i += 1
        result[i], result[high] = result[high], result[i]
        
        stack.append((low, i - 1))
        stack.append((i + 1, high))
    
    return result

def mergesort_iterative(arr):
    if len(arr) <= 1:
        return arr
        
    result = arr[:]
    size = 1
    
    while size < len(result):
        for start in range(0, len(result), size * 2):
            mid = min(start + size, len(result))
            end = min(start + 2 * size, len(result))
            
            left = result[start:mid]
            right = result[mid:end]
            
            merged = []
            i = j = 0
            while i < len(left) and j < len(right):
                if left[i] < right[j]:
                    merged.append(left[i])
                    i += 1
                else:
                    merged.append(right[j])
                    j += 1
            merged.extend(left[i:])
            merged.extend(right[j:])
            result[start:start + len(merged)] = merged
            
        size *= 2
    
    return result

@timing_decorator
def quicksort_iterative_timed(arr):
    return quicksort_iterative(arr)

@timing_decorator
def mergesort_iterative_timed(arr):
    return mergesort_iterative(arr)

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
        assert quicksort_iterative(test[:]) == expected
        assert mergesort_iterative(test[:]) == expected
    
    print("Производительность:")
    from random import randint
    
    random_data = [randint(0, 10000) for _ in range(10000)]
    quicksort_iterative_timed(random_data[:])
    mergesort_iterative_timed(random_data[:])
    print(f"Случайные: Q={quicksort_iterative_timed.execution_time:.4f}, M={mergesort_iterative_timed.execution_time:.4f}")
    
    sorted_data = list(range(10000))
    quicksort_iterative_timed(sorted_data[:])
    mergesort_iterative_timed(sorted_data[:])
    print(f"Отсортированные: Q={quicksort_iterative_timed.execution_time:.4f}, M={mergesort_iterative_timed.execution_time:.4f}")

if __name__ == "__main__":
    tests()