class TreeNode:
    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self, arr=None):
        self.root = None
        if arr:
            self.buildTree(arr)
    
    def buildTree(self, arr):
        arr.sort()
        self.root = self._buildTree(arr)
    
    def _buildTree(self, arr):
        if not arr:
            return None
        mid = len(arr) // 2
        root = TreeNode(arr[mid])
        root.left = self._buildTree(arr[:mid])
        root.right = self._buildTree(arr[mid+1:])
        return root