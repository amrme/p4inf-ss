# calculate the average spam confidence in a mbox text file

# ask the user for a file
fname = raw_input("path to file >")

# validate file
try:
	fh = open(fname)
except:
	print("Invalid path")
	exit()

# loop over all lns
sumSpam = 0
count = 0
for line in fh:
	# ignore each line that wout "X-DSPAM-Confidence:"
	if  line.find("X-DSPAM-Confidence:") == -1 :
		continue
	count += 1
	sumSpam = sumSpam + float(line[line.find(":")+2:])

print "Average spam confidence: ", sumSpam/count
