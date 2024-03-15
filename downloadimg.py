import tweepy

# Set up your Twitter API credentials
consumer_key = 'QHT5kQK2FO01yuzWT3cMneZpj'#WjlaSTFzeGE4QkoyeW4wUDlNbWc6MTpjaQ
consumer_secret = 'pO10SMn5ZkRjm8S7J3ErCp1gr57gStqfY1nOPW9FsHTHLM19RO'#WW3ctzmbAEzQXAwK_Rk5liWzhPffoaK2w6annkDf89HSDv42fM
access_token = '1619035967872016384-hdq8gscebGd9mh14BNWF05Rv4RaLEr'
access_token_secret = 'GUyhSKifoj1lEwddV1DBFyg6AFkj2Vevvax1lwHwME08g'

# Authenticate with Twitter
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# Update your status (tweet "Hello Test")
api.update_status("Hello Test")

print("Tweeted: Hello Test")