#! /usr/bin/python
#-*- coding:utf8 -*-

from optparse import OptionParser
import sys
import re

def minEditDist(sm , sn):
	m, n = len(sm) + 1, len(sn) + 1
	
	# create a matrix (m*n)

	matrix = [[0]*n for i in range(m)]

	matrix[0][0] = 0

	for i in range(1, m):
		matrix[i][0] = matrix[i-1][0] + 1
	
	for j in range(1, n):
		matrix[0][j] = matrix[0][j-1] + 1	


	for i in range(m):
		print matrix[i]

	print "------------------------------------------------------------"	
	print ""

	cost = 0
	idx = 0

	for i in range(1,m):
		for j in range(1,n):
			if sm[i-1] == sn[j-1]:
				cost = 0
			else:
				cost = 1
			matrix[i][j] = min(matrix[i-1][j]+1, matrix[i][j-1]+1, matrix[i-1][j-1]+cost)
			idx += 1
			#print "sm["+str(i)+"-1: "+sm[i-1]+" sn["+str(j)+"-1]: " + sn[j-1] + " idx: " + str(idx) + " i: " + str(i) + " j: " + str(j) 
			print "sm["+str(i)+"-1]: "+sm[i-1]+" sn["+str(j)+"-1]: " + sn[j-1] + " idx: " + str(idx) 
			for k in range(m):
				print matrix[k]

			print ""

	return matrix[m-1][n-1]

	

		

def main( argv ):
	str1 = argv[1].decode('utf-8')
	str2 = argv[2].decode('utf-8')

	print "str1: " + str1
	print "str2: " + str2

	print ""

	result = minEditDist( str1, str2)
	print "result: " + str(result)

if __name__=="__main__":
        main(sys.argv)

