import numpy as np 
np_array = np.array([(1, 2, 3, 4, 8),(1, 3, 4, 5, 6)])
flo_at_array = np.array([(4, 6, 7, 9, 7),(3, 4, 6, 7, 6)], dtype = float)
print(np_array)
print()
print(type(np_array))
print("The shape of np_array")
print(np_array.shape)
print()
print("Floating array")
print(flo_at_array)
print()

# Numpy array of zeros 
x = np.zeros((4,5))
print("Array of Zeros")
print(x)
print()

# Numpy array of ones 
y = np.ones((3,4))
print("Array of Ones")
print(y)
print()

# Numpy array of full
z = np.full((3,4),5)
print("Full array")
print(z)
print()

# Identity Matrix 
I = np.eye(4)
print("Identity Matrix(Array)")
print(I)
print()

# Numpy array with Random values 
R = np.random.random((3,4))
print("Numpy array of Random Values")
print(R)
print()

# Random Integer values array within a specific range 
R_I = np.random.randint(10, 100, (3,5))
print("Random Integer values within a specific range")
print(R_I)
print()

# Array of evenly spaced values
E = np.linspace(10, 30, 5)
print("Array of evenly spaced values")
print(E)
print()

# Array of evenly spaced values ---> specifying the steps 
e = np.arange(10, 30, 5)
print("Array of evenly spaced values with specifying the steps")
print(e)
print()

# Convert a list to a Numpy array
list_2 = [2, 4, 5, 6, 7]
new_nparray = np.asarray(list_2)
print("Converting the list")
print(type(new_nparray))
print(new_nparray)
print()

array = np.random.randint(0, 10, (3,4))
print(array)
print("Shape of the array")
print(array.shape)

trans = np.transpose(array)
print("\nTranspose of the array")
print(trans)
print("Shape of the array\n", trans.shape)

# Number of Dimension 
print("Number of Dimension\n", trans.ndim)      
print("Number of Element in an array\n", trans.size)
print("Checking the Datatype of the values in the array\n", trans.dtype)
