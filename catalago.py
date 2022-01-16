from io import open
import pickle

class Pelicula:
    
    # Constructor de clase
    def __init__(self, titulo, duracion, lanzamiento):
        self.titulo = titulo
        self.duracion = duracion
        self.lanzamiento = lanzamiento
        print('Se ha creado la película:',self.titulo)
        
    def __str__(self):
        return '{} ({})'.format(self.titulo, self.lanzamiento)


class Catalogo:
    
    peliculas = []
    
    # Constructor de clase
    def __init__(self, peliculas=[]):
        self.peliculas = peliculas
        
    def agregar(self,p):
        self.peliculas.append(p)
        
    def mostrar(self):
        for p in self.peliculas:
            print(p)

c=Catalogo()
c.agregar(Pelicula("Spiderman",125,2002))
c.mostrar()