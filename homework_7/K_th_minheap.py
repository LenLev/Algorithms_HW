# без использования heapq
def sift_up(a, i):
    while i > 0:
        p = (i - 1) // 2
        if a[p] <= a[i]:
            break
        a[p], a[i] = a[i], a[p]
        i = p

def sift_down(a, i, n):
    while True:
        l = 2*i + 1
        r = l + 1
        smallest = i
        if l < n and a[l] < a[smallest]:
            smallest = l
        if r < n and a[r] < a[smallest]:
            smallest = r
        if smallest == i:
            break
        a[i], a[smallest] = a[smallest], a[i]
        i = smallest

def heap_push(a, x):
    a.append(x)
    sift_up(a, len(a)-1)

def heap_pop(a):
    a[0], a[-1] = a[-1], a[0]
    x = a.pop()
    if a:
        sift_down(a, 0, len(a))
    return x

def kth_largest_noheapq(nums, k):
    h = []
    for x in nums:
        if len(h) < k:
            heap_push(h, x)
        else:
            if x > h[0]:
                heap_pop(h)
                heap_push(h, x)
    return h[0]

# с использованием heapq 
import heapq
def kth_largest_heapq(nums, k):
    h = []
    for x in nums:
        if len(h) < k:
            heapq.heappush(h, x)
        else:
            if x > h[0]:
                heapq.heapreplace(h, x)
    return h[0]

def tests():
    assert kth_largest_noheapq([3,2,1,5,6,4], 2) == 5
    assert kth_largest_heapq([3,2,1,5,6,4], 2) == 5

    assert kth_largest_noheapq([3,2,3,1,2,4,5,5,6], 4) == 4
    assert kth_largest_heapq([3,2,3,1,2,4,5,5,6], 4) == 4

    assert kth_largest_noheapq([1], 1) == 1
    assert kth_largest_heapq([1], 1) == 1

    assert kth_largest_noheapq([9,8,7,6], 1) == 9
    assert kth_largest_heapq([9,8,7,6], 1) == 9

    assert kth_largest_noheapq([5,5,5,5,5], 3) == 5
    assert kth_largest_heapq([5,5,5,5,5], 3) == 5

    print("успех")

if __name__ == "__main__":
    tests()