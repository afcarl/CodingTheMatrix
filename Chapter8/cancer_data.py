# Copyright 2013 Philip N. Klein
from vec import Vec,neg, add,scalar_mul
from matutil import rowdict2mat
import random
import mat
from mat import matrix_vector_mul,vector_matrix_mul, transpose
import pandas as pd

def transpose(M):
    """
    Returns the matrix that is the transpose of M.

    M = Mat(({0,1}, {0,1}), {(0,1):3, (1,0):2, (1,1):4})
    M.transpose() == Mat(({0,1}, {0,1}), {(0,1):2, (1,0):3, (1,1):4})
    True
    M = Mat(({'x','y','z'}, {2,4}), {('x',4):3, ('x',2):2, ('y',4):4, ('z',4):5})
    Mt = Mat(({2,4}, {'x','y','z'}), {(4,'x'):3, (2,'x'):2, (4,'y'):4, (4,'z'):5})
    M.transpose() == Mt
    True
    """
    
    k = M.f.keys()
    v = M.f.values()
    
    keys = map(lambda x: (x[1],x[0]),k)
    M.f = dict(zip(keys,v))
    
    M.D = (M.D[1],M.D[0])
    
    return M

def read_training_data(fname, D=None):
    """Given a file in appropriate format, and given a set D of features,
    returns the pair (A, b) consisting of
    a P-by-D matrix A and a P-vector b,
    where P is a set of patient identification integers (IDs).

    For each patient ID p,
      - row p of A is the D-vector describing patient p's tissue sample,
      - entry p of b is +1 if patient p's tissue is malignant, and -1 if it is benign.

    The set D of features must be a subset of the features in the data (see text).
    """
    file = open(fname)
    params = ["radius", "texture", "perimeter","area","smoothness","compactness","concavity","concave points","symmetry","fractal dimension"];
    stats = ["(mean)", "(stderr)", "(worst)"]
    feature_labels = set([y+x for x in stats for y in params])
    feature_map = {params[i]+stats[j]:j*len(params)+i for i in range(len(params)) for j in range(len(stats))}
    if D is None: D = feature_labels
    feature_vectors = {}
    patient_diagnoses = {}
    for line in file:
        row = line.split(",")
        patient_ID = int(row[0])
        patient_diagnoses[patient_ID] = -1 if row[1]=='B' else +1
        feature_vectors[patient_ID] = Vec(D, {f:float(row[feature_map[f]+2]) for f in D})
    return rowdict2mat(feature_vectors), Vec(set(patient_diagnoses.keys()), patient_diagnoses)


def signum(u):
	u.f = dict(map(lambda x:(x[0],-1) if x[1]<0 else (x[0],1), u.f.items()))
	
	return u

def fraction_wrong(A,b,w):
	

	w_result = signum(matrix_vector_mul(A,w))
	print w_result
	frac = map(lambda x: 1 if (x[1]== filter(lambda y:y[0]==x[0] ,b.f.items())[0][1]) else 0 , w_result.f.items())
	print sum(frac)*100.0/len(frac)

def find_grad(A,b,w):
	
	# print A.D
	#print '\n'
	w_result = (matrix_vector_mul(A,w))
	
	sc = add(w_result, neg(b))
	
	# print '\n'
	# print sc.D
	# # print A.D
	# # # print A
	# print '\n'
	# T = transpose(A)
	# print T.D
	# print T
	G = matrix_vector_mul(A,sc)

	#print G
	return (G)
	# #print matrix_matrix_mul(transpose(A), sc)
def gradient_descent_step(A,b,w,sigma):
	i = 100
	while i>0:
		#scalar_mul(find_grad(data[0],b,w),0.5)
		i = i-1
		w = add(w,neg(scalar_mul(find_grad(data[0],b,w),sigma)))
	print w

if __name__ == '__main__':
	data = read_training_data("/Users/khokher/Documents/CodingTheMatrix/Chapter8/train.data")
	#print data
	#print signum(Vec({'a','e','i','o','u'}, {'o':4,'u':7}))
	#print data[1]
	
	b = data[1]

	random_list = [random.choice([1,-1]) for i in range(30)]
	w = Vec(data[0].D[1], dict(zip(data[0].D[1], random_list)))
	#fraction_wrong(data[0],b,w)
	#find_grad(data[0],b,w)
	gradient_descent_step(data[0],b,w,0.5)
	

