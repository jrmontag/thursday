from datetime import datetime
import json
import logging
import random

import twitter as tw

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def tweet_content():
    """Generate tweet string (140 characters or less)
    """
    # potential responses
    yes_opts = [ 
        'YEAAAA',
        'awwww yea',
        'you betcha',
        'BOOYAH',
        'well, whatdya know?',
        'does a giraffe have a long neck?',
        'how about that?!',
        'yes'
        ]
    no_opts = [
        'no',
        'of course not',
        'big tall glass of nope',
        'how about no, scott',
        'hang tight',
        'gotta wait it out',
        'yes, if today is also opposite day',
        'nope nope nope nope',
        'nuh uh',
        'inconceivably, no',
        'def no'
        ]
    # check Thursday (= 3) against current weekday (Monday=0)
    if datetime.now().weekday() == 3:
        return random.choice(yes_opts) 
    else:
        return random.choice(no_opts) 
 

def send_tweet(event, context):
    """Post tweet
    """
    logging.info('Time to send a Tweet')
    with open("twitter_credentials.json", "r") as f:
        credentials = json.load(f)
    logging.info('loaded a credentials file')
    t = tw.Api(**credentials)
    logging.info('sending tweet')
    try:
        status = tweet_content()
        t.PostUpdate(status=status)
        logging.info('Tweeted {}'.format(status))
        return "Tweeted {}".format(status)
    except Exception as e:
        logging.error('uh oh: {}'.format(e))
        return e.message

if __name__ == '__main__':
    print tweet_content()
