import numpy as np
import matplotlib.pyplot as plt
import shutil, os, sys 

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
  parser.add_option( '-f', '--filename', dest = 'filename', action = 'store', type = 'string', default = 'enabled.csv', help = 'Supply filename' )
  ( options, args ) = parser.parse_args()
  File = options.filename
else: 
  from optparse import OptionParser
  parser = OptionParser()
  parser.add_option( '-f', '--filename', dest = 'filename', action = 'store', type = 'string', default = 'enabled.csv', help = 'Supply filename' )
  ( options, args ) = parser.parse_args()
  File = options.filename

print( 'Input path: %s \n' % File )
with open( File, 'r' ) as f: 
  print 'First line reads: ' + f.readline().strip()
  print 'Number of columns: ' + str( len( f.readline().strip().split( ',' ) ) )

ts = raw_input( 'Analyze time stamp? (y/n)    ' ) 
if ts == 'y' or ts == 'yes' or ts == 'Yes':
  useTime = True
  lineindex=0
  timestamp = []
  for line in open( File, 'r' ):
    vals = line.split( ',' )
    Hour = str( int( float( vals[ 0 ] ) ) )
    Minute = str( int( float( vals[ 1 ] ) ) )
    Second = str( float( float( vals[ 2 ] ) ) + float( vals[ 3 ] ) )
    time = float( Hour )*60*60 + float( Minute )*60 + float( Second )
    if lineindex == 0: starttime = time
    time = time-starttime
    lineindex = lineindex + 1
    timestamp.append( time ) 
  print 'Independent variable set to timestamp. \nTimestamp fills indices 0-3.'
  
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

if useTime: plt.plot( timestamp, valY, 'ro' )
else: plt.plot( valX, valY, 'ro' )
plt.show() 
