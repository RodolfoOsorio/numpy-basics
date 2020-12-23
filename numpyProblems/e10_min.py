
import numpy

a=numpy.array([ [1,2,3], [2,4,2], [1,2,1] ])

b= numpy.min(a)
print("El valor mínimo de la matriz es: ", b)

c = numpy.min(a,0)
print("Los mínimos de cada columna: ",c)

d = numpy.min(a,1)
print("Los mínimos de cada fila",d)
