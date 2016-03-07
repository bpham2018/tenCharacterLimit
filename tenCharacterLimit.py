import os

inFile = open( "input.txt", 'r' ) # opens the input file in read mode

if os.path.isfile ( "output.txt" ): # if output file already exists, opens it in read/write mode,
# otherwise creates it by opening it in write mode

	outFile = open( "output.txt", 'r+' ) # don't open in 'w' if don't have to because
	# 'w' is dangerous!	
		
else:

	outFile = open( "output.txt", 'w' )

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