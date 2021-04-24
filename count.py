#########--------- IMPORTS ---------#########
from bs4 import BeautifulSoup
import requests


#########--------- FUNCTIONS ---------#########
def count_html_elements():
    '''
      using `requests`, fetch url provided
      then create BeautifulSoup object with
      parsed data
    '''

    url = 'https://developer.mozilla.org/en-US/docs/Web/HTML/Element'

    page = requests.get(url)

    soup = BeautifulSoup(page.content, 'html.parser')

    print(soup)


#########--------- DRIVER CODE ---------#########
if __name__ == "__main__":
    count_html_elements()
