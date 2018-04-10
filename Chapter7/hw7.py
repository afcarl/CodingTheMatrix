from vecutil import list2vec
from solver import solve
from independence import rank
from matutil import listlist2mat, coldict2mat, rowdict2mat, mat2rowdict,mat2coldict, identity 
from mat import Mat
from GF2 import one
from vec import Vec,add,neg,scalar_mul
from triangular import triangular_solve
import random
from bitutil import *
import itertools
import numpy as np
random.seed(2)
def randGF2():
	return random.randint(0,1)*one


def choose_secret_vector(s,t):
	
	while True:
		u = list2vec([randGF2(),randGF2(),randGF2(),randGF2(),randGF2(),randGF2()])
		if (a0*u == s) and (b0*u == t):
			break
	return u


def other_vectors():

	while True:
		l_ = [a0,b0]
		for i in range(8):
			l_.append(list2vec([randGF2(),randGF2(),randGF2(),randGF2(),randGF2(),randGF2()]))
		ranks = []
		for comb in list(itertools.combinations([0,2,4,6,8], 3)):
			
			l = [(l_[i],l_[i+1]) for i in comb]
			the_three = [item for sublist in l for item in sublist]
			r = rank(the_three)
			if r<6:
				continue
			else:
				ranks.append(r)
		
		if set(ranks)== {6}:
			print("yess")
			return l_
		


	return l_

a0 = list2vec([one,one,0,one,0,one])
b0 = list2vec([one,one,0,0,0,one])
# #print(one*8)
# #print(choose_secret_vector(0,0))
ten_vecs = other_vectors()
# print(len(ten_vecs))
string_ = str2bits('Priya')
matrix_ = mat2coldict(bits2mat(string_,2))
U = []
for i in range(len(matrix_)):

	s,t = list(list(matrix_.values())[i].f.values())
	print(s,t)
	U.append(choose_secret_vector(s,t))
	

all_shares = []
for u in U:
	shares = []
	for v in ten_vecs:
		shares.append(np.dot(u,v))
	all_shares.append(shares)
print('\n all_shares \n')
print(all_shares)
#print(map(lambda x: list(x),mat2coldict(bits2mat(str2bits('Priya'),2))[0].f.values()))



