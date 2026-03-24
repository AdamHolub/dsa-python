from collections import deque

q = deque()
q.append(1)
q.append(2)
q.popleft() # 1

class MovingAverage:

    """
    Time Complexity: O(1)
    Space Complexity: O(k) k - window space
    """
    
    def __init__(self, size):
        self.queue = deque()
        self.size = size
        self.sum = 0
        
    def next(self, val):
        self.queue.append(val)
        self.sum += val
        
        if len(self.queue) > self.size:
            self.sum -= self.queue.popleft()
        
        return self.sum / len(self.queue)

av = MovingAverage(5)

print(av.next(5))
print(av.next(15))
print(av.next(50))
