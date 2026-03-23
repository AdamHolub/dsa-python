from binaryTree import Node

class BinaryTree:
    @staticmethod
    def find_value(node, target):
        if node is None:
            return False
        if node.value == target:
            return True
        return BinaryTree.find_value(node.left, target) or BinaryTree.find_value(node.right, target)
    
    @staticmethod
    def tree_sum(node):
        if node is None:
            return 0
        return (node.value + BinaryTree.tree_sum(node.left) + BinaryTree.tree_sum(node.right))

    @staticmethod
    def count_leaves(node):
        if node is None:
            return 0
        if node.left is None and node.right is None:
            return 1
        return BinaryTree.count_leaves(node.left) + BinaryTree.count_leaves(node.right)
    
    @staticmethod
    def reverse_tree(node):
        
        """
        Time Complexity: O(n) n - number of nodes in the tree
        Space Complexity: O(h) h - height of the tree
        """
        
        if node is None:
            return
        node.left, node.right = node.right, node.left
        BinaryTree.reverse_tree(node.left)
        BinaryTree.reverse_tree(node.right)
        
        return node
    
    @staticmethod
    def same_tree(node1, node2):
        
        """
        Time Complexity: O(n) n - number of nodes in the tree
        Space Complexity: O(h) h - height of the tree
        """
        
        if node1 is None and node2 is None:
            return True
        if node1 is None or node2 is None:
            return False
        if node1.value != node2.value:
            return False
        return BinaryTree.same_tree(node1.left, node2.left) and BinaryTree.same_tree(node1.right, node2.right)

    @staticmethod
    def max_depth(node):
        
        """
        Time Complexity: O(n) n - number of nodes in the tree
        Space Complexity: O(h) h - height of the tree
        """
        
        if node is None:
            return 0
        left_depth = BinaryTree.max_depth(node.left)
        right_depth = BinaryTree.max_depth(node.right)
        return max(left_depth, right_depth) + 1
    
    @staticmethod
    def path_sum(node, target_sum):
        
        """
        Time Complexity: O(n) n - number of nodes in the tree
        Space Complexity: O(h) h - height of the tree
        """
        
        if node is None:
            return False
        if node.left is None and node.right is None:
            return node.value == target_sum
        remaining_sum = target_sum - node.value
        return BinaryTree.path_sum(node.left, remaining_sum) or BinaryTree.path_sum(node.right, remaining_sum)
    
# Binary Tree Example
root = Node(5)
root.left = Node(3)
root.right = Node(8)

root.left.left = Node(1)
root.left.right = Node(4)

root.right.right = Node(9)


print("Find 3:", BinaryTree.find_value(root, 3))  # True
print("Find 10:", BinaryTree.find_value(root, 10))  # False

print("Tree Sum:", BinaryTree.tree_sum(root))

print("Leaf Count:", BinaryTree.count_leaves(root))

#reversed_root = BinaryTree.reverse_tree(root)
#print("Reversed Tree Root Value:", reversed_root.value)
#print("Reversed Tree Left Child Value:", reversed_root.left.value)
#print("Reversed Tree Right Child Value:", reversed_root.right.value)

print("Max Depth:", BinaryTree.max_depth(root))
print("Path Sum (12):", BinaryTree.path_sum(root, 12))