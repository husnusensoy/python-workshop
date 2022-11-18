import time

import numpy as np
from tqdm import tqdm

#vector = [i for i in range(1_000_000)]
#v = np.array(vector)

v = vi = np.arange(1_000_000)
vf = vi.astype(np.float32)

start = time.time()

for _ in tqdm(range(100)):
    vector2 = v * v

end = time.time()

print(f"Elapsed time for 100 doubling is {end-start}")

np.matmul(v,v)
print(type(v))



print(vi.dtype)
print(vf.dtype)

vv =np.concatenate((vf,vi))

print(len(vv))
print(vv.dtype)