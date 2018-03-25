import requests
from bs4 import BeautifulSoup

myResults_file = requests.get("http://www.meusresultados.com/futebol/portugal/primeira-liga/")

soup = BeautifulSoup(myResults_file.text, "html.parser")

table_of_results = soup.find_all("table", class_="soccer")

test_id = soup.find("tr", id="g_1_tdTHicx5")
print(table_of_results)