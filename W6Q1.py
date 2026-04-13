def minimum(nums):
    if len(nums) == 0:
        return None
    
    m = nums[0]
    for n in nums:
        if n < m:
            m = n
    return m

def avg(nums):
    if len(nums) == 0:
        return None
    
    total = 0
    for n in nums:
        total += n

    return total / len(nums)

def median(nums):
    if len(nums) == 0:
        return None
    
    nums = sorted(nums)
    n = len(nums)
    mid = n // 2

    if n % 2 == 1:
        return nums[mid]
    else:
        return (nums[mid - 1] + nums[mid]) / 2
    
def normalize(x, lo, hi):
    if hi == lo:
        return None
    return (x - lo) / (hi - lo)

def clamp(x, lo, hi):
    if x < lo:
        return lo
    if x > hi:
        return hi
    return x

assert minimum([3,1,5]) == 1
assert minimum([10]) == 10
assert minimum([]) == None

assert avg([2,4,6]) == 4
assert avg([5]) == 5
assert avg([]) == None

assert median([1,2,3]) == 2
assert median([1,2,3,4]) == 2.5
assert median([5]) == 5

assert normalize(5,0,10) == 0.5
assert normalize(0,0,10) == 0
assert normalize(10,0,10) == 1

assert clamp(5,0,10) == 5
assert clamp(-3,0,10) == 0
assert clamp(20,0,10) == 10
