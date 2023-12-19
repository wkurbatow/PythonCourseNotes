from bs4 import BeautifulSoup
# import  lxml
import requests

response = requests.get("https://www.billboard.com/charts/hot-100/2023-09-25/")

soup = BeautifulSoup(response.text,"html.parser")
# print(soup.prettify())
block_item = soup.select('ul li ul li h3')
items = []
for item in block_item:
    txt = item.getText()
    x = txt.splitlines()
    x = [x1.strip() for x1 in x]
    x = [x1 for x1 in x if x1 != ''] 
    # print(x)
    items.append(x[0])
# print(items)
   
# items = [item.getText() for item in items]

text_in_new_file = ''

for text_line in items:
    text_in_new_file += text_line + '\n'
print(text_in_new_file)

with open("100track.txt","w") as new_file:
        new_file.write(text_in_new_file)
