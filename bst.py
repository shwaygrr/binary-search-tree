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
        