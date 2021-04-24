#########--------- IMPORTS ---------#########
from bs4 import BeautifulSoup
import requests
import csv


#########--------- FUNCTIONS ---------#########
def count_html_elements():
    '''
      using `requests`, fetch url provided
      then create BeautifulSoup object with
      parsed data
    '''

    url = 'https://developer.mozilla.org/en-US/docs/Web/HTML/Element'

    page = requests.get(url)

    soup = BeautifulSoup(page.content, 'html.parser')

    all_html_elements_count = set(soup.find_all('code'))

    print(len(html_elements_count))  # 252

    with open('result.csv', 'w', newline='') as csvfile:
        result_writer = csv.writer(csvfile, delimiter=' ',
                                   quotechar='|', quoting=csv.QUOTE_MINIMAL)

        for html_element in all_html_elements_count:
            result_writer.writerow(html_element)


#########--------- DRIVER CODE ---------#########
if __name__ == "__main__":
    count_html_elements()
