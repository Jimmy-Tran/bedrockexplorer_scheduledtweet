import tweepy
import requests
from bs4 import BeautifulSoup
import os

url = input(str("Enter a bedrockexplorer url\n"))
#https://www.bedrockexplorer.com/@2-tail-productions/axolotls
response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")

p_element = soup.select_one("p.text-justify")
img_element = soup.select_one("img#imgPdpKeyArt")
a_element = soup.select_one("a.btn.btn-lg.btn-play.btn-block")

text = p_element.text
img = img_element.txt
img_src = img_element['src']
a_src = a_element['href']

desc = text.split('◼')

twitter_layout = desc[0] + "\n\nGet it now on the\n@MinecraftMarket\n\n" + a_src + "\n\n#minecraft #minecraftskin #minecraftskins #blockbench #Art"

# Your Twitter API credentials
consumer_key = ''
consumer_secret = ''
access_token = ''
access_token_secret = ''

# Authenticate with Twitter API
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# Scheduled time for tweet (in hours)
scheduled_time = 1

# Upload image to Twitter
img_url = img_src
response = requests.get(img_url)

# save the image to a local file
with open("image.jpg", "wb") as f:
    f.write(response.content)

uploaded_img = api.media_upload("./image.jpg")

# Schedule tweet
api.update_status(status=twitter_layout, media_ids=[uploaded_img.media_id_string],scheduled_at=scheduled_time)
print("done")

#                  in_reply_to_status_id=None, auto_populate_reply_metadata=True,
       #           scheduled_at=scheduled_time