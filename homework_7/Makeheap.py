def _sift_down(arr, i, n):
    while True:
        left = 2*i + 1
        right = 2*i + 2
        smallest = i

        if left < n and arr[left] < arr[smallest]:
            smallest = left
        if right < n and arr[right] < arr[smallest]:
            smallest = right

        if smallest == i:
            break

        arr[i], arr[smallest] = arr[smallest], arr[i]
        i = smallest


# O(n log n)
def makeheap_n_log_n(arr):
    n = len(arr)

    for i in range(n):
        j = i
        while j > 0:
            parent = (j - 1) // 2
            if arr[j] < arr[parent]:
                arr[j], arr[parent] = arr[parent], arr[j]
                j = parent
            else:
                break
    return arr


# O(n)
def makeheap(arr):
    n = len(arr)
    for i in range(n//2 - 1, -1, -1):
        _sift_down(arr, i, n)
    return arr


def tests():
    def is_heap(a):
        n = len(a)
        for i in range(n):
            l = 2*i+1
            r = 2*i+2
            if l < n and a[i] > a[l]:
                return False
            if r < n and a[i] > a[r]:
                return False
        return True

    arr1 = [5,4,3,2,1]
    assert is_heap(makeheap_n_log_n(arr1.copy()))
    assert is_heap(makeheap(arr1.copy()))

    arr2 = [9,1,8,2,7,3,6,4,5]
    assert is_heap(makeheap_n_log_n(arr2.copy()))
    assert is_heap(makeheap(arr2.copy()))

    assert is_heap(makeheap_n_log_n([].copy()))
    assert is_heap(makeheap([].copy()))

    arr4 = [7]*10
    assert is_heap(makeheap_n_log_n(arr4.copy()))
    assert is_heap(makeheap(arr4.copy()))

    print("Успех")
    
if __name__ == "__main__":
    tests()

# Сравнение скорости работы двух алгоритмов
import time
import random

big = [random.randint(0,10**9) for _ in range(20000)]

a1 = big.copy()
t1 = time.time()
makeheap_n_log_n(a1)
t1 = time.time() - t1

a2 = big.copy()
t2 = time.time()
makeheap(a2)
t2 = time.time() - t2

print(f"n log n: {t1:.4f}")
print(f"n: {t2:.4f}")
print(f"ratio: {t1 / t2:.4f}")
