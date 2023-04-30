from bs4 import BeautifulSoup
import requests

result = requests.get("www.google.com")

content = result.text

soup = BeautifulSoup(content,'lxml')

# soup.find(id="specific_id")
# soup.find('tag',class_="class_name")
# find will returns the single element
soup.find('article',class_="main_article")
soup.find('h1')

# To locate multiple elements by it's tag name, returns list
# obtain multiple elements, all the elements will be stored in a list
soup.find_all("h2")


