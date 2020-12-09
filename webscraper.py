import requests
import pprint 
from bs4 import BeautifulSoup

URL = "https://rexwordpuzzle.blogspot.com/2020/11/"
page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')

posts = soup.find_all('div', class_="post")

for post in posts:
	print(post.prettify())

print(len(posts))