def subsets(nums):
    
    """
    Time Complexity: O(n * 2^n)
    Space Complexity: O(n)
    """
    
    result = []
    
    def backtrack(start, path):
        result.append(path[:])
        
        for i in range(start, len(nums)):
            path.append(nums[i])
            backtrack(i + 1, path)
            path.pop()
    
    backtrack(0, [])
    return result


nums = [1,4,6,4,10]

print(subsets(nums))