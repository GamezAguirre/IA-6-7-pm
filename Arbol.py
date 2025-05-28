
# GAMEZ AGUIRRE JESUS ALEXANDER 
from Nodo import Nodo
class Arbol:
    def __init__(self):
        self.raiz = None

    #Insertar un valor en el árbol
    def insertar(self, valor):
        if self.raiz is None:
            self.raiz = Nodo(valor)
        else:
            self._insertar_recursivo(self.raiz, valor)
    #Insertar un valor en el árbol buscando su posición correcta
    def _insertar_recursivo(self, nodo, valor):
        if valor < nodo.valor:
            if nodo.izquierda is None:
                nodo.izquierda = Nodo(valor)
            else:
                self._insertar_recursivo(nodo.izquierda, valor)
        else:
            if nodo.derecha is None:
                nodo.derecha = Nodo(valor)
            else:
                self._insertar_recursivo(nodo.derecha, valor)
    #Buscar un valor en el árbol
    def buscar(self, valor):
        return self._buscar_recursivo(self.raiz, valor)
    #Buscar un valor en el árbol si no se encuentra o es vacio retorna None
    def _buscar_recursivo(self, nodo, valor):
        if nodo is None or nodo.valor == valor:
            return nodo
        if valor < nodo.valor:
            return self._buscar_recursivo(nodo.izquierda, valor)
        return self._buscar_recursivo(nodo.derecha, valor)

    # Determinar si un nodo está vacío
    def nodo_vacio(self, nodo):
        return nodo is None