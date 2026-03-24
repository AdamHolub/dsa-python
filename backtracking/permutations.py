def permutations(nums):
    
    """
    Time Complexity: O(n!)
    Space Complexity: O(n)
    """
    
    result = []
    
    def backtrack(path, used):
        if len(path) == len(nums):
            result.append(path[:])
            return
        
        for i in range(len(nums)):
            if used[i]:
                continue
            
            used[i] = True
            path.append(nums[i])
            
            backtrack(path, used)
            
            path.pop()
            used[i] = False
    
    backtrack([], [False] * len(nums))
    return result

nums = [1,6,7,8]

print(permutations(nums))