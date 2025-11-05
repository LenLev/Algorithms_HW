def find_kth_largest(nums, k):
    def quickselect(left, right, target_index):
        pivot_index = partition(left, right)
        
        if pivot_index == target_index:
            return nums[pivot_index]
        elif pivot_index < target_index:
            return quickselect(pivot_index + 1, right, target_index)
        else:
            return quickselect(left, pivot_index - 1, target_index)
    
    def partition(left, right):
        pivot = nums[right]
        i = left
        for j in range(left, right):
            if nums[j] <= pivot:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
        nums[i], nums[right] = nums[right], nums[i]
        return i
    
    return quickselect(0, len(nums) - 1, len(nums) - k)


def tests():
    assert find_kth_largest([10, 7, 11, 5, 2, 9], 3) == 9

    assert find_kth_largest([4, 4, 4, 4, 4], 2) == 4

    assert find_kth_largest([1, 2, 3, 4, 5, 6], 1) == 6

    assert find_kth_largest([9, 8, 7, 6, 5], 5) == 5

    assert find_kth_largest([-10, -3, 0, 5, 2, -1], 2) == 2

    print("Успех")

if __name__ == "__main__":
    tests()