inFile = open( "input.txt", 'r' )

outFile = open( "output.txt", 'r+' )

originalMessage = inFile.readlines()

numberMessageLines = len( originalMessage )

lineNumber = 0

while numberMessageLines > lineNumber:
	
	singleLine = originalMessage[ lineNumber ]
	
	if len( singleLine ) <= 10: 
		
		singleLine = singleLine[ : -1 ]
	
	outFile.write( singleLine [0:10] + "\n" )
	
	lineNumber += 1
