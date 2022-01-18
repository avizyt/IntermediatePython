import numpy as np
import scipy.linalg as la


A = np.array([[2,3],[5,4]])
b = np.array([4,3])
rank = np.linalg.matrix_rank(A)
print("Rank: ",rank)

conditon_number = np.linalg.cond(A)
print("conditon number: ",conditon_number)

norm_A = np.linalg.norm(A)
print("norm of A: ",norm_A)

inv_A = np.linalg.inv(A)
pinv_A = np.linalg.pinv(A)
# print(inv_A)
# print(pinv_A)

print(pinv_A.dot(b))

P,L,U = la.lu(A)

# print(P.dot(L.dot(U)))

print(la.solve(A,b))
# print(solve)

