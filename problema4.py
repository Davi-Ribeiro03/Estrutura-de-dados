from binTree import Node

def morrisPre(root):
    current = root
    while current:
        if not current.left:
            print(current.data, end=" ")
            current = current.right
        else:
            predecessor = current.left
            while predecessor.right and predecessor.right != current:
                predecessor = predecessor.right
            
            if not predecessor.right:
                print(current.data, end=" ")  
                predecessor.right = current
                current = current.left
            else:
                predecessor.right = None
                current = current.right
                



node = Node(1)
node.setLeft(2)
node.setRight(4)
node.left.setLeft(5)
node.left.setRight(3)
node.left.left.setLeft(6)

morrisPre(node)




















# node = Node(10)
# node.setLeft(5)
# node.setRight(2)
# node.right.setLeft(4)
# node.right.setRight(8)
# node.left.setLeft(1)
# node.left.setRight(3)