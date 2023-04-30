from bs4 import BeautifulSoup
import requests

result = requests.get("www.google.com")

content = result.text

soup = BeautifulSoup(content,'lxml')
