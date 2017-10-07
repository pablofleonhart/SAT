from operator import itemgetter
from random import *
import sys
import time
import resource

class GSat:
	m = 0	# variables
	n = 0	# clauses
	clauses = []	# set of clauses

	def __init__( self, filename ):
		file = open( filename, "r" )
		finish = False
		read = False
		
		clause = []

		while not finish:
		    line = file.readline()

		    if not line:
		        finish = True

		    else:
		        line = line.split()
		        
		        if len( line ) > 0:
		            if line[0] == 'p':
		                self.n = int( line[2] )
		                self.m = int( line[3] )
		                read = True

		            elif read:
		            	for i in xrange( len( line ) ):
		            		if line[i] == '0':
		            			self.clauses.append( clause )
		            			clause = []
		            		else:
		            			clause.append( line[i] )

		if len( self.clauses ) < self.m:
			self.clauses.append( clause )

		file.close()

	def run( self, tries ):
		maxFlips = 3 * self.n 	# number of search's restarts
		maxTries = tries		# amount of time to spend looking for an assignment
		seed = time.time()
		it = 0
		start = time.time()
		t = []
		while time.time() - start < tries:
		#for i in xrange( maxTries ):
			seed += 10000
			# generates randomly truth assignment
			t = self.generateAttempt( self.n + 1, seed )

			for j in xrange( maxFlips ):
				it += 1
				res = self.satisfies( t )
				if res[0]:
					return ( t, j, it )

				p = self.getVariable( res[1] )			
				t[p] = self.invValue( t[p] )
				#print p

		return ( 'Insatisfied' )

	def generateAttempt( self, n, s ):		
		seed( s )
		result = []
		for i in xrange( n ):
			result.append( randint( 0, 1 ) )

		return result

	def invValue( self, v ):
		if v == 0:
			return 1
		else:
			return 0

	def getVariable( self, vec ):
		mx = 0
		px = []
		#print vec
		#idxs, srd = zip( *sorted( enumerate( vec ), key=itemgetter( 1 ), reverse=True ) )		
		#tam = int( len( vec )*0.02 )
		#print srd[:tam], idxs[:tam]
		#change = self.reservoir_sampling( list( srd[:tam] ), list( idxs[:tam] ), 1 )
		#print self.qsort( vec )
		for i in xrange( 1, len( vec ) ):
			if vec[i] > mx:
				mx = vec[i]
				px = []
				px.append( i )
			elif vec[i] == mx:
				px.append( i )

		#print self.reservoir_sampling( px, 5 )
		if len( px ) == 1:
			return px[0]
		else:
			return choice( px )
		#return change[0]

	def reservoir_sampling( self, items, idxs, k ):
		""" 
		Reservoir sampling algorithm for large sample space or unknow end list
		See <http://en.wikipedia.org/wiki/Reservoir_sampling> for detail>
		Type: ([a] * Int) -> [a]
		Prev constrain: k is positive and items at least of k items
		Post constrain: the length of return array is k
		"""
		#print items, len( items )
		sample = items[0:k]
		isample = idxs[0:k]
		#print sample, isample

		for i in range( k, len( items ) ):
			j = randrange( 0, i + 1 )
			if j < k and items[i] > 0:
				sample[j] = items[i]
				isample[j] = idxs[i]

		return isample

	def satisfies( self, vec, ):
		res = [] # values from each clause
		ins = [ 0 for i in xrange( len( vec ) )] # number of clauses insatisfied ( by variable )
		sat = 1

		for c in self.clauses:
			s = 0 # value of clause
			for i in xrange( len( c ) ):
				ab = abs( int( c[i] ) )
				if int( c[i] ) < 0:
					value = self.invValue( vec[ab] )
				else:
					value = vec[ab]

				s += value

			if s == 0:
				for i in xrange( len( c ) ):
					ab = abs( int( c[i] ) )
					ins[ab] += 1

				sat = 0

			res.append( s )

		return ( sat == 1, ins )