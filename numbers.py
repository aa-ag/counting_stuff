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

    inlinks = soup.find_all("p").find("a")

    for inlink in inlinks:
        print(inlink.string)

    # with open('names.csv', 'w', newline='') as csvfile:
    #     fieldnames = ['#', 'number', 'description']
    #     writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    #     writer.writeheader()


#########--------- DRIVER CODE ---------#########
if __name__ == "__main__":
    numbers_types()
