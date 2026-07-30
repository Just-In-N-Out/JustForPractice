def count_evens(nums):
    even = 0
    for n in nums:
        if n % 2 == 0:
            even +=1
    return even
            
