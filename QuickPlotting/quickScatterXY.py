### quickScatterXY.py
# This script analyzes a CSV file to produce a scatter plot of the specified dependent vs indepent columns 

import numpy as np
import matplotlib.pyplot as plt
import shutil, os, sys 

def setTimeUnits( timestamps ):
	timer = []
	timeUnits = str( raw_input( 'Plot time in seconds? Minutes? Hours? (s, m, h)   ') )
	unitDEFN = { 'h': ( 60.0*60.0, 'hr' ) , 'm': ( 60.0, 'min' ), 's': ( 1.0, 'sec' ) }
	conversion = unitDEFN[ timeUnits ][ 0 ]
	for i in timestamp:
		timer.append( i / conversion ) 
	return timer, unitDEFN[ timeUnits ][ 1 ]

def runStats( vals ):
  ar = np.asarray( vals ).astype( np.float )
  Max = np.amax( ar )
  Min = np.amin( ar )
  Range = Max - Min
  Mean = np.mean( ar )
  RMS = np.std( ar )
  return Max, Min, Range, Mean, RMS

def runStatsNonzero( vals ):
  ar = np.asarray( vals ).astype( np.float )
  ar = ar[ np.nonzero( ar ) ] 
  Max = np.amax( ar )
  Min = np.amin( ar )
  Range = Max - Min
  Mean = np.mean( ar )
  RMS = np.std( ar )
  return Max, Min, Range, Mean, RMS

def statReport( vals ):
  stats = runStats( vals )
  print ' Max: %.6f \n Min: %.6f \n Range: %.6f \n Mean: %.6f \n RMS: %.6f \n' % ( stats[ 0 ], stats[ 1 ], stats[ 2 ], stats[ 3 ], stats[ 4 ] )
  stats = runStatsNonzero( vals )
  print '---- (TRIMMED) ----\n Max: %.6f \n Min: %.6f \n Range: %.6f \n Mean: %.6f \n RMS: %.6f \n' % ( stats[ 0 ], stats[ 1 ], stats[ 2 ], stats[ 3 ], stats[ 4 ] )

def calculateEfficiency( vals ):
  ar = np.array( vals ).astype( np.float )
  nSuccess = float( np.count_nonzero( ar ) )
  nTotal = float( len( vals ) )
  eff = ( nSuccess/nTotal )*100.00
  print ' Efficiency = %.6f' % eff

if sys.platform == 'ios': 
  import console, appex
  console.clear()
  File = appex.get_file_path()
elif sys.platform == 'darwin': 
  from optparse import OptionParser
  parser = OptionParser()
  parser.add_option( '-f', '--filename', dest = 'filename', action = 'store', type = 'string', default = '', help = 'Supply filename' )
  ( options, args ) = parser.parse_args()
  File = options.filename
else: 
  from optparse import OptionParser
  parser = OptionParser()
  parser.add_option( '-f', '--filename', dest = 'filename', action = 'store', type = 'string', default = '', help = 'Supply filename' )
  ( options, args ) = parser.parse_args()
  File = options.filename
  
print( 'Input path: %s \n' % File )
with open( File, 'r' ) as f: 
  print 'First line reads: ' + f.readline().strip()
  print 'Number of columns: ' + str( len( f.readline().strip().split( ',' ) ) )

ts = raw_input( 'Analyze time stamp? (y/n)    ' ) 
if ts == 'y' or ts == 'yes' or ts == 'Yes':
  useTime = True
  colIndex = int( raw_input( 'In which column does time data begin?    ' ) )
  lineindex=0
  timestamp = []
  for line in open( File, 'r' ):
    vals = line.split( ',' )
    Hour = str( int( float( vals[ colIndex + 0 ] ) ) )
    Minute = str( int( float( vals[ colIndex + 1 ] ) ) )
    Second = str( float( float( vals[ colIndex + 2 ] ) ) + float( vals[ colIndex + 3 ] ) )
    time = float( Hour )*60*60 + float( Minute )*60 + float( Second )
    if lineindex == 0: starttime = time
    time = time-starttime
    lineindex = lineindex + 1
    timestamp.append( time ) 
  print 'Independent variable set to timestamp. \nTimestamp fills indices %d-%d.' % ( colIndex, colIndex + 3 )
  
else:  
  useTime = False
  X = int( raw_input( 'Independent variable column index: ' ) )
Y = int( raw_input( 'Dependent variable column index: ' ) )

if not useTime: valX = []
valY = []

for line in open( File, 'r' ):
	l = line.split( ',' )
	if not useTime: valX.append( l[ X ] )
	valY.append( l[ Y ] )

print '\nDependent variable analysis: \n'
statReport( valY ) 
calculateEfficiency( valY )

print '\nPreparing plot...'
bGrid = bool( raw_input( 'Grid the plots? (True/False)   ' ) )
plt.figure( 1 )
plt.clf()
plt.subplot( 211 )
if useTime: 
	( timer, tu ) = setTimeUnits( timestamp )
	plt.plot( timer, valY, 'ro' )
	plt.xlabel( 'time [%s]' % tu )
else: plt.plot( valX, valY, 'ro' )
plt.grid( bGrid )

# Repeat plotting without the failed entries
plt.subplot( 212 )
aY = np.asarray( valY ).astype( np.float )
if useTime:
	aT = np.array( timer ).astype( np.float )
	plt.plot( aT[ np.nonzero( aY ) ], aY[ np.nonzero( aY ) ], 'b-' )
	plt.xlabel( 'time [%s]' % tu )
else:
	aX = np.array( valX ).astype( np.float )
	plt.plot( aX[ np.nonzero( aY ) ], aY[ np.nonzero( aY ) ], 'b-' )
plt.ylabel( 'Trimmed result' )
plt.grid( bGrid )
plt.show() 
