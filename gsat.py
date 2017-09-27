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

	maxFlips = n 	# number of search restarts
	maxTries = 100	# amount of time to spend looking for an assignment

	print m, n
	print clauses, len( clauses )

	for i in xrange( m ):
		print clauses[i], "and"

	for i in xrange( maxTries ):
		# T = generates randomly truth assignment
		for j in xrange( maxFlips ):
			# if T is satisfied, return T
			# p ?
			# T ??
			p = 0

def generateAttempt( n ):

main()