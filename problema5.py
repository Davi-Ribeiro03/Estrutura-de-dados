from binTree import Node
from stack import Stack

node = Node(10)
node.setLeft(5)
node.setRight(2)
node.right.setLeft(4)
node.right.setRight(8)
node.left.setLeft(1)
node.left.setRight(3)

def contaNos(root):
    if not root: return 0

    return 1 + contaNos(root.left) + contaNos(root.right)

# print(contaNos(node))

def maiorValor(root):
    if not root: return None
    s = Stack(10)
    s.push(root)
    maiorValor = 0

    while not s.isEmpty():
        n = s.pop()
        maiorValor = n.data if maiorValor < n.data else maiorValor

        if n.right: s.push(n.right)
        if n.left: s.push(n.left)

    return maiorValor

# print(maiorValor(node))


def encontraValor(root,valor):
    if not root: return False 
    if root.data == valor: return True
   

    return encontraValor(root.left,valor) or encontraValor(root.right, valor)


print(encontraValor(node,12))