inFile = open( "input.txt", 'r' ) # opens the input file in read mode

outFile = open( "output.txt", 'w' )  # opens the output file in write mode- This will also create the file if it does not already exist

originalMessage = inFile.readlines() # creates a list of lines by reading from the input file

numberMessageLines = len( originalMessage ) # sets a variable equal the number of lines

lineNumber = 0

while numberMessageLines > lineNumber: # program will stop reading after last line of message
	
	singleLine = originalMessage[ lineNumber ] # selects the current line
	
	if len( singleLine ) <= 10: # deletes the "\n" if line was short enough to fit it
		
		singleLine = singleLine[ : -1 ]
	
	outFile.write( singleLine [0:10] + "\n" ) # writes characters 0-10 of line + "\n"
	
	lineNumber += 1 # adds to lineNumber to work towards terminating loop

inFile.close() # Always close files -dont want data to get corrupted
outFile.close()
