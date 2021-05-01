#########--------- IMPORTS ---------#########
from bs4 import BeautifulSoup
import requests
import csv


#########--------- FUNCTIONS ---------#########
def numbers_types():
    '''
      using `requests`, fetch url provided
      then create BeautifulSoup object with
      parsed data, count lenth of list created by `find_all()`
      grabbing class and finally, create txt with entire list
    '''
    url = 'https://en.wikipedia.org/wiki/List_of_types_of_numbers'

    page = requests.get(url)

    soup = BeautifulSoup(page.content, 'html.parser')

    tags = {tag.name for tag in soup.find_all()}

    print(tags)


#########--------- DRIVER CODE ---------#########
if __name__ == "__main__":
    numbers_types()
    '''
     {'ol', 'td', 'h2', 'mstyle', 'link', 'nav', 
     'a', 'table', 'body', 'br', 'footer', 'mi', 
     'sup', 'tbody', 'i', 'noscript', 'span', 'div', 
     'li', 'h3', 'h1', 'script', 'abbr', 'img', 'th', 
     'tr', 'form', 'label', 'semantics', 'b', 'meta', 
     'head', 'mrow', 'annotation', 'ul', 'math', 'p', 
     'style', 'html', 'cite', 'title', 'input'}
    '''
