import numpy as np
def lcs3(dimensiones, palabra1, palabra2, palabra3):
    
    """Algoritmo que encuentra la subpalabra en común más corta entre tres cadenas de texto."""

    ## Registramos los valores del usuario:
    #dimensiones = str(input("Dimensiones de las palabras: "))
    #palabra1 = str(input("Palabra1: "))
    #palabra2 = str(input("Palabra2: "))
    #palabra3 = str(input("Palabra3: "))
    
    ## Convertimos la linea 1 a una lista de enteros:
        
    dimensiones = [int (x) for x in dimensiones.split()]
    
    ## En este caso, nos encontramos con un problema de programación 
    ## Dinámica que se resuelve creando una matriz M de tamaño n, m, k
    ## que satisfaga:
        
    ## 1. Sí algún elemento está vacío, entonces no hay subpalabra común,
    ## Así, M[i][j][k]=0.
    
    ## 2 Sí el elemento de todas las cadenas concuerda, entonces:
    ##  M[i][j][k]= 1 + M[i-1][j-1][k-1]
    
    ## 3 Sí los elementos de al menos uno de los 3 pares de cadenas no concuerdan, entonces 
    ## M[i][j][k]=max(M[i-1][j][k],M[i][j-1][k],M[i][j][k-1])
    #print(dimensiones)
    m = np.zeros(dimensiones)
    #print(m[1][1][1])
    palabra = ""
    
    for i in range (dimensiones[0]):
        
        for j in range (dimensiones[1]):
            
            for k in range (dimensiones[2]):
                
                if i == 0 or j == 0 or k==0 :
                    m[i][j][k] = 1
                elif palabra1[i]!=palabra2[j]!=palabra3[k]:
                    m[i][j][k] = 0 
                elif palabra1[i]!= palabra2[j] or palabra2[j]!=palabra3[k] or palabra1[i]!=palabra3[k]:
                    m[i][j][k] = max(m[i][j][k],m[i][j][k],m[i][j][k])
                    
                elif palabra1[i]== palabra2[j]==palabra3[k]:
                    m[i][j][k] = 1 +  m[i-1][j-1][k-1]
                if m[i][j][k] > len(palabra):
                    palabra = palabra1[i+1-int(m[i][j][k]):i+1]
                
    return palabra

print(lcs3("10 10 9", "aabbabbaba", "abbabababa", "bbabbabab" ))
