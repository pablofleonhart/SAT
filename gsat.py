from random import *
import sys
import time
import resource

def main():
	param = sys.argv[1:]

	file = open( param[0], "r" )
	finish = False
	read = False

	m = 0	# variables
	n = 0	# clauses
	clauses = []	# set of clauses
	clause = []

	while not finish:
	    line = file.readline()

	    if not line:
	        finish = True

	    else:
	    	#print line.split( "0" )
	        line = line.split()
	        
	        if len( line ) > 0:
	            if line[0] == 'p':
	                n = int( line[2] )
	                m = int( line[3] )
	                read = True

	            elif read:
	            	for i in xrange( len( line ) ):
	            		if line[i] == '0':
	            			clauses.append( clause )
	            			clause = []
	            		else:
	            			clause.append( line[i] )

	if len( clauses ) < m:
		clauses.append( clause )            		

	maxFlips = 3*n 	# number of search's restarts
	maxTries = 100	# amount of time to spend looking for an assignment
	seed = 1001

	print m, n
	print clauses, len( clauses )

	for i in xrange( m ):
		print clauses[i], "and"

	for i in xrange( maxTries ):
		# T = generates randomly truth assignment
		t = generateAttempt( n+1, seed )
		for j in xrange( maxFlips ):
			res = satisfies( t, clauses )
			if res[0]:
				print 'OK'
			# if T is satisfied, return T
			# p ?
			# T ??
			p = 0

	v = generateAttempt( n+1, seed )
	#v = random.randrange( 0, 1, n+1 )
	print v
	print satisfies( v, clauses )

def generateAttempt( n, s ):
	seed( s )
	result = []
	for i in xrange( n ):
		result.append( randint( 0, 1 ) )

	return result

def invValue( v ):
	if v == 0:
		return 1
	else:
		return 0

def satisfies( vec, clauses ):
	res = [] # values from each clause
	ins = [ 0 for i in xrange( len( vec ) )] # number of clauses insatisfied ( by variable )
	sat = 1

	for c in clauses:
		s = 0 # value of clause
		for i in xrange( len( c ) ):
			ab = abs( int( c[i] ) )
			if int( c[i] ) < 0:
				value = invValue( vec[ab] )
			else:
				value = vec[ab]

			s += value
			#print c[i], int( c[i] ) > 0, ab, value
		#print c, s
		if s == 0:
			for i in xrange( len( c ) ):
				ab = abs( int( c[i] ) )
				ins[ab] += 1

			sat = 0

		res.append( s )

	#print res
	#print ins
	return ( sat == 1, ins )

main()