import numpy as np
import matplotlib.pyplot as plt
import shutil, os, sys 

if sys.platform == 'ios': 
  import console, appex
  console.clear()
  file = appex.get_file_path()
elif sys.platform == 'darwin': 
  from optparse import OptionParser
  parser = OptionParser()
  parser.add_option( '-f', '--filename', dest = 'filename', action = 'store', type = 'string', default = 'enabled.csv', help = 'Supply filename' )
  ( options, args ) = parser.parse_args()
  file = options.filename
else: 
  from optparse import OptionParser
  parser = OptionParser()
  parser.add_option( '-f', '--filename', dest = 'filename', action = 'store', type = 'string', default = 'enabled.csv', help = 'Supply filename' )
  ( options, args ) = parser.parse_args()
  file = options.filename

print( 'Input path: %s \n' % file )

X = int( raw_input( 'Independent variable column index: ' ) )
Y = int( raw_input( 'Dependent variable column index: ' ) )
valX = []
valY = []
for line in open( file, 'r' ):
	l = line.split( ',' )
	valX.append( l[ X ] )
	valY.append( l[ Y ] )
print '\n End of file'

plt.plot( valX, valY, 'ro' )
plt.show() 
