import time
import sys

import tweepy

from secrets import consumer_key, consumer_secret, access_token, access_token_secret

TWEET_LENGTH = 140


def ergenize(s):
	"""Replace all vowels with O"""
	for vowel in u'aeıioöuü':
		s = s.replace(vowel, 'o')
	for vowel in u'AEIİOÖUÜ':
		s = s.replace(vowel, 'O')		
	return s


def bot(api, text, first_wno=0, duration=60*60, send_tweets=False):
	"""Go over the words in a given text"""

	print('num chracters:', len(text), ', div by 140:', len(text) / 140) # 70234, 501.67	

	words = text.split()

	curr_len = 0
	tweet_no = 1
	tweet = []
	for n, w in enumerate(words[first_wno:]):
		length_after_new_word = len(' '.join(tweet + [w]))
		if  length_after_new_word > TWEET_LENGTH:
			text = ' '.join(tweet)
			print('TWEET #{} ({}-{})/{} {}'.format(tweet_no, n - len(tweet) + first_wno, n - 1 + first_wno, len(words), time.ctime(time.time())))
			print('Original: {}\nErgenized: {}\n'.format(text, ergenize(text)))
			if send_tweets:
				api.update_status(ergenize(text)) 
			tweet_no += 1
			tweet = [w]
			time.sleep(duration) # wait an hour
		else:
			tweet.append(w)


if __name__ == '__main__':
	auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(access_token, access_token_secret)
	api = tweepy.API(auth)

	filename = sys.argv[1]
	word_no = int(sys.argv[2])
	duration = int(sys.argv[3])
	send = bool(int(sys.argv[4]))

	with open(filename, 'rt') as f:
		text = f.read()		

	bot(api, text, first_wno=word_no, duration=duration, send_tweets=send)
