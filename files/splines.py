# print the 1st line of a file

fh = open("mbox.txt")

for line in mbox:
	if line.startwith("From "):
		print line
		