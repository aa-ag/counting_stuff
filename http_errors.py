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
    all_http_errors_titles = [i.text.lstrip(' ') for i in soup.find_all("dt")]

    # print(len(all_http_errors_titles)) # 97

    # all_http_errors_decriptions = [j.text for j in soup.find_all("dd")]

    f = open('http_errors.txt', 'w')

    for error in all_http_errors_titles:
        f.write(error + '\n')


#########--------- DRIVER CODE ---------#########
if __name__ == "__main__":
    get_http_errors()
