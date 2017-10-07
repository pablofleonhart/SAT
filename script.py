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

file = open( "walkresults.txt", 'r' )

finish = False
alg = ""
ti = []
period = []
iteration = []

while not finish:
	line = file.readline().split()
	if not line:
		finish = True

	elif line[0] != 'alg':
		if line[1] != alg:
			if alg == "":
				alg = line[1]
			else:
				print "gsat " + alg + " " + str( '{0:,.2f}'.format( mean( ti ) ) ), str( '{0:,.2f}'.format( pstdev( ti ) ) )
				print "gsat " + alg + " " + str( '{0:,.2f}'.format( mean( period ) ) ), str( '{0:,.2f}'.format( pstdev( period ) ) )
				print "gsat " + alg + " " + str( '{0:,.2f}'.format( mean( iteration ) ) ), str( '{0:,.2f}'.format( pstdev( iteration ) ) )
				alg = line[1]

		ti.append( float( line[3] ) )
		period.append( int( line[4] ) )
		iteration.append( int( line[5] ) )

file.close()
print "gsat " + alg + " " + str( '{0:,.2f}'.format( mean( ti ) ) ), str( '{0:,.2f}'.format( pstdev( ti ) ) )
print "gsat " + alg + " " + str( '{0:,.2f}'.format( mean( period ) ) ), str( '{0:,.2f}'.format( pstdev( period ) ) )
print "gsat " + alg + " " + str( '{0:,.2f}'.format( mean( iteration ) ) ), str( '{0:,.2f}'.format( pstdev( iteration ) ) )