#Se crea el arbol binario
class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key


#Esta funcion permite ingresar un nodo nuevo al arbol
def insert(root, key):
    if root is None:
        return Node(key)
    if root.val == key:
            return root
    if root.val < key:
            root.right = insert(root.right, key)
    else:
            root.left = insert(root.left, key)
    return root


# Funcion de recorrido "in order" ( Left -> Root -> Right)
def inorder(node):
    if node:
        inorder(node.left)
        print(node.val, end=" ")
        inorder(node.right)

# Funcion de recorrido "Pre Order" ( Root -> Left -> Right )
def preorder(node):
    if node is None:
        return
    print(node.val, end=' ')
    preorder(node.left)
    preorder(node.right)

# Funcion de recorrido "Post Order" (Left -> Right -> Root)

def postorder(node):
    if node is None:
        return
    postorder(node.left)
    postorder(node.right)
    print(node.val, end=' ')



r = Node(20) #Crea el arbol (y su primer nodo)
r = insert(r, 15)
r = insert(r, 4)
r = insert(r, 22)
r = insert(r, 34)
r = insert(r, 17)
r = insert(r, 2)
r = insert(r, 14)

# Imprimimos la busqueda "in order"
print("Recorrido in order:")
inorder(r)
print("\nRecorrido preorder:")
preorder(r)
print("\nRecorrido postorder:")
postorder(r)