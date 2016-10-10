from bs4 import BeautifulSoup
import requests

search_terms = input ("Search for a GIF")
url = "http://www.giphy.com/search/" + search_terms

response = requests.get(url)
soup = BeautifulSoup(response.text,'html.parser')
