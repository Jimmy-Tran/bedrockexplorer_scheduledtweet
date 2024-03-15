
import requests
from bs4 import BeautifulSoup

url = "https://www.bedrockexplorer.com/@2-tail-productions/axolotls"
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

#bearer
#AAAAAAAAAAAAAAAAAAAAAI7ulQEAAAAAMI9M%2BFIYrBsb%2FnW3GtOPjYDsym4%3Dh99NcjKy4LwypgMkzbvrdko8MPyW4WfL5iEPhh1AfzFSzbqXlX
#api secret
#oz2FUBo8Fj68OVWzk0IYhBH7qviXI8qLECs4bUYWKkn6g3ZuSK
#api
#6wzICRa2QlG67R96jiMaAzRJC

#access token
#1619035967872016384-qyLIEWzUB7UwGYknrxv9YmjIRutuyQ
#token secret
#DpMKz3Ga4HJvRlS5OfFBC9rCqg1uGxQ9BVboZQKB6RVzo

#minecraft #minecraftskin #minecraftskins #blockbench #Art'

twitter_layout = desc[0] + "\n\nGet it now on the\n@MinecraftMarket\n\n" + a_src + "\n\n#minecraft #minecraftskin #minecraftskins #blockbench #Art"
print(twitter_layout)
print(img_src)