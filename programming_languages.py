#########--------- IMPORTS ---------#########
from bs4 import BeautifulSoup
import requests


#########--------- FUNCTIONS ---------#########
def count_programming_languages():
    url = 'https://en.wikipedia.org/wiki/List_of_programming_languages'

    page = requests.get(url)

    soup = BeautifulSoup(page.content, 'html.parser')

    lis = [li for li in soup.find_all("li")]

    print(lis)


#########--------- DRIVER CODE ---------#########
if __name__ == "__main__":
    count_programming_languages()
