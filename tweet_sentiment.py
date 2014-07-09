import json
import sys

afinnfile = open(sys.argv[1])
f = open(sys.argv[2])


scores = {} # initialize an empty dictionary
for line in afinnfile:
  term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
  scores[term] = int(score)  # Convert the score to an integer.

for line in f:
	score=0.0
	line1 = json.loads(line)
	try:
		for word in line1["text"].strip().split(' '):
			score += scores[word]
		print str(score) 		
	except KeyError:
		print '0.0'
