# count the lines in a txt file

fh = open("mbox.txt")

i = 0

for line in fh:
	i += 1

print "num of lines: ", i