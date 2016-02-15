from datetime import datetime
import json
import random

import twitter as tw

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
        'does trump seem like a good presidential candidate?',
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
    if datetime.now().weekday == 3:
        return random.choice(yes_opts) 
    else:
        return random.choice(no_opts) 
 

def send_tweet(event, context):
    """Post tweet
    """
    with open("twitter_credentials.json", "r") as f:
        credentials = json.load(f)
    t = tw.Api(**credentials)
    try:
        status = tweet_content()
        t.PostUpdate(status=status)
        return "Tweeted {}".format(status)
    except Exception as e:
        return e.message

if __name__ == '__main__':
    print tweet_content()
