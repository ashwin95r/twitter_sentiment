import json
import sys

f = open(sys.argv[1])

dic = {}
tot =0.0

for line in f:
	line1 = json.loads(line)
	try:
		for word in line1["text"].strip().split(' '):
			if word in dic.keys():
				dic[word.strip()] += 1.0
			else:
				dic[word.strip()] =1.0
			tot +=1.0
	except KeyError:
		continue
	
for item in dic:
	print item + ' ' + str(dic[item]/tot)	
	
