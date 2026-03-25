def can_finish(numCourses, prerequisites):
    
    """
    Time Complexity: O(V + E)
    Space COmplexity: O(V + E)
    """
    
    graph = { i: [] for i in range(numCourses)}
    
    for course, prereq in prerequisites:
        graph[course].append(prereq)
        
    visited = set()
    visiting = set()
    
    def dfs(course):
        if course in visiting:
            return False
        
        if course in visited:
            return True
        
        visiting.add(course)
        
        for neighbor in graph[course]:
            if not dfs(neighbor):
                return False
        
        visiting.remove(course)
        visited.add(course)
        
        return True
    
    for course in range(numCourses):
        if not dfs(course):
            return False
    
    return True

print(can_finish(2, [[1,0]]))          # True
print(can_finish(2, [[1,0],[0,1]]))    # False (cycle)