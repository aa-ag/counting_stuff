#########--------- IMPORTS ---------#########
from bs4 import BeautifulSoup
import requests
import csv


#########--------- FUNCTIONS ---------#########
def count_formats_elements():
    '''
      using `requests`, fetch url provided
      then create BeautifulSoup object with
      parsed data, count lenth of list created by `find_all()`
      and finally, create csv with entire list
    '''

    url = 'https://www.wikiwand.com/en/List_of_file_formats'

    page = requests.get(url)

    soup = BeautifulSoup(page.content, 'html.parser')

    all_formats = soup.find_all('top')

    print(all_formats)

    # print(len(all_formats_count))

    # with open('formats_result.csv', 'w', newline='') as csvfile:
    #     result_writer = csv.writer(csvfile, delimiter=' ',
    #                                quotechar='|', quoting=csv.QUOTE_MINIMAL)

    #     for html_element in all_html_elements_count:
    #         result_writer.writerow(html_element)


#########--------- DRIVER CODE ---------#########
if __name__ == "__main__":
    count_formats_elements()
