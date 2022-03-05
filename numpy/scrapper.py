# Scrapping website for text
from bs4 import BeautifulSoup
import requests
import re

# define scrapper function
def scrapper(url):
    # get the html
    response = requests.get(url)
    # parse the html
    soup = BeautifulSoup(response.text, "html.parser")
    # find the text
    text = soup.find_all(text=True)
    # remove the html tags
    output = filter(visible, text)
    # return the text
    return output