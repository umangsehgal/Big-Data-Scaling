import sys
import json
import re

instances = {} 

def getHashTags():
	tweet_file = open(sys.argv[1])
	for line in tweet_file:
		result = json.loads(line)
		e = result.get('entities', None)
		if e!=None:
			h = e.get('hashtags',None)
			if h!=None:
				for i in range(0, len(h)):
					term = h[i].get('text')
					instances[term] = int(instances.get(term,0))-1

def frequencies():
	count = 0
	for key, value in sorted(instances.items(), key=lambda kv: (kv[1], kv[0])):
		if key!='' and count<10:
			print(key, -instances[key])
			count = count+1

def main():
	getHashTags()
	frequencies()

if __name__ == '__main__':
	main()