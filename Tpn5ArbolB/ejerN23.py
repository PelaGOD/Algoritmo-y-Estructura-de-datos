class Nodo:
    def __init__(self, criatura, derrotado_por, capturada=None, descripcion=None):
        self.criatura = criatura
        self.derrotado_por = derrotado_por
        self.capturada = capturada
        self.descripcion = descripcion
        self.izquierda = None
        self.derecha = None

class ArbolBinario:
    def __init__(self):
        self.raiz = None

    def insertar(self, criatura, derrotado_por):
        if self.raiz is None:
            self.raiz = Nodo(criatura, derrotado_por)
        else:
            self._insertar(self.raiz, criatura, derrotado_por)

    def _insertar(self, nodo, criatura, derrotado_por):
        if criatura < nodo.criatura:
            if nodo.izquierda is None:
                nodo.izquierda = Nodo(criatura, derrotado_por)
            else:
                self._insertar(nodo.izquierda, criatura, derrotado_por)
        else:
            if nodo.derecha is None:
                nodo.derecha = Nodo(criatura, derrotado_por)
            else:
                self._insertar(nodo.derecha, criatura, derrotado_por)

    def inorden(self):
        self._inorden(self.raiz)

    def _inorden(self, nodo):
        if nodo:
            self._inorden(nodo.izquierda)
            print(f"Criatura: {nodo.criatura}, Derrotado por: {nodo.derrotado_por}")
            self._inorden(nodo.derecha)

    def buscar(self, criatura):
        return self._buscar(self.raiz, criatura)

    def _buscar(self, nodo, criatura):
        if nodo is None or nodo.criatura == criatura:
            return nodo
        if criatura < nodo.criatura:
            return self._buscar(nodo.izquierda, criatura)
        return self._buscar(nodo.derecha, criatura)

    def eliminar(self, criatura):
        self.raiz = self._eliminar(self.raiz, criatura)

    def _eliminar(self, nodo, criatura):
        if nodo is None:
            return nodo
        if criatura < nodo.criatura:
            nodo.izquierda = self._eliminar(nodo.izquierda, criatura)
        elif criatura > nodo.criatura:
            nodo.derecha = self._eliminar(nodo.derecha, criatura)
        else:
            if nodo.izquierda is None:
                return nodo.derecha
            elif nodo.derecha is None:
                return nodo.izquierda
            temp = self._minValueNode(nodo.derecha)
            nodo.criatura = temp.criatura
            nodo.derecha = self._eliminar(nodo.derecha, temp.criatura)
        return nodo

    def _minValueNode(self, nodo):
        current = nodo
        while current.izquierda is not None:
            current = current.izquierda
        return current

    def modificar(self, criatura, nueva_criatura=None, derrotado_por=None, capturada=None, descripcion=None):
        nodo = self.buscar(criatura)
        if nodo:
            if nueva_criatura:
                nodo.criatura = nueva_criatura
            if derrotado_por:
                nodo.derrotado_por = derrotado_por
            if capturada:
                nodo.capturada = capturada
            if descripcion:
                nodo.descripcion = descripcion

    def listar_por_nivel(self):
        if not self.raiz:
            return
        queue = [self.raiz]
        while queue:
            current = queue.pop(0)
            print(f"Criatura: {current.criatura}, Derrotado por: {current.derrotado_por}")
            if current.izquierda:
                queue.append(current.izquierda)
            if current.derecha:
                queue.append(current.derecha)

# Datos de la tabla
criaturas = [
    ("Tifón", "Zeus"), ("Ceto", "-"), ("Pequeño Pino", "Heracles"), ("Jabalí de Calidón", "Atalanta"),
    ("Equidna", "Argos Panoptes"), ("Toro de Creta", "Teseo"), ("Escila", "Heracles"), ("Gerión", "Heracles"),
    ("Caribdis", "-"), ("Cloto", "-"), ("Esteno", "Atropos"), ("Minotauro de Creta", "Teseo"),
    ("Euríale", "Laquesis"), ("Medusa", "Perseo"), ("Ladón", "Heracles"), ("Agrio y Celæno", "Argos Panoptes"),
    ("Quimera", "Bellerofonte"), ("Harpías", "-"), ("Hidra de Lerna", "Heracles"), ("Sirenas", "-"),
    ("Dragón de la Cólquida", "Jason"), ("Talos", "Medea"), ("León de Nemea", "Heracles"), ("Pitón", "Apolo"),
    ("Esﬁnge", "Edipo"), ("Cierva Cerinea", "Heracles"), ("Cerbero", "Heracles")
]

# Crear el árbol e insertar los datos
arbol = ArbolBinario()
for criatura, derrotado_por in criaturas:
    arbol.insertar(criatura, derrotado_por)

# Ejemplo de uso
print("Listado inorden de las criaturas y quienes las derrotaron:")
arbol.inorden()

print("\nMostrar toda la información de la criatura Talos:")
talos = arbol.buscar("Talos")
if talos:
    print(f"Criatura: {talos.criatura}, Derrotado por: {talos.derrotado_por}, Capturada: {talos.capturada}, Descripción: {talos.descripcion}")

# Modificar nodos
arbol.modificar("Cerbero", capturada="Heracles")
arbol.modificar("Toro de Creta", capturada="Heracles")
arbol.modificar("Cierva Cerinea", capturada="Heracles")
arbol.modificar("Jabalí de Erimanto", capturada="Heracles")

print("\nListado por nivel del árbol:")
arbol.listar_por_nivel()
