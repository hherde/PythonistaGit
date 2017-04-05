nCaptures = 10.0 
scanRange = 0.8 #mm 
stepsize = 200.00 #um 
locations = 4.0
waittime = 5.0 #seconds

heights = scanRange/( stepsize/1000.0 )
print heights
nImages = heights*nCaptures

print 'Collecting %d images' % int( nImages*locations )
tSingle = nImages*waittime
tAll = tSingle*locations

print 'Single location scan will take %.2f minutes' % ( tSingle/( 60.0 ) ) 
print 'Full scan will take %.2f hours' % ( tAll/( 60.0*60.0 ) )
