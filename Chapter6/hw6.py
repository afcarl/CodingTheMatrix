from vecutil import list2vec
from solver import solve
from independence import rank
from matutil import listlist2mat, coldict2mat, rowdict2mat, mat2rowdict,mat2coldict, identity 
from mat import Mat
from GF2 import one
from vec import Vec,add,neg
from triangular import triangular_solve


def morph(S,B):
	#B is independent list
	#S is list of vectors
	# Span(S) = Span(B)
	returned_list = []
	rank_B = rank(B)
	for b in B:
		# if set(B) == set(S_rem):
		# 	break
		B.pop(0)
		cond = B
		for s in S:

			if rank(cond+[s])==rank_B:
				B.append(s)
				S.remove(s)
				returned_list.append([b,s])
				

	return returned_list
	
def get_basis(U):
	
	rank_ = rank(U)
	#already contains independent vectors
	if my_is_independent(U):
		return U 
	# if not there are superfluous vectors
	U_basis = []
	r = 0
	for u in U:
		if rank(U_basis+[u]) > r:
			U_basis.append(u)
			r = rank[u]
		if r == rank_:
			return U_basis

	


def my_is_independent(L):
	cols = len(L)
	rows = len(L[0].D)
	rank_ = min(cols,rows)
	
	if rank(L) == rank_:
		return True
	else:
		False

def direct_sum_decompose(U,V,w):
	basis_vectors_W = get_basis(U)
	UV = coldict2mat(basis_vectors_W)
	W = solve(UV, w)
	print(W)
	basis_vectors_W = get_basis(V)
	UV = coldict2mat(basis_vectors_W)
	W = solve(UV, w)
	print(W)
	basis_vectors_W = get_basis(U+V)
	UV = coldict2mat(basis_vectors_W)
	W = solve(UV, w)
	print(W)

def is_invertible(M):
	L = mat2coldict(M)
	L = list(L.values())
	cols = len(L)
	rows = len(L[0].D)
	if cols == rows and my_is_independent(L):
		return True
	else:
		return False
	

def matrix_inverse(M):
	L = []
	if is_invertible(M):
		print('yayyy')
		for e in M.D[0]:
			w = [0]*len(M.D[0])
			w[e] = one
			w = list2vec(w)
			L.append(solve(M,w))
	#print(L)
	return coldict2mat(L)

def find_triangular_matrix_inverse(A):
	L=[]
	label_list = []
	I = identity(A.D[0],1)
	R = mat2rowdict(A)
	w = mat2rowdict(I)
	label_list.extend(range(len(R)))
	for k,v in w.items():
		print(k,v,)
		s = triangular_solve(R, label_list, v)
		L.append(s)
	return coldict2mat(L)
           


####### triangular solve ######
A = listlist2mat([[1, .5, .2, 4],[0, 1, .3, .9],[0,0,1,.1],[0,0,0,1]])
print(find_triangular_matrix_inverse(A))
####### triangular solve ######

####### matrix inverse #######
# M = Mat(({0, 1, 2}, {0, 1, 2}), {(0, 1): one, (1, 2): 0, (0,0): 0, (2, 0): 0, (1, 0): one, (2, 2): one, (0, 2): 0, (2, 1): 0,(1, 1): 0})
# print(matrix_inverse(M))
####### matrix inverse #######

##### is_invertible #####
# M = Mat(({0, 1, 2, 3}, {0, 1, 2, 3}), {(0, 1): 0, (1, 2): 1,
#     (3, 2): 0, (0, 0): 1, (3, 3): 4, (3, 0): 0, (3, 1): 0, (1, 1): 2,
#     (2, 1): 0, (0, 2): 1, (2, 0): 0, (1, 3): 0, (2, 3): 1, (2, 2): 3,
#     (1, 0): 0, (0, 3): 0})
# print(is_invertible(M))
##### is_invertible #####



####### direct sum ######
# U_basis = [Vec({0, 1, 2, 3, 4, 5},{0: 2, 1: 1, 2: 0, 3: 0, 4: 6, 5: 0}),Vec({0, 1, 2, 3, 4, 5},{0: 11, 1: 5, 2: 0, 3: 0, 4: 1, 5: 0}),Vec({0, 1, 2, 3, 4, 5},{0: 3, 1: 1.5, 2: 0, 3: 0, 4: 7.5, 5: 0})]
# V_basis = [Vec({0, 1, 2, 3, 4, 5},{0: 0, 1: 0, 2: 7, 3: 0, 4: 0, 5: 1}),Vec({0, 1, 2, 3, 4, 5},{0: 0, 1: 0, 2: 15, 3: 0, 4: 0, 5: 2})]
# w = Vec({0, 1, 2, 3, 4, 5},{0: 2, 1: 5, 2: 0, 3: 0, 4: 1, 5: 0})
# direct_sum_decompose(U_basis, V_basis,w)
####### direct sum ######

###### independence ######
#print(my_is_independent([list2vec(v) for v in [[2,4,0],[8,16,4]]]))
###### independence ######


####### Uncomment Below for morph ##########
# S = [list2vec(v) for v in [[2,4,0],[1,0,3],[0,4,4],[1,1,1]]]
# B = [list2vec(v) for v in [[1,0,0],[0,1,0],[0,0,1]]]

# for s,b in (morph(S,B)):
# 	print('injecting')
# 	print(s)
# 	print('ejecting')
# 	print(b)
###### Uncomment above for morph ##########
