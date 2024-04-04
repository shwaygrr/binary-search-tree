import random

#random array for testing
def randomArr(size, range_param=10):
  L = range(range_param)
  return [random.choice(L) for _ in range(size)]


arr = [2, 6, 9, 3, 1, 9, 0, 4, 1, 5]
print(arr.sort)

#build and print tree
tree = BinarySearchTree(arr)
tree.printTree()

#search for node of key 6
tree.search(6) #search for existing node
tree.search(10) #search for non existent node

#insert new nodes
tree.insert(10)
tree.insert(47)
tree.insert(4)

#delete nodes
tree.delete(6)
tree.delete(47)
tree.delete(100) #delete non existing node