from vecutil import list2vec
from solver import solve
from independence import rank
from matutil import listlist2mat, coldict2mat, rowdict2mat, mat2rowdict,mat2coldict, identity 
from mat import Mat
from GF2 import one
from vec import Vec,add,neg,scalar_mul
from triangular import triangular_solve
import random
from factoring_support import intsqrt, dumb_factor
from bitutil import *
import itertools
import numpy as np
random.seed(2)

def root_method(N):
	a = intsqrt(N)+1
	
	for i in range(a,N+1):
		
		b = intsqrt(i**2 - N)
		
		if b%1==0:
			print(b)
			return i-b

def gcd(x,y): return x if y==0 else gcd(y,x%y)

def int2GF2(x): return one if x%2==1 else 0

def make_Vec(primeset, factors):
	d = primeset
	print(factors)
	f = dict(map(lambda x: (x[0],int2GF2(x[1])), factors))
	print(f)
	return Vec(d, f)

# N = [55,77,118,146771]
# print(root_method(N[1]))
# r = 12398280234912304
# s = 2752187456 #5504374912
# t = 9541094510
# a = r*s
# b = s*t
# print(gcd(a,b))
# print(dumb_factor(75,{2,3,5,7}))
factors = {2,3,5,7,11}
#print(int2GF2(3))
N = 2419
print(dumb_factor(N,factors))
print(make_Vec(factors, dumb_factor(N,factors)))