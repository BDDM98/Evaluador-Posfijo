# -*- coding: utf-8 -*-
class Pila:
    """ Representa una pila con operaciones de apilar, desapilar y
        verificar si está vacía. """
 
    def __init__(self):
        """ Crea una pila vacía. """
        # La pila vacía se representa con una lista vacía
        self.items=[]

    def apilar(self, x):
        """ Agrega el elemento x a la pila. """
        # Apilar es agregar al final de la lista.
        self.items.append(x)

    def desapilar(self):
        """ Devuelve el elemento tope y lo elimina de la pila.
            Si la pila está vacía levanta una excepción. """
        try:
            return self.items.pop()
        except IndexError:
            raise ValueError("La pila está vacía")

    def es_vacia(self):
        """ Devuelve True si la lista está vacía, False si no. """
        return self.items == []

def verificar(caracteres):
    datos=caracteres.split(" ")
    print(datos) 
    while len(datos)+1!=0:
        if len(datos)!=0:
            try:
                print(int(datos[0]),)
                datos.pop(0)
            except ValueError:
                    if datos[0]=="+" or datos[0]=="-" or datos[0]=="*" or datos[0]=="/" or datos[0]=="\n":
                        print("Error en los operadores")
                        return 0
                    else:
                        for i in len(datos):
                            if datos[i]=="+" or datos[i]=="-" or datos[i]=="*" or datos[i]=="/" or datos[i]=="\n":
                                print("ok")
                                datos.pop(i)
                            

                  
               # except ValueError:
                #    return 0
            #except ValueError:
             #   return 0
        else:
            print("ok")
            return 1
def leer(nombre):
    operaciones = Pila()
    archivo = open(nombre,"r")
    for linea in archivo.readlines():
        print linea
        verificar(linea)
        operaciones.apilar(linea)
    archivo.close()
    
leer("pruebita.txt")
