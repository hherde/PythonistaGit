import appex, console, clipboard
import os

File = appex.get_file_path()
#print( File )

mydir = os.path.realpath( File ).strip( os.path.basename( File )  ) 
print( '\nFile is ' + os.path.basename( File ) + ' \nin directory ' + mydir + '\n')

showContent = bool( raw_input( 'Show contents of ' + mydir + '? (True/False)   ' ) )
if showContent:
	print( 'Also contained in this directory: ')
	console.quicklook( mydir )
copyPath = bool( raw_input( '\nCopy directory path to clipboard?  (True/False)  ' ) )
if copyPath: clipboard.set( mydir )
