class TreeNode:
    def __init__(self, value=None):
        """
        Initializes a TreeNode with the given key.

        Args:
            value: The key to be stored in the node. Default is None.
        """
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self, arr=None):
        """
        Initializes a BinarySearchTree with an optional array to build the tree.

        Args:
            arr: An optional array of values to build the BST. Default is None.
        """
        self.root = None
        if arr:
            self.buildTree(arr)
    
    #build tree from array
    def buildTree(self, arr):
        """
        Builds a BST from the given array.

        Args:
            arr: An array of values to build the BST.
        """
        def _buildTree(arr):
            if not arr:
                return None
            mid = len(arr) // 2
            root = TreeNode(arr[mid])
            root.left = _buildTree(arr[:mid])
            root.right = _buildTree(arr[mid+1:])
            return root
        arr.sort()
        set_arr = list(set(arr))
        print(set_arr)
        self.root = _buildTree(set_arr)

    # Print tree https://stackoverflow.com/a/72497198/23355472
    def printTree(self):
        """
        Prints the BST in a tree-like format.
        """
        #height
        def height(root):
            return 1 + max(height(root.left), height(root.right)) if root else -1
        
        nlevels = height(self.root)
        width = pow(2, nlevels + 1)

        q = [(self.root, 0, width, 'c')]
        levels = []

        while q:
            node, level, x, align = q.pop(0)
            if node:
                if len(levels) <= level:
                    levels.append([])
            
                levels[level].append([node, level, x, align])
                seg = width // (pow(2, level + 1))
                q.append((node.left, level + 1, x - seg, 'l'))
                q.append((node.right, level + 1, x + seg, 'r'))

        for i, l in enumerate(levels):
            pre = 0
            preline = 0
            linestr = ''
            pstr = ''
            seg = width // (pow(2, i + 1))
            for n in l:
                valstr = str(n[0].value)
                if n[3] == 'r':
                    linestr += ' ' * (n[2] - preline - 1 - seg - seg // 2) + '¯' * (seg + seg // 2) + '\\'
                    preline = n[2] 
                if n[3] == 'l':
                    linestr += ' ' * (n[2] - preline - 1) + '/' + '¯' * (seg + seg // 2)  
                    preline = n[2] + seg + seg // 2
                pstr += ' ' * (n[2] - pre - len(valstr)) + valstr
                pre = n[2]
            print(linestr)
            print(pstr)
        #parent of existing node
    
    #search node by key
    def search(self, value):
        """
        Recursive Search for a node with the given key

        Args:
            value: The key to search for.

        Returns:
            The node containing the value if found, else None.
        """
        #recursive search function (dont want to give access to node_count param)
        def _search(node, val, node_count):
            if not node:
                print(f'Tree does not contain key {val}')
                return None
            if val == node.value:
                print(f'Node {node_count} contains key {val}')
                return node #can also return node_count
            elif val < node.value:
                return _search(node.left, val, node_count * 2)
            elif val > node.value:
                return _search(node.right, val, node_count * 2 + 1)

        return _search(self.root, value, 1)

    #parent of existing node by key
    def parent(self, value):
        """
        Iterative search for parent of a node with the given key.

        Args:
            value: The key of the node whose parent is to be found.

        Returns:
            The parent node if found, else None.
        """
        parent = None
        child = self.root

        if self.search(value) is None:
          print(f'{value} is not present in the tree.')
          return None

        while child is not None:
            if value == child.value:
                if parent:
                    print(f'Parent of {value} is node with key {parent.value}')
                    return parent
                else:
                    print(f'{value} is the root node, it has no parent.')
                    return None
            parent = child
            if value < child.value:
                child = child.left
            else:
                child = child.right    

    #insert node by key
    def insert(self, value):
        """
        Iteratively inserts a node with the given value to as a root

        Args:
            value: The value of the node to be inserted.
        """
        if self.search(value) is not None:
            print("Key already exists, Cannot have duplicate keys")
        else:
            parent = None
            child = self.root

            #find the parent node of new node
            while child is not None:
                parent = child
                if value < child.value:
                    child = child.left
                else:
                    child = child.right

            #insert node
            if parent is None: #tree empty
                self.root = TreeNode(value)
            elif value < parent.value: #insert to left child
                parent.left = TreeNode(value)
            else: #insert to right child
                parent.right = TreeNode(value)
            print(value, " inserted")
            self.printTree()
    
    #min of subtree by root key 
    def treeMin(self, subtree_key=None):
        """
        Finds the minimum value node in the subtree rooted at the node with given key.

        Args:
            subtree_key: The key of the root of the subtree. Default is root.

        Returns:
            The node with the minimum value in the subtree if found, else None.
        """
        if subtree_key is None:
            subtree_key = self.root.value
        subtree_root = self.search(subtree_key)
        if subtree_root is None:
            print(f"Key {subtree_key} does not exist")
            return None
        current = subtree_root
        while current.left is not None:
            current = current.left
        print(f"Min of subtree with root {subtree_key} is {current.value}")
        return current
        
    #max of subtree by root key
    def treeMax(self, subtree_key=None):
        """
        Finds the maximum value node in the subtree rooted at the node with given key.

        Args:
            subtree_key: The key of the root of the subtree. Default is root.

        Returns:
            The node with the maximum value in the subtree if found, else None.
        """
        if subtree_key is None:
            subtree_key = self.root.value
        subtree_root = self.search(subtree_key)
        if subtree_root is None:
            print(f"Key {subtree_key} does not exist")
            return None
        current = subtree_root
        while current.right is not None:
            current = current.right
        print(f"Max of subtree with root {subtree_key} is {current.value}")
        return current
    
    #successor of existing node by key
    def successor(self, node_key):
        """
        Finds the successor of a node with the given key.

        Args:
            node_key: The key of the node whose successor is to be found.

        Returns:
            The successor node if found, else None.
        """
        node = self.search(node_key)
        if node is None:
            print(f"Key {node_key} does not exist")
            return None
        
        print("Succcessor: ")
        if node.right is not None: #return min of right subtree
            return self.treeMin(node.right.value)
        
        #if no right subtree
        parent = self.parent(node.value)
        while parent is not None and node == parent.right:
            node = parent
            parent = self.parent(parent.value)
        return parent
    
    #predecessor of existing node by key
    def predecessor(self, node_key):
        """
        Finds the predecessor of a node with the given key in the BST.

        Args:
            node_key: The key of the node whose predecessor is to be found.

        Returns:
            The predecessor node if found, else None.
        """
        node = self.search(node_key)
        if node is None:
            print(f"Key {node_key} does not exist")
            return None
        
        print("Predecesssor: ")
        if node.left is not None:
            return(self.treeMax(node.left.value))
        
        #if no left subtree
        parent = self.parent(node.value)
        while parent is not None and node == parent.left:
            node = parent
            parent = self.parent(parent.value)
        return parent
    
    #delete node by key
    def delete(self, value):
        """
        Deletes the node with the given value from the BST.

        Args:
            value: The value of the node to be deleted.
        """
        def _delete(val, root=None):
            if root is None:
                return None

            if val < root.value:
                root.left = _delete(val, root.left)
            elif val > root.value:
                root.right = _delete(val, root.right)
            else:
                if root.left is None and root.right is None:
                    return None
                elif root.right is None:
                    return root.left
                elif root.left is None:
                    return root.right
                else:
                    #find successor to replace the node
                    successor = self.treeMin(root.right.value)
                    root.value = successor.value
                    root.right = _delete(successor.value, root.right)
            return root

        if self.search(value) is not None:
            self.root = _delete(value, self.root)
            print(f'{value} deleted')
            self.printTree()
        else:
            print("Node does not exist")    