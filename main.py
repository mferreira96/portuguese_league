import requests
from bs4 import BeautifulSoup

myResults_file = requests.get("http://www.maisfutebol.iol.pt/resultadoseclassificacoes/128/Portugal/Primeira-Liga")

soup = BeautifulSoup(myResults_file.content, "html.parser")

table = soup.find("table", class_="tableJogosClass")
tr_tag = table.find("tr")
team = list(tr_tag.find("td", class_="team").children)[1].get_text()

print(team)
