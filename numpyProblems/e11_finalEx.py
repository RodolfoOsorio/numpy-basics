
import numpy

#Matriz de enteros 0-255
x = (255*numpy.random.rand(8,8)).astype(numpy.uint8)
print("Matriz de enteros 8 bits:\n",x)

#Restar 128

y=x.astype(numpy.int16)-128
print("Matriz - 128: \n",y)

#Cuantizacion
#Es DIVIDIR en el problema(corregir)

Q = numpy.array([ [16,11,10,16,24,40,51,61] ], dtype=numpy.uint8)
Q = numpy.append(Q, [ [12,12,14,19,26,58,60,55] ], 0)
Q = numpy.append(Q, [ [14,13,16,24,40,57,69,56] ], 0)
Q = numpy.append(Q, [ [14,17,22,29,51,87,80,62] ], 0)
Q = numpy.append(Q, [ [18,22,37,56,68,109,103,77] ], 0)
Q = numpy.append(Q, [ [24,35,55,64,81,104,113,92] ], 0)
Q = numpy.append(Q, [ [49,64,78,87,103,121,120,101] ], 0)
Q = numpy.append(Q, [ [72,92,95,98,112,100,103,99] ], 0)

print("Producto punto a punto con la sig matriz:\n",Q)

R = y*Q

print("\nResultado:\n",R)

