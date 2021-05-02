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

    all_http_errors = [i.text for i in soup.find_all("dt")]

    # print(all_http_errors)

    # print(len(all_http_errors))  # 97

    with open('http_errors.csv', 'w', newline='') as csvfile:
        result_writer = csv.writer(csvfile, delimiter=' ',
                                   quotechar=' ', quoting=csv.QUOTE_MINIMAL)

        for error in all_http_errors:
            result_writer.writerow([error])


#########--------- DRIVER CODE ---------#########
if __name__ == "__main__":
    list_http_errors()
