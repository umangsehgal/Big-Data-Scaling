import sys
import re
import json

scores = {}
newscores = {}
instances = {}

def scores_calc(file1):
    for line in file1:
        term, score = line.split("\t")
        scores[term] = int(score)

def score_tweets(file2):
    tweet_count = 1
    for line in file2:
        tweet_score = 0
        result = json.loads(line)
        string = result.get('text','zz')
        new_words = []
        words = string.strip().split() 
        for word in words:
            word_score = int(scores.get(word,10000)) 
            if word_score == 10000:
                new_words.append(word)
            else:
                tweet_score += word_score
        for word in new_words:
        	newscores[word] = newscores.get(word,0) + tweet_score 
        tweet_count += 1

def display_words():
	for key, value in sorted(newscores.items(), key=lambda kv: (kv[1], kv[0])):
	    print(key, value)

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    scores_calc(sent_file)
    score_tweets(tweet_file)
    display_words()

if __name__ == '__main__':
    main()
