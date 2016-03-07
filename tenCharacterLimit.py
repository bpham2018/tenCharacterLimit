import os

inFile = open( "input.txt", 'r' )

if os.path.isfile ( "output.txt" ):

	outFile = open( "output.txt", 'r+' )
		
else:

	outFile = open( "output.txt", 'w' )

originalMessage = inFile.readlines()

numberMessageLines = len( originalMessage )

lineNumber = 0

while numberMessageLines > lineNumber:
	
	singleLine = originalMessage[ lineNumber ]
	
	if len( singleLine ) <= 10: 
		
		singleLine = singleLine[ : -1 ]
	
	outFile.write( singleLine [0:10] + "\n" )
	
	lineNumber += 1
