# Dada uma pilha de inteiros, reorganize os elementos em uma fila, de tal modo que os elementos da primeira metade da pilha estão intercalados com os elementos da segunda metade da pilha.
from stack import Stack
from lista import Queue

def intercala(stack): 
    size = 0
    listaAuxiliar = Queue()
    lista = Queue()

    while not stack.isEmpty():
       listaAuxiliar.enQueue(stack.pop())
       size += 1
        # 2 3 4 5 6 7 9

    for _ in range(size // 2):
        lista.enQueue(listaAuxiliar.deQueue())
        #  2 3 4
        # 5 6 7 9
      
    for _ in range(size // 2):
        lista.enQueue(lista.deQueue())
        lista.enQueue(listaAuxiliar.deQueue())
       

    if( size % 2 != 0):
        lista.enQueue(listaAuxiliar.deQueue())
      

    lista.printQueue()
    

stack = Stack(10)
stack.push(7)
stack.push(6)
stack.push(5)
stack.push(4)
stack.push(3)
stack.push(2)

intercala(stack)

# 2 3 4 5 6 7 9
#result: 2 5 3 6 4 7 9

# 2 3 4 5 6 7 
#result: 2 5 3 6 4 7

