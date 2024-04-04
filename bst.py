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
    
    #build tree
    def buildTree(self, arr):
        def _buildTree(arr):
            if not arr:
                return None
            mid = len(arr) // 2
            root = TreeNode(arr[mid])
            root.left = _buildTree(arr[:mid])
            root.right = _buildTree(arr[mid+1:])
            return root
        arr.sort()
        self.root = _buildTree(arr)

    # Print tree https://stackoverflow.com/a/72497198/23355472
    def printTree(self):
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
    
    #search for key
    def search(self, value):
        #recursive search function (dont want to give access to node_count param)
        def _search(node, val, node_count):
            if not node:
                print(f'Node {node_count} does not contain key {val}')
                return None
            if val == node.value:
                print(f'Node {node_count} contains key {val}')
                return node #can also return node_count
            elif val < node.value:
                return _search(node.left, val, node_count * 2)
            elif val > node.value:
                return _search(node.right, val, node_count * 2 + 1)

        return _search(self.root, value, 1)

    #insert node
    def insert(self, value):
        parent = None
        child = self.root

        #find the parent node of insert node
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

    #parent of existing node
    def parent(self, value):
        parent = None
        child = self.root

        while child is not None:
            if value == child.value:
                if parent:
                    # print(f'Parent of {value} is node with key {parent.value}')
                    return parent
                else:
                    # print(f'{value} is the root node, it has no parent.')
                    return None
            parent = child
            if value < child.value:
                child = child.left
            else:
                child = child.right

        print(f'{value} is not present in the tree.')
        return None
    
    #insert node
    def delete(self, value):
        #algorithms from book
        def treeMin(val):
            root = self.search(val)
            if root is None:
                return None
            current = root
            while current.left is not None:
                current = current.left
            return current
        
        def treeMax(val):
            node = self.search(val)
            if node is None:
                return None
            current = node
            while current.right is not None:
                current = current.right
            return current

        def successor(val):
            val_node = self.search(val)
            if val_node is None:
                return None
            if val_node.right is not None: #return min of right subtree
                return treeMin(val_node.right.value)
            
            #if not right subtree
            parent = self.parent(val_node.value)
            while parent is not None and val_node == parent.right:
                val_node = parent
                parent = self.parent(successor.value)
            return parent
        
        def predecessor(val):
            node = self.search(val)

            if node.left is not None:
                return(treeMax(node.left.value))
            parent = self.parent(node.value)
            while parent is not None and node == parent.left:
                node = parent
                parent = self.parent(parent.value)
            return parent
        
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
                    successor = treeMin(root.right.value)
                    root.value = successor.value
                    root.right = _delete(successor.value, root.right)
            return root

        if self.search(value) is not None:
            self.root = _delete(value, self.root)
            self.printTree()
        else:
            print("Node does not exist")    