### BASED ON mmcfre/Save-Script

import console, sys, clipboard, datetime

console.clear()
today = datetime.datetime.now()
print today 

import appex, shutil, os 

def getUniqueName( filename, ext ):
	root, extension = os.path.splitext( filename )
	if ext != '': extension = ext
	filename = root + extension 
	filenum = 1
	while os.path.isfile( filename ): 
		filename = '{} {}{}'.format( root, filenum, extension )
		filenum += 1
	return filename
	
def main(): 
	console.clear()
	dest_path_short = '~/Documents/inbox'
	dest_path = os.path.expanduser( dest_path_short )
	if not os.path.isdir( dest_path ): 
		print( 'Creating ' + dest_path_short )
		os.mkdir( dest_path )
	if not appex.is_running_extension():
		print( 'Using clipboard content...' )
		text = clipboard.get()
		assert text, 'No text on the clipboard!'
		resp = console.alert( 'Alert!', 'Select file extension', '.py', '.pyui', hide_cancel_button = False )
		if resp == 1: ext = '.py'
		elif resp == 2: ext = '.pyui'
		filename = os.path.join( dest_path, 'clipboard' )
		filename = getUniqueName( filename, ext )
		while os.path.isfile( filename ): 
			filename = '{} {}{}'.format( root, filenum, extension )
			filenum += 1
		with open( filename, 'w' ) as f: 
			f.write( text )
		print( 'Finished writing ' + filename + ' to Pythonista.' )
	else: 
		file = appex.get_file_path()
		print( 'Input path: %s ' % file )
		filename = os.path.join( dest_path, os.path.basename( file ) )
		filename = getUniqueName( filename, '' )
		shutil.copy( file, filename )
	print( 'Saved %s in %s ' % ( filename, dest_path_short ) )
	if not os.path.exists( filename ): print( ' > Error: file %s not found!' % os.path.basename( filename ) )
	else: print( ' > as %s' % os.path.basename( filename ) )
		
if __name__ == '__main__':
	main()
