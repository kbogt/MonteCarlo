import pylab
import random
import math
N=2500000

##Descomentar para escribir las iteraciones en un archivo
##f=open('registro.txt', 'w')

##definiendo la integral en terminos de x[0], x[1], x[2]... x[n-1] done n es el numero de variables
## por ejemplo para la ecuacion de un circulo unitario
##def fx(x):
##    if x[0]**2+x[1]**2 <=1:
##        return 1
##    else:
##        return 0
    
##otro ejemplo la integral de (x*y) end donde x=x[0] y y=x[1]
##def fx(x):
##    return math.sin(x[0])*math.exp(x[1])

def fx(x):
    return x[0]**2+x[1]**2
##Limites del espacio muestral en orden de x[0], x[1], etc...
##Nota debe haber un limite de integracion por cada variable


##SS=[(0,math.pi),(0,math.log(2))]
SS=[(0,1),(0,1)]
## Definiendo el volumen muestral

V=1
for dif in SS:
    V*=(dif[1]-dif[0])

##Realizando la sumatoria con la funcion valuada con terminos aleatorios.
suma=0
for i in range(N):
    x=[]
    for j in range(len(SS)):
        x.append(random.randrange(SS[j][0],SS[j][1], _int=float))
    suma+=fx(x)
##Descomentar para escribir las iteraciones en un archivo
##    if i!=0:
##        f.write('Iteracion:'+'\t'+str(i)+'\t'+'sumatoria: '+'\t'+str(suma)+'\t'+'Respuesta Relativa:'+'\t'+str(float(V)/i*suma)+'\n')
        
##Imprimiendo el resultado.
Qn=float(V)/N*suma
##Descomentar para escribir las iteraciones en un archivo
##f.write('Resultado='+'\t'+str(Qn)+'\t'+'con'+'\t'+str(N)+'\t'+'iteraciones')
##f.close()
print Qn
                 


                 
    
