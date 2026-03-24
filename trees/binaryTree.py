from collections import deque

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    
    @staticmethod
    def preorder(node):
        
        """
        Time Complexity: O(n) n - number of nodes in the tree
        Space Complexity: O(h) h - height of the tree
        """
        
        result = []
        def dfs(node):
            if node is None:
                return
            result.append(node.value)
            dfs(node.left)
            dfs(node.right)
        dfs(node)
        return result
           
    @staticmethod
    def inorder(node):
        
        """
        Time Complexity: O(n) n - number of nodes in the tree
        Space Complexity: O(h) h - height of the tree
        """
        
        result = []
        def dfs(node):
            if node is None:
                return
            dfs(node.left)
            result.append(node.value)
            dfs(node.right)
        dfs(node)
        return result
         
    @staticmethod
    def postorder(node):
        
        """
        Time Complexity: O(n) n - number of nodes in the tree
        Space Complexity: O(h) h - height of the tree
        """
        
        result = []
        def dfs(node):
            if node is None:
                return
            dfs(node.left)
            dfs(node.right)
            result.append(node.value)
        dfs(node)
        return result

    @staticmethod
    def bfs(root):
        
        """
        Time Complexity: O(n) n - number of nodes in the tree
        Space Complexity: O(w) w - max width of the tree
        """
        
        if root is None:
            return []
        result = []
        queue = deque([root])
        while queue:
            current = queue.popleft()
            result.append(current.value)
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)
        return result

    @staticmethod
    def dfs(root):
        
        """
        Time Complexity: O(n) n - number of nodes in the tree
        Space Complexity: O(h) h - height of the tree
        """
        
        if root is None:
            return []
        result = []
        stack = [root]
        while stack:
            current = stack.pop()
            result.append(current.value)
            if current.right:
                stack.append(current.right)
            if current.left:
                stack.append(current.left)
        return result

    @staticmethod
    def height(node):
        
        """
        Time Complexity: O(n) n - number of nodes in the tree
        Space Complexity: O(h) h - height of the tree
        """
        
        if node is None:
            return 0
        left_height = BinaryTree.height(node.left)
        right_height = BinaryTree.height(node.right)
        return max(left_height, right_height) + 1
    

# Binary Tree Example
root = Node(5)
root.left = Node(3)
root.right = Node(8)

root.left.left = Node(1)
root.left.right = Node(4)

root.right.right = Node(9)

print("Preorder:", BinaryTree.preorder(root))
print("Inorder:", BinaryTree.inorder(root))
print("Postorder:", BinaryTree.postorder(root))
print("BFS:", BinaryTree.bfs(root))
print("DFS:", BinaryTree.dfs(root))
print("Height:", BinaryTree.height(root))