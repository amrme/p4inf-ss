# print the 1st line of a file

fh = open("mbox.txt")

for line in fh:
	if line.startswith("From "):
		print line[4:].strip()
