from vecutil import list2vec
from solver import solve
from independence import rank
from matutil import listlist2mat, coldict2mat, rowdict2mat, mat2rowdict,mat2coldict, identity 
from mat import Mat
from GF2 import one
from vec import Vec,add,neg
from triangular import triangular_solve
from orthogonalization import orthogonalize
import numpy as np
def basis(vlist):

	a = orthogonalize(vlist)
	
	#print(np.linalg.norm(list(a[0].f.values()),2))
	return [e for e in orthogonalize(vlist) if e*e > 1e-20]

def subset_basis(vlist):
	return [vlist[i] for i,e in enumerate(orthogonalize(vlist)) if e*e > 1e-20]
vlist_ = [[2,4,3,5,0],[4,-2,-5,4,0],[-8,14,21,-2,0],[-1,-4,-4,0,0],[-2,-18,-19,-6,0],[5,-3,1,-5,2]]
vlist = map(lambda x: list2vec(x),vlist_)
#print(rank(list(vlist)))
#print(list(vlist))
print(len(basis(list(vlist))))
