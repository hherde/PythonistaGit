#coding: utf-8

import appex, console
import os

Files = appex.get_file_paths()
print( Files )

print( os.path.basename( Files[ 0 ] ) )
mydir = os.path.realpath( Files[ 0 ] ).strip( os.path.basename( File[ 0 ] )  ) 
print mydir 

for fname in Files: 
	with open( fname, 'r' ) as f: 
		print( '\n' + fname )
		print( 'First line reads: ' + f.readline().strip() )
		print( 'Number of columns: ' + str( len( f.readline().strip().split( ',' ) ) ) )

console.quicklook( mydir )
