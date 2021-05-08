#########--------- IMPORTS ---------#########
from bs4 import BeautifulSoup
import requests


#########--------- FUNCTIONS ---------#########
def count_programming_languages():
    url = 'https://www.wikiwand.com/en/List_of_programming_languages'

    page = requests.get(url)

    soup = BeautifulSoup(page.content, 'html.parser')

    print(soup)


#########--------- DRIVER CODE ---------#########
if __name__ == "__main__":
    count_programming_languages()
