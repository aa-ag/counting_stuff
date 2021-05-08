#########--------- IMPORTS ---------#########
from bs4 import BeautifulSoup
import requests


#########--------- FUNCTIONS ---------#########
def count_programming_languages():
    url = 'https://en.wikipedia.org/wiki/List_of_programming_languages'

    page = requests.get(url)

    soup = BeautifulSoup(page.content, 'html.parser')

    lis = [li.find_next(
        'a').text for li in soup.find_all("li")]

    all_programming_languages = lis[35:-155]
    # print(len(all_programming_languages))  # 686

    f = open('languages.txt', 'w')

    for language in all_programming_languages:
        f.write(f"{language}\n")


#########--------- DRIVER CODE ---------#########
if __name__ == "__main__":
    count_programming_languages()
