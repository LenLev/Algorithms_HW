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
def permute(nums):
    if len(nums) <= 1:
        return [nums]
    res = []
    for i in range(len(nums)):
        for p in permute(nums[:i] + nums[i+1:]):
            res.append([nums[i]] + p)
    return res

def test_permute():
    assert permute([1,2,3]) == [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
    assert permute([0,1]) == [[0,1],[1,0]]
    assert permute([1]) == [[1]]
    assert permute([]) == [[]]
    assert permute([1,1]) == [[1,1],[1,1]]
    print('Успех')

if __name__ == "__main__":
    test_permute()