#########--------- IMPORTS ---------#########
from bs4 import BeautifulSoup
import requests
import csv


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

    all_http_errors_titles = [i.text.lstrip(' ') for i in soup.find_all("dt")]

    all_http_errors_descriptions = [j.text for j in soup.find_all("dd")]

    all_http_errors = dict()

    for x in all_http_errors_titles:
        for y in all_http_errors_descriptions:
            all_http_errors[x] = y

    print(all_http_errors)


#########--------- DRIVER CODE ---------#########
if __name__ == "__main__":
    list_http_errors()
