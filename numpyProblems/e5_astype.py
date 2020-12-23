
import numpy

x = numpy.array([ [1,2,3], [4,5,6], [7,8,9] ])
print(x)
print(x.shape)

y = 10*numpy.random.rand(4,4)
print(y)

z = y.astype(numpy.int16)
print(z)

#tipos: int8, uint8, int16, uint16, int32, uint32, int64, uint64, float32, float64
