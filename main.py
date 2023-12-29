import time

import numpy as np

my_list = list(range(100_000))  # python list 0~99999 --> Normal
my_array = np.array(range(100_000))  # numpy array (massiv) 0~99999 --> Vektorlashgan

start = time.time()
for _ in range(10):
    my_array * 2
end = time.time()

# 0.013599872589111328
# 0.0010001659393310547

natija = end - start
print("Dastur sekund oladi: ", natija)

data = {
    "7/4/2014": 2000,
    "4/4/2012": 2000,
    "3/4/2017": 2000,
    "2/4/2011": 2000,
    "8/4/2019": 1000,
    "7/19/2021": 2000,
    "5/15/2018": 3000,
    "11/14/2009": 2000,
    "2/15/2025": 2400,
    "1/4/2013": 2000,
    "9/25/2014": 4000,
    "10/4/2019": 2000,
    "7/4/2020": 2000,
    "12/5/2014": 2500,
}
