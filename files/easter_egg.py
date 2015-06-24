# funny
# easter eggs

# ask the user for a file
fname = raw_input("path to file >")

# validate file
try:
	fh = open(fname)
except:
	if fname == "say my name":
		print "Heisenberg"
		exit()
	else:
		print "Invalid path", fname
		exit()

i = 0

for line in fh:
	i += 1

print "num of lines: ", i