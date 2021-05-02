#########--------- IMPORTS ---------#########
from bs4 import BeautifulSoup
import requests
import csv


#########--------- FUNCTIONS ---------#########
def get_http_errors():
    '''
      using `requests`, fetch url provided
      then create BeautifulSoup object with
      parsed data, count lenth of list created by `find_all()`
      and finally, create csv with entire list
    '''

    # grab info from source
    url = 'https://en.wikipedia.org/wiki/List_of_HTTP_status_codes'

    page = requests.get(url)

    soup = BeautifulSoup(page.content, 'html.parser')

    # grab titles and descriptions to create dict with both
    http_errors_titles = [i.text.lstrip(' ') for i in soup.find_all("dt")]

    http_errors_descriptions = [j.find_next(
        'dd').text for j in soup.find_all("dt")]

    all_http_errors = dict(zip(http_errors_titles, http_errors_descriptions))

    f = open('http_errors.txt', 'w')

    for error, description in all_http_errors.items():
        f.write(f"{error} - {description}\n")


#########--------- DRIVER CODE ---------#########
if __name__ == "__main__":
    get_http_errors()
