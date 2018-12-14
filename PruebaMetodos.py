'''
Created on 14 dic. 2018

@author: aochi
'''
from time import time

class metodosOrdenamiento:
    def mostrarVector(self, datos):
        cont=1
        for i in range(0, len(datos)):
            if(int(cont)==15):
                print("  "+str(datos[i])+",    ")
                cont=1
            else:
                print("  "+str(datos[i])+",    ", end="")
                cont+=1
    
    def mostrarDatosDeEficiencia(self, contadorComparaciones, contadorIntercambios,
                                 contadorRecorridos, tiempoTotal):
        print("~~~~~~~~~~~~ DATOS DE EFICIENCIA DEL ALGORITMO ~~~~~~~~~~~~~~~~~~")
        print()
        print("Cantidad  de  recorridos  realizados:    "+str(contadorRecorridos))
        print("Cantidad de comparaciones realizadas:    "+str(contadorComparaciones))
        print("Cantidad  de intercambios realizados:    "+str(contadorIntercambios))
        print("Tiempo     total     de    ejecucion:    "+str(tiempoTotal)+" segundos")
        print("Tiempo     total     de    ejecucion:    "+str(tiempoTotal*1000)+" milisegundos")
        
    def ordenamientoPorSeleccion(self, datos):
        contadorComparaciones=0
        contadorIntercambios=0
        contadorRecorridos=0
        
        inicio=time()
        for i in range(0, len(datos)):
            menor=i
            for j in range(i+1, len(datos)):
                contadorComparaciones+=1
                if(datos[j]<datos[menor]):
                    menor=j
            aux=datos[i]
            datos[i]=datos[menor]
            datos[menor]=aux
            contadorIntercambios+=1
            contadorRecorridos+=1
            contadorIntercambios+=1
        tiempoTotal=time()-inicio
        self.mostrarVector(datos)
        print()
        print()
        self.mostrarDatosDeEficiencia(contadorComparaciones, contadorIntercambios, contadorRecorridos, tiempoTotal)
    
    def ordenamientoPorInsercion(self, datos):
        contadorComparaciones=0
        contadorIntercambios=0
        contadorRecorridos=0
        
        inicio=time()
        for i in range(1, len(datos)):
            valor=datos[i]
            j=i-1
            while(j>=0):
                contadorComparaciones+=1
                if(valor<datos[j]):
                    contadorIntercambios+=1
                    datos[j+1]=datos[j]
                    datos[j]=valor
                    j-=1
                else:
                    break
            contadorRecorridos+=1
        tiempoTotal=time()-inicio
        self.mostrarVector(datos)
        print()
        print()
        self.mostrarDatosDeEficiencia(contadorComparaciones, contadorIntercambios, contadorRecorridos, tiempoTotal)
        
        
datos=[2,8,1,65,21,14,36,12,9,60,35,46]

mo=metodosOrdenamiento()
print("Vector original")
mo.mostrarVector(datos)
print()
print("Vector ordenado")
print()
mo.ordenamientoPorInsercion(datos.copy())
print()
print("Vector original")

mo.mostrarVector(datos.copy())
print()
print("Vector ordenado")
mo.ordenamientoPorSeleccion(datos.copy())