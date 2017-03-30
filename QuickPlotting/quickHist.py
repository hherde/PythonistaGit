### quickHist.py
# This script analyzes a CSV file to produce a histogram of the specified column

import numpy as np
import matplotlib.mlab as mlab
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

X = int( raw_input( 'Independent variable column index: ' ) )

valX = []

for line in open( File, 'r' ):
	l = line.split( ',' )
	valX.append( l[ X ] )

print '\nDependent variable analysis: \n'
statReport( valX ) 
calculateEfficiency( valX )

print '\nPreparing plot...'
nbins = int( raw_input( 'How many bins?  ' ) )
bNorm = bool( raw_input( 'Normalize? (True/False)  ' ) )

plt.figure( 1 )
plt.clf()
plt.subplot( 211 )
aX = np.array( valX ).astype( np.float )
n, bins, patches = plt.hist( aX, nbins, normed=bNorm, facecolor='green', alpha=0.75)
# add a 'best fit' line
y = mlab.normpdf( bins, runStats( valX )[ 3 ], runStats( valX )[ 4 ] )
l = plt.plot( bins, y, 'r--', linewidth=1 )
plt.grid( True )

# Repeat plotting without the failed entries
plt.subplot( 212 )
n, bins, patches = plt.hist( aX[ np.nonzero( aX ) ], nbins, normed = bNorm )
y = mlab.normpdf( bins, runStats( valX )[ 3 ], runStats( valX )[ 4 ] )
l = plt.plot( bins, y, 'r--', linewidth=1 )
plt.ylabel( 'Trimmed result' )
plt.grid( True ) 
plt.show()
