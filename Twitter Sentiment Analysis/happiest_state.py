import sys
import json
import re

scores = {} 
states = {}

def score():
	sent_file = open(sys.argv[1])
	for line in sent_file:
		term, score = line.split("\t") 
		scores[term] = int(score)  

def scoreTweets():
	tweet_count = 0
	tweet_file = open(sys.argv[2])
	for line in tweet_file:
		tweet_score = 0
		result = json.loads(line)
		place = result.get('place',None)
		user = result.get('coordinates', None)
		if place!=None:
			country_code = place.get('country_code',None)
			if country_code=='US':
				string = result.get('text','zz')
				state = place.get('full_name')[-2:]
				words = re.compile('\w+').findall(string)
				for word in words:
					word_score = int(scores.get(word,'0'))
					tweet_score = tweet_score + word_score
				tweet_count= tweet_count + 1
				states[state] = tweet_score - states.get(state,0)

def printStateScores():
    
    for key, value in sorted(states.items(), key=lambda kv: (kv[1], kv[0])):
        print (key) 
        break

def main():
	score()
	scoreTweets()
	printStateScores()

if __name__ == '__main__':
	main()