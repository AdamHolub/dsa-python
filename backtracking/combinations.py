def combination_sum(candidates, target):
    
    """
    Time Complexity: O(2^t) t - target
    Space Complexity: O(t)
    """
    
    result = []
    
    def backtrack(start, path, remaining):
        if remaining == 0:
            result.append(path[:])
            return
        
        if remaining < 0:
            return
        
        for x in range(start, len(candidates)):
            path.append(candidates[x])
            
            backtrack(x, path, remaining-candidates[x])
            
            path.pop()
    
    backtrack(0, [], target)
    return result

print(combination_sum([2,3,6,7,1], 7))
