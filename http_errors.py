#########--------- IMPORTS ---------#########
from bs4 import BeautifulSoup
import requests


#########--------- FUNCTIONS ---------#########
def list_http_errors():
    '''
      using `requests`, fetch url provided
      then create BeautifulSoup object with
      parsed data, count lenth of list created by `find_all()`
      and finally, create csv with entire list
    '''

    url = 'https://en.wikipedia.org/wiki/List_of_HTTP_status_codes'

    page = requests.get(url)

    soup = BeautifulSoup(page.content, 'html.parser')

    all_http_errors = [i.text for i in soup.find_all("dt")]

    print(all_http_errors)

    print(len(all_http_errors))


#########--------- DRIVER CODE ---------#########
if __name__ == "__main__":
    list_http_errors()