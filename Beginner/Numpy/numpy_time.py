import numpy as np 
from time import perf_counter 

# This checks how long it takes to process a list without NumPy

python_list = [i for i in range(10000)]
start_time = perf_counter()
python_list = [i+5 for i in python_list]
end_time = perf_counter()
print(f"Python list : {end_time-start_time:.10f}")

# This is the list created by Numpy 

np_array = np.array([i for i in range(10000)])
start_time1 = perf_counter()
np_array+=1
end_time1 = perf_counter()
print(f"Numpy list  : {end_time1 - start_time1:.10f}")
