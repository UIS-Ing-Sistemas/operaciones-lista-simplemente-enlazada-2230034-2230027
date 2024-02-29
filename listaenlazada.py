class Nodo:
    def __init__(self,valor):
        self.data = valor
        self.siguiente = None

class ListaSE:
    def __init__(self):
        self.cabeza = None

    def AgregarInicio(self,valor):
        nuevo_nodo = Nodo(valor)
        if self.cabeza == None:
            self.cabeza = nuevo_nodo
        else:
            nuevo_nodo.siguiente = self.cabeza
            self.cabeza = nuevo_nodo

    def AgregarFinal(self, valor):
        nuevo_nodo = Nodo(valor)
        if self.cabeza is None:
            # Si la lista está vacía, el nuevo nodo se convierte en la cabeza
            self.cabeza = nuevo_nodo
        else:
            # Si la lista no está vacía, recorremos la lista hasta llegar al último nodo
            actual_nodo = self.cabeza
            while actual_nodo.siguiente is not None:
                actual_nodo = actual_nodo.siguiente
            actual_nodo.siguiente = nuevo_nodo


    def EliminarPrimero(self):
              self.cabeza = self.cabeza.siguiente
              return

    def EliminarUltimo(self):
        #Se verifica que la lista no este vacia
        if self.cabeza != None:     
              if self.cabeza.siguiente == None:
                  actual_nodo = self.cabeza
                  while actual_nodo.siguiente != None:
                      actual_nodo = actual_nodo.siguiente
                      actual_nodo.siguiente = None
                      return
              return

    def BuscarElemento(self, valor):
        actual_nodo = self.cabeza

        while actual_nodo != None:
            if actual_nodo.data == valor:
                return True
            actual_nodo = actual_nodo.siguiente
        return False

    def ContarElementos(self):
        actual_nodo = self.cabeza
        contador = 0
        while actual_nodo != None:
            contador += 1
            actual_nodo = actual_nodo.siguiente
        return contador

    def IndicarVacia(self):
        if self.cabeza == None:
            return True
        else:
            return False

#Fin de la Clase Lista

ListaSimple = ListaSE()

ListaSimple.AgregarInicio(2)
ListaSimple.AgregarInicio(1)
ListaSimple.AgregarFinal(3)
print("---Lista Original---")
print(ListaSimple.cabeza.data)
print(ListaSimple.cabeza.siguiente.data)
print(ListaSimple.cabeza.siguiente.siguiente.data)

print("---Buscando un elemento en la lista(Numero:3)---")
print(ListaSimple.BuscarElemento(valor=3))

print(f"Cantidad de elementos en la lista: {ListaSimple.ContarElementos()}")



print("---Eliminando el primer elemento de la lista---")
ListaSimple.EliminarPrimero()
print(ListaSimple.cabeza.data)
print(ListaSimple.cabeza.siguiente.data)

print("---Eliminando el ultimo elemento de la lista---")
ListaSimple.EliminarUltimo()
print(ListaSimple.cabeza.data)

print("---Verificando si la lista está vacía---")
print(ListaSimple.IndicarVacia())
