import time

import numpy as np

my_list = list(range(100_000))  # python list 0~99999 --> Normal
my_array = np.array(range(100_000))  # numpy array (massiv) 0~99999 --> Vektorlashgan

start = time.time()
for _ in range(10): my_array * 2
end = time.time()

natija = end - start
print("Dastur sekund oladi: ", natija)
