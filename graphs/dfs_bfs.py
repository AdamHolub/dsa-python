from collections import deque

def dfs(graph, node, visited):
    
    """
    Time Complexity: O(V + E) V - number of vertices, E - number of edges
    Space Complexity: O(V) V - number of vertices
    """
    
    if node in visited:
        return
    
    visited.add(node)
    print(f"dfs: {node}")
    
    for neighbor in graph[node]:
        dfs(graph, neighbor, visited)


graph = {
    0:[1,2],
    1:[0,3],
    2:[0],
    3:[1]
}

visited = set()
dfs(graph, 0, visited)

print()

def bfs(graph, start):
    
    """
    Time Complexity: O(V + E) V - number of vertices, E - number of edges
    Space Complexity: O(V) V - number of vertices
    """
    
    visited = set()
    queue = deque([start])
    visited.add(start)
    
    while queue:
        node = queue.popleft()
        print(f"bfs: {node}")
        
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)


graph2 = {
    0:[1,2,3],
    1:[0,3],
    2:[0],
    3:[0,1]
}

start = 2
bfs(graph2, start)
