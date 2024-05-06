from bst import *

if __name__ == '__main__':

  arr = [2, 6, 9, 3, 1, 9, 0, 4, 5]


  # build and print tree
  tree = BinarySearchTree(arr)
  tree.printTree()

  # search for node of key 6
  tree.search(9) #search for existing node
  tree.search(10) #search for non existent node

  #insert new nodes
  tree.insert(12)
  tree.insert(47)
  tree.insert(4)

  #delete nodes
  tree.delete(6)
  tree.delete(47)
  tree.delete(100) #delete non existing node