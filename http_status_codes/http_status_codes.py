#########--------- IMPORTS ---------#########
from bs4 import BeautifulSoup
import requests


#########--------- FUNCTIONS ---------#########
def get_http_status_codes():
    '''
      using `requests`, fetch url provided
      then create BeautifulSoup object with
      parsed data, count lenth of list created by `find_all()`
      and finally, create txt doc with all status codes and
      their descriptions
    '''

    # grab info from source
    url = 'https://en.wikipedia.org/wiki/List_of_HTTP_status_codes'

    page = requests.get(url)

    soup = BeautifulSoup(page.content, 'html.parser')

    # grab titles and descriptions to create dict with both
    http_status_titles = [i.text.lstrip(' ') for i in soup.find_all("dt")]

    http_status_descriptions = [j.find_next(
        'dd').text for j in soup.find_all("dt")]

    all_http_status = dict(
        zip(http_status_titles, http_status_descriptions))

    f = open('http_status.txt', 'w')

    for status, description in all_http_status.items():
        f.write(f"{status} - {description}\n")


#########--------- DRIVER CODE ---------#########
if __name__ == "__main__":
    get_http_status_codes()
