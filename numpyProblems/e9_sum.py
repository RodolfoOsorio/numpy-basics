
import numpy

a = numpy.array([ [1,2,1],[2,4,2],[1,2,1] ])
b = numpy.sum(a)
print("Suma todos los elementos de la matriz",b)

c = numpy.sum(a,0)
print("Suma a lo largo de las columnas: ",c)

d = numpy.sum(a,1)
print("Suma a lo largo de los renglones: ",d)


