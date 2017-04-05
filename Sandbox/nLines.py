import console, appex
File = appex.get_file_path()
i = 0
for line in open( File ): 
	i += 1
print i 
