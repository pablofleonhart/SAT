import os
import time
from gsat import GSat

def mean( data ):
    n = len( data )
    if n < 1:
        return 0.00

    return sum( data ) / n

def _ss( data ):
    c = mean( data )
    ss = sum( ( x - c ) ** 2 for x in data )
    return ss

def pstdev( data ):
    n = len( data )
    if n < 2:
        return 0.00
    ss = _ss( data )
    pvar = ss / n
    return pvar ** 0.5

pattern = "{:9s}{:14s}{:7s}{:7s}{:4s}{:10s}"
file = open( "results.txt", 'w' )
file.write( pattern.format( "alg", "instance", "rep", 't', 'p', 'i' ) + '\n' )

ti = []
period = []
iteration = []

files = [ "flat50-1.cnf", "flat75-1.cnf", "flat100-1.cnf", "par8-5-c.cnf" ]

for f in files:
	filename = "files/" + f
	gsat = GSat( filename )
	
	for i in xrange( 1, 16 ):		
		start = time.time()
		res = gsat.run()
		end = time.time()
		drt = end - start

		nfile = f.replace( ".cnf", '' )

		if res == 'Insatisfied':
			pattern = "{:9s}{:14s}{:<7d}{:<7s}{:<4s}{:<10s}"
			file.write( pattern.format( "gsat", nfile, i, "NA", "NA", "NA" ) + '\n' )
			ti.append( 0 )
			period.append( 0 )
			iteration.append( 0 )

		else:
			pattern = "{:9s}{:14s}{:<7d}{:<7.2f}{:<4d}{:<10d}"
			file.write( pattern.format( "gsat", nfile, i, drt, res[1], res[2] ) + '\n' )
			ti.append( drt )
			period.append( res[1] )
			iteration.append( res[2] )

		print "gsat", i, drt

	print "gsat " + nfile + " " + str( '{0:,.2f}'.format( mean( ti ) ) ), str( '{0:,.2f}'.format( pstdev( ti ) ) )
	print "gsat " + nfile + " " + str( '{0:,.2f}'.format( mean( period ) ) ), str( '{0:,.2f}'.format( pstdev( period ) ) )
	print "gsat " + nfile + " " + str( '{0:,.2f}'.format( mean( iteration ) ) ), str( '{0:,.2f}'.format( pstdev( iteration ) ) )

file.close()