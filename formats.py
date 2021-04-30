#########--------- IMPORTS ---------#########
from bs4 import BeautifulSoup
import requests


#########--------- FUNCTIONS ---------#########
def count_formats_elements():
    '''
      using `requests`, fetch url provided
      then create BeautifulSoup object with
      parsed data, count lenth of list created by `find_all()`
      and finally, create txt with entire list
    '''

    url = 'https://en.wikipedia.org/wiki/List_of_file_formats'

    page = requests.get(url)

    soup = BeautifulSoup(page.content, 'html.parser')

    print(len(soup.find_all()))  # 5326

    f = open('formats.txt', 'w')

    for ul in soup.find_all('ul'):
        f.write(''.join(ul.findAll(text=True)))


#########--------- DRIVER CODE ---------#########
if __name__ == "__main__":
    count_formats_elements()
