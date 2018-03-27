import requests
from bs4 import BeautifulSoup


def journey(): 
  myResults_file = requests.get("http://www.maisfutebol.iol.pt/resultadoseclassificacoes/128/Portugal/Primeira-Liga")

  soup = BeautifulSoup(myResults_file.content, "html.parser")



journey()  
