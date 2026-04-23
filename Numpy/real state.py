import numpy as np

brokered_by, price , bed , bath = np.genfromtxt("Numpy\\RealEstate-USA.csv", delimiter=",", usecols=(0, 2, 3, 4), unpack=True, dtype=None, skip_header=1 )
print("brokered_by")
print(brokered_by)
print("price")
print(price)
print("bed")
print(bed)
print("bath")
print(bath)
