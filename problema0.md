Pilhas:
Pilhas são estruturas de dados em que os dados são empilhados um acima do outro de forma sequencial .. Sempre que um novo elemento é inserido damos a ele o nome de “topo”, pois é o primeiro elemento ao qual teremos acesso.Essa estrutura segue um padrão conhecido como LIFO (Last In First Out), onde o último a entrar será o primeiro a sair. 
Podem ser implementadas utilizando arrays; arrays dinâmicos e listas encadeadas.
As principais operações em uma pilha são:
Empilhar (push): Adicionar um elemento ao topo da pilha.
Desempilhar (pop): Remover o elemento do topo da pilha.
Verificar o topo (peek): Obter o elemento no topo da pilha sem removê-lo.
Verificar se está vazia (isEmpty): Verificar se a pilha não contém elementos.



FILA:
Fila são estruturas de dados, onde o primeiro elemento a ser inserido, será também o primeiro a ser retirado. Desta forma, serão adicionados elementos no fim e removidos pelo início.
A estrutura de dados fila segue um padrão conhecido como FIFO (first-in first-out), onde o primeiro a entrar é o primeiro a sair.
Pode ser implementada utilizando arrays, arrays circulares e listas encadeadas
Operações Básicas: As principais operações em uma fila são:
Enfileirar (enqueue): Adicionar um elemento ao final da fila.
Desenfileirar (dequeue): Remover o elemento do início da fila.
Verificar o início (front): Obter o elemento no início da fila sem removê-lo.
Verificar se está vazia (isEmpty): Verificar se a fila não contém elementos.



DEQUE:
É uma variação da fila que aceita inserção e remoção de elementos tanto do início quanto do final da fila.
podem ser implementados utilizando arrays dinâmicos ou listas ligadas duplamente encadeadas.

As principais operações em um deque são:
Inserir no início (push_front): Adicionar um elemento no início do deque.
Inserir no final (push_back): Adicionar um elemento no final do deque.
Remover do início (pop_front): Remover o elemento do início do deque.
Remover do final (pop_back): Remover o elemento do final do deque.
Verificar o início (front): Obter o elemento no início do deque sem removê-lo.
Verificar o final (back): Obter o elemento no final do deque sem removê-lo.
Verificar se está vazio (isEmpty): Verificar se o deque não contém elementos.




Árvore binária:
Uma árvore é um conjunto de nós, que possuem uma relação pai-filho. São hierárquicas e no caso das árvores binárias, cada nó tem no máximo dois filhos, geralmente referidos como filho esquerdo e filho direito. 

Definições:
Nó raiz
Nó pai
Nós filhos
Nó ancestral
Nó descendente
Nós folhas (nós externos)


Árvore Estritamente Binária (Própria)
Todo nó (não folha) tem subárvores direita e esquerda

Árvore Binária Cheia (Full Binary Tree)
Árvore estritamente binária de profundidade d
Todas as folhas estão no nível d

Árvore Binária Completa
Profundidade d
Cada folha esteja no nível d ou d-1
As folhas estão o mais à esquerda possível

Árvore Binária Balanceada
Para cada nó,  as alturas de suas sub-árvores difere no máximo de 1

Árvore Binária Perfeitamente Balanceada
Para cada nó,  o número de nós de suas sub-árvores difere no máximo de 1
Toda AB perfeitamente balanceada é balanceada, mas o contrário não é verdade
