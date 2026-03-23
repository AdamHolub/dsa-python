class Stack:
    def __init__(self):
        self.stack = []
    
    def push(self, val):
        self.stack.append(val)
    
    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        return None
    
    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        return None
    
    def is_empty(self):
        return len(self.stack) == 0

s = Stack()
s.push(3)
s.push(6)
s.push(4)
print(s.pop())
print(s.peek())
    
def is_valid(s):
    stack = []
    mapping = {
        ")": "(",
        "]": "[",
        "}": "{"
    }
    
    for char in s:
        if char in mapping:
            top = stack.pop() if stack else "#"
            
            if mapping[char] != top:
                return False
        else:
            stack.append(char)
    return not stack

print(is_valid("({{}})")) # True
print(is_valid("({{)")) # False


class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []
    
    def push(self, val):
        self.stack.append(val)
        
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)
    
    def pop(self):
        if self.stack:
            val = self.stack.pop()
            if val == self.min_stack[-1]:
                self.min_stack.pop()
    
    def top(self):
        return self.stack[-1] if self.stack else None
    
    def get_min(self):
        return self.min_stack[-1] if self.min_stack else None
    
m = MinStack()
m.push(3)
m.push(2)
m.push(9)
m.push(8)
m.pop()
print(m.top())
print(m.get_min())

