from bs4 import BeautifulSoup
# import  lxml
import requests

response = requests.get("https://www.empireonline.com/movies/features/best-movies-2/")

soup = BeautifulSoup(response.text,"html.parser")

block_item = soup.find('div', class_='block-item listicle_listicle__container__anuKG')

items = block_item.find_all('h3', class_='listicleItem_listicle-item__title__BfenH')

items = [item.getText() for item in items]

text_in_new_file = ''

for text_line in items[::-1]:
    text_in_new_file += text_line + '\n'

with open("100movie_letter.txt","w") as new_file:
        new_file.write(text_in_new_file)
