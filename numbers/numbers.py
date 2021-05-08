#########--------- IMPORTS ---------#########
from bs4 import BeautifulSoup
import requests
import csv
import re


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

    numbers = {number.text for number in soup.find_all('p')}

    print(numbers)


#########--------- DRIVER CODE ---------#########
if __name__ == "__main__":
    numbers_types()
