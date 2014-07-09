import json
import sys
import operator

f = open(sys.argv[1])

dic = {}
tot =0.0

for line in f:
	line1 = json.loads(line)
	try:
		for i in line1['entities']['hashtags']:
			if i['text'] in dic:
				dic[i['text']] += 1
			else:
			 	dic[i['text']] = 1		
	except IndexError :
		continue
	except KeyError:
		continue
i
x = sorted(dic.iteritems(), key=operator.itemgetter(1))

x = x[-11:]			
for i in range(10,0,-1) :
	print x[i][0]+ ' '+str(x[i][1])
