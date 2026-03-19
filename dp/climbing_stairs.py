def climbing_stairs(n):
    
    """
    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    
    if n <= 0:
        return 0
    if n == 1:
        return 1
    if n == 2:
        return 2
    dp = [0] * (n + 1)
    dp[1] = 1
    dp[2] = 2
    for x in range(3, n + 1):
        dp[x] = dp[x-1] + dp[x-2]
    return dp[n]

def climbing_stairs_recursive(n):
    
    """
    Time Complexity: O(2^n)
    Space Complexity: O(n)
    """
    
    if n <= 0:
        return 0
    if n == 1:
        return 1
    if n == 2:
        return 2
    return climbing_stairs_recursive(n-1) + climbing_stairs_recursive(n-2)

def climbing_stairs_dp(n):
    
    """
    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    
    if n <= 0:
        return 0
    if n == 1:
        return 1
    if n == 2:
        return 2
    dp = [1, 2]
    for x in range(2, n + 1):
        dp.append(dp[x-1] + dp[x-2])
    return dp[n-1]

def climbing_stairs_memo(n, memo=None):
    
    """
    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    
    if memo is None:
        memo = {}
    if n in memo:
        return memo[n]
    if n <= 0:
        return 0
    if n == 1:
        return 1
    if n == 2:
        return 2
    memo[n] = climbing_stairs_memo(n-1, memo) + climbing_stairs_memo(n-2, memo)
    return memo[n]

def climbing_stairs_optimized(n):
    
    """
    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    
    if n <= 0:
        return 0
    if n == 1:
        return 1
    if n == 2:
        return 2
    a, b = 1, 2
    for x in range(3, n + 1):
        current = a + b
        a, b = b, current
    return b


if __name__ == "__main__":
    n = 6
    print("Number of ways to climb", n, "stairs:", climbing_stairs(n))
    print("Number of ways to climb", n, "stairs (recursive):", climbing_stairs_recursive(n))
    print("Number of ways to climb", n, "stairs (dp):", climbing_stairs_dp(n))
    print("Number of ways to climb", n, "stairs (memo):", climbing_stairs_memo(n))
    print("Number of ways to climb", n, "stairs (optimized):", climbing_stairs_optimized(n))
