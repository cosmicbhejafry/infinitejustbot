
import tweepy
import random
import pandas as pd
import time
from datetime import datetime as dt
from os import environ

consumer_key = environ[consumer_key]
consumer_secret =  environ[consumer_secret]
access_token = environ[access_token]
access_token_secret = environ[access_token_secret]

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)


df1 = pd.read_csv("./infinitejest_twitter_rows.csv", encoding='latin-1')

def get_twt(df,currtime,injustix=3):

  if(currtime[3]==4 and currtime[4]==20):
    tweet='fake funda'
    return tweet

  readRow = random.randrange (1,len(df.index))
  cointoss = random.randrange(1,injustix)
  if(cointoss==1):
    tweet = str(df.iat[readRow, 0])
  else:
    tweet = "just {}".format(dt.now().timestamp()) 
  
  return tweet

currtime = dt.now().timetuple()
glob_sleep_arr = [3600,3600*2,3600*3,3600*5,3600*8,3600*4,3600]
glob_dct = {2:0,3:1,5:2,8:3,13:4,21:5,1:6}
api.update_status("just {}".format(currtime[3]))
while currtime[2] < 31:
  currtime = dt.now().timetuple()
  tweet = get_twt(df1,currtime)    

  if len(tweet) < 280:
    if currtime[3] in glob_dct.keys():
      try:
        api.update_status(tweet)
      except:
        print("bt with {} at {}".format(tweet,currtime))      
      print("At {} have tweeted: {}".format(currtime[3],tweet)) 
      time.sleep(glob_sleep_arr[glob_dct[currtime[3]]])
    currtime = dt.now().timetuple()
  else:
    continue
