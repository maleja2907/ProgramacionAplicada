class persona (object):
    def __init__(self):
        self.nombre() # Nombre de la persona
        self.Hermanos() # hermanos de la persona (n datos)
        self.Padres() # padres de la persona (2 datos o menos)

    def add_siblings (self,sib):
        # TODO: verificar y asegurar que los hermanos tengan los mismos padres (0.5)
        self.Hermanos.append(sib)

    def add_parents (self,parent):
        if self.Padres < 2:
            self.Padres.append(parent)
        else:
            print('No se puede agregar')

    def search (self,nombre):
        '''
        se busca a cualquier persona en el arbol, se asume que el usuario puede colocar cualquier combinación de
        mayusculas y minusculas
        :param nombre: nombre de la persona a buscar
        :return: retorna el objeto encontrado así como la altura a la que se encuentra el elemento
        '''
        #TODO: Implementar un método de busqueda para encontrar a cualquier persona en el arbol (0.5)

    def tree2dict (self):
        '''
        convierte el arbol actual en un diccionario usando los nombres como llaves y los padres y hermanos como llaves
        :return: retorna un diccionario
        '''
        # TODO: Implementar una función que permita convertir el arbol actual en un diccionario (1.0)

    def encript(self,nombre):
        '''
        crea un archivo encriptado, con la información correspondiente al arbol
        :param nombre: nombre del archivo que se desea crear
        :return: null
        '''
        # TODO: Implementar una función que permita converti el arbol en un archivo encriptado (1.0)

    def decrip(self,nombre):
        '''
        lee un archivo de texto, lo decifra y convierte el resultado en el arbol correspondiente
        :param nombre: Nombre del archivo que se desea leer
        :return: arbol creado
        '''
        #TODO: Im plementar una función que permita convertir un archivo encriptado en un arbol (1.0)

##
'''
la siguiente sección se debe realizar en un archivo distinto llamado TALLER02-2_nombre_apellido.py
'''
#TODO: iniciar y crear el arbol con una profundidad de almenos 4 con su familia (0.2)
#TODO: validar la función de busqueda (0.2)
#TODO: validad la encriptación de los archivos (0.2)
#TODO: validar la decriptación de archivos (0.2)
#TODO: validar la converción a diccionario (0.2)



class persona():
    def init(self, Hermanos, Padres, hijos, conyugues):
        self.Hermanos = []  # hermanos de la persona (n datos)
        self.Padres = []  # padres de la persona (2 datos o menos)
        self.hijos = []  # hijos
        self.conyugues = ""  #

    def add_siblings(self, Hermano):
        per = persona(Hermano, self.Padres)
        # TODO: verificar y asegurar que los hermanos tengan los mismos padres (0.5)
        self.Hermanos.append(per)

    def add_parents(self, Parent):
        if len(self.Padres) < 2:
            self.Padres.append(persona(Parent))
        else:
            print('No se puede agregar')

    def add_childrens(self, Hijo):
        per = persona(Hijo)
        self.hijo.append(per)

    def add_conyugues(self, conyugue):
        per = persona(conyugue)
        self.conyugue = conyugue

    def busqper(self, lista, nombre):
        i = 0
        while i < len(lista):
            if nombre == self.lista[i]:
                return nombre
            break
            else:
            i += 1


def search(self, nombre):
    i = 0
    while i < len(self.Hermanos):
        if nombre == self.Hermanos[i]:
            print(f"{nombre} es hermano")
            break
        else:
            i += 1
    j = 0
    while j < len(self.Padres):
        if nombre == self.Padres[i]:
            print(f"{nombre} es un padre")
            break
        else:
            j += 1


'''
    se busca a cualquier persona en el arbol, se asume que el usuario puede colocar cualquier combinación de
    mayusculas y minusculas
    :param nombre: nombre de la persona a buscar
    :return: retorna el objeto encontrado así como la altura a la que se encuentra el elemento
    '''


# TODO: Implementar un método de busqueda para encontrar a cualquier persona en el arbol (0.5)

def tree2dict(self):
    '''
    convierte el arbol actual en un diccionario usando los nombres como llaves y los padres y hermanos como llaves
    :return: retorna un diccionario
    '''
    # TODO: Implementar una función que permita convertir el arbol actual en un diccionario (1.0)


def encript(self, nombre):
    '''
    crea un archivo encriptado, con la información correspondiente al arbol
    :param nombre: nombre del archivo que se desea crear
    :return: null
    '''
    # TODO: Implementar una función que permita converti el arbol en un archivo encriptado (1.0)


def decrip(self, nombre):
    '''
    lee un archivo de texto, lo decifra y convierte el resultado en el arbol correspondiente
    :param nombre: Nombre del archivo que se desea leer
    :return: arbol creado
    '''
    # TODO: Im plementar una función que permita convertir un archivo encriptado en un arbol (1.0


gustav = persona()
gustav.add_siblings("juan")
gustav.add_siblings("pablo")
gustav.add_siblings("pedro")
gustav.add_siblings("jose")
gustav.add_parents("jaime")
gustav.add_parents("luisa")
juan = persona()
gustav.search("juan")
print(gustav.Hermanos, gustav.Padres)
# gustav.search("luisa")
