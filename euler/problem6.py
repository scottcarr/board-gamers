import numpy as np

input = np.asarray(range(1,101))
sq_sm = sum(input)**2
sm_sq = sum(input**2)
print sq_sm - sm_sq
