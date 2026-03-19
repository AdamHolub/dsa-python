def fib(n):
    
    """
    Time Complexity: O(2^n) - Exponential time due to repeated calculations
    Space Complexity: O(n) - Due to the call stack in recursion
    """
    
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)

def fib_memo(n, memo=None):
    
    """
    Time Complexity: O(n) - Each Fibonacci number is calculated once
    Space Complexity: O(n) - Due to the memoization dictionary and call stack
    """
    
    if memo is None:
        memo = {}
    if n in memo:
        return memo[n]
    if n <= 1:
        memo[n] = n
        return n
    memo[n] = fib_memo(n-1, memo) + fib_memo(n-2, memo)
    return memo[n]

def fib_tab(n):
    
    """
    Time Complexity: O(n) - Each Fibonacci number is calculated once
    Space Complexity: O(n) - Due to the dp array storing Fibonacci numbers up to n
    """
    
    if n <= 1:
        return n
    dp = [0] * (n + 1)
    dp[1] = 1
    for x in range(2, n + 1):
        dp[x] = dp[x-1] + dp[x-2]
    return dp[n]

def fb(n):
    
    """
    Time Complexity: O(n) - Each Fibonacci number is calculated once
    Space Complexity: O(n) - Due to the list storing Fibonacci numbers up to n
    """
    
    res = [0, 1]
    for x in range(2, n + 1):
        res.append(res[x-1] + res[x-2])
    return res[n]

def fib_optimized(n):
    
    """
    Time Complexity: O(n) - Each Fibonacci number is calculated once
    Space Complexity: O(1) - Only a constant amount of space is used to store the last two Fibonacci numbers
    """
    
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b


if __name__ == "__main__":
    
    #for x in range(11):
    #    print(f"fib({x}) = {fib(x)}")
    #    print(f"fib_memo({x}) = {fib_memo(x)}")

    print(fib(10))  # Output: 55
    print(fib_memo(10))  # Output: 55
    print(fib_tab(10))  # Output: 55
    print(fb(10))  # Output: 55
    print(fib_optimized(10))  # Output: 55