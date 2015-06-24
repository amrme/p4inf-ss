# read the contents of a file 
# and print all lns in UpperCase

# ask the user for a file
fname = raw_input("path to file >")

# validate file
try:
	fh = open(fname)
except:
	print("Invalid path")
	exit

# pt all lines
for line in fh:
	print(line.upper().strip())