from nclsx import NCLS
import numpy as np

# starts = np.random.randint(0, int(1e8), int(1e3))
starts = np.array(range(100))
ends = starts + 100
ids = starts

ncls = NCLS(starts, ends, ids)

starts2 = np.array([0, 10, 20, 40000], dtype=np.long)
ends2 = np.array([5, 15, 25, 50000], dtype=np.long)
indexes2 = np.array([0, 1, 2, 3], dtype=np.long)

print("starts:", starts)

print("starts2:", starts2)
print("ends2:", ends2)

print("overlap:", ncls.has_overlaps(starts2, ends2, indexes2))

for i in range(0, 100):
    print(ncls.find_overlap_list(i, i + 10))
