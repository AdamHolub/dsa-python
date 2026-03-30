def generate_parentheses(n):
    
    """
    Time Complexity: O(2^n)
    Space Complexity: O(n)
    """
    
    result = []
    
    def backtrack(curr, open, close):
        if len(curr) == 2 * n:
            result.append(curr)
            return

        if open < n:
            backtrack(curr + "(", open + 1, close)

        if close < open:
            backtrack(curr + ")", open, close + 1)
    
    backtrack("", 0, 0)
    
    return result

print(generate_parentheses(5))

