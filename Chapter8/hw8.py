from vecutil import list2vec
from solver import solve
from independence import rank
from matutil import listlist2mat, coldict2mat, rowdict2mat, mat2rowdict,mat2coldict, identity 
from mat import Mat,matrix_vector_mul, transpose,vector_matrix_mul
from GF2 import one
from vec import Vec,add,neg
from triangular import triangular_solve
from orthogonalization import orthogonalize,project_orthogonal
import numpy as np
def basis(vlist):

	a = orthogonalize(vlist)
	
	#print(np.linalg.norm(list(a[0].f.values()),2))
	return [e for e in orthogonalize(vlist) if e*e > 1e-20]

def subset_basis(vlist):
	return [vlist[i] for i,e in enumerate(orthogonalize(vlist)) if e*e > 1e-20]


def orthogonal_vec2rep(Q,b):
	Q = listlist2mat(Q)
	print(Q)
	b = list2vec(b)
	print(Q*b)

def orthogonal_change_of_basis(A,B,a):
	print(A)
	print(a)
	return a*A
def orthonormal_projection_orthogonal(W,b):

	print(project_orthogonal(b,W))
	
##### Question 1 and 2 #####
# vlist_ = [[2,4,3,5,0],[4,-2,-5,4,0],[-8,14,21,-2,0],[-1,-4,-4,0,0],[-2,-18,-19,-6,0],[5,-3,1,-5,2]]
# vlist = map(lambda x: list2vec(x),vlist_)
#print(subset_basis(list(vlist)))
##### Question 1 and 2 #####

# Q = [[1/np.sqrt(2),1/np.sqrt(2),0],[1/np.sqrt(3),-1/np.sqrt(3),1/np.sqrt(3)],[-1/np.sqrt(6),1/np.sqrt(6),2/np.sqrt(6)]]
# b = [10,20,30]
# orthogonal_vec2rep(Q,b)
# A_ = [[1/np.sqrt(2),1/np.sqrt(2),0],[1/np.sqrt(3),-1/np.sqrt(3),1/np.sqrt(3)],[-1/np.sqrt(6),1/np.sqrt(6),2/np.sqrt(6)]]
# A = listlist2mat(A_)
# B_ = [[1/np.sqrt(2),1/np.sqrt(2),0],[1/np.sqrt(3),-1/np.sqrt(3),1/np.sqrt(3)],[-1/np.sqrt(6),1/np.sqrt(6),2/np.sqrt(6)]]
# B = listlist2mat(B_)
# a = list2vec([np.sqrt(2),1/np.sqrt(3),2/np.sqrt(6)])
# print(orthogonal_change_of_basis(A,B,a))

vlist_ = [[1/np.sqrt(2),1/np.sqrt(2),0],[1/np.sqrt(3),-1/np.sqrt(3),1/np.sqrt(3)]]#[[1/np.sqrt(2),1/np.sqrt(3)],[1/np.sqrt(2),-1/np.sqrt(3)],[0,1/np.sqrt(3)]]
W = list(map(lambda x: list2vec(x),vlist_))
b = list2vec([10,20,30])
print(W,b)
orthonormal_projection_orthogonal(W,b)



