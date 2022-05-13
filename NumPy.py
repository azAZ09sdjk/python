import numpy as np

a = np.array([1, 2, 3], dtype='int64')

b = np.array([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]])
print("1 dimension array")
print(a)
print("2 dimension array")
print(b)

c = a.ndim
d = b.ndim

print("Get dimension Command")
print(c)
print(d)

#Get Shape
e = a.shape
f = b.shape

print("Get Shape Command")
print(e)
print(f)

g = a.dtype
h = b.dtype

print("Get type Command")
print(g)
print(h)

print("Getting Specific element")
