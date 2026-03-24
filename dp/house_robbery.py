def robbery(nums):
    
    """
    Time Complexity: O(1)
    Space Complexity: O(k)
    """
    
    if not nums:
        return 0
    if len(nums) == 1:
        return nums[0]

    dp = [0] * len(nums)
    dp[0] = nums[0]
    dp[1] = max(nums[0], nums[1])
    
    for x in range(2, len(nums)):
        dp[x] = max(dp[x-1], nums[x] + dp[x-2])
    
    return dp[-1]

def robbery_optim(nums):
    
    """
    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    
    prev2 = 0
    prev1 = 0
    for num in nums:
        curr = max(prev1, num + prev2)
        prev2 = prev1
        prev1 = curr
    
    return prev1


nums = [2, 7, 9, 3, 1]

print(f"Robbery example dp: {robbery(nums)}")
print(f"Robbery examplce optimize: {robbery_optim(nums)}")