import os
import sys
import itertools
import operator

def inverted_index(l):
	
	it = itertools.groupby(sorted(l),operator.itemgetter(0))
	for key, grp in it:
		yield (key, list(set(map(operator.itemgetter(1), grp))))
	

def makeInverseIndex(file_name):

	with open(file_name) as file:
		stories_list = [x.split(' ') for x in file.readlines()]
		indexed = [(i,x) for (i,x) in enumerate(stories_list)]
		word_index = map(lambda x: zip([x[0]]*len(x[1]), x[1]), indexed)
		decompose_list = [item for sublist in word_index for item in sublist]
		decompose_list = map(lambda x: (x[1],x[0]), decompose_list)
		inverted__index = list(inverted_index(decompose_list))
		return inverted__index

def orSearch(inverted_index, words_list):
	words_list = set(words_list)
	fitlered = [v for (k,v) in inverted_index if k in words_list]
	fitlered = set([item for sublist in fitlered for item in sublist])
	print fitlered

def andSearch(inverted_index, words_list):
	words_list = set(words_list)
	fitlered = [v for (k,v) in inverted_index if k in words_list]
	print reduce(lambda x,y: set(x) & set(y), fitlered)


if __name__ == '__main__':
	inverted_index = makeInverseIndex('stories_small.txt')
	#print inverted_index
	orSearch(inverted_index, ['A','!'])
	andSearch(inverted_index, ['A','!'])