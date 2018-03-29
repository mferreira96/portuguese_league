import requests
from bs4 import BeautifulSoup


def journey(): 
  myResults_file = requests.get("http://www.maisfutebol.iol.pt/resultadoseclassificacoes/128/Portugal/Primeira-Liga")

  soup = BeautifulSoup(myResults_file.content, "html.parser")

  jr = soup.find("div", class_="jrj")

  number_of_journey = list(jr.find("div", class_="tabelaTitle").children)[2].strip()
  print(number_of_journey)

  list_of_games = jr.find("div", class_="tableJogos").find_all("li")

  for info in list_of_games:
    if "dateRow" in info.get("class"):
      printDate(info)
    elif "JgTerminado" in info.get("class"):
      printFinishedGame(info)
    else:
      printGame(info)  

def printDate(info):
  print()
  print(info.get_text().strip())  


def printGame(info):

  home = list(info.find_all("span"))[0].get_text().strip()
  time = list(info.find_all("span"))[1].get_text().strip()
  opponent = list(info.find_all("span"))[2].get_text().strip()

  print("{:>15}".format(home), "{:6}".format(time), "{:15}".format(opponent), sep="  ")
      
def printFinishedGame(info):
  print(list(info.find_all("span")))

  home = list(info.find_all("span"))[0].get_text().strip()
  home_score = list(info.find_all("span"))[1].get_text().strip()
  opponent_score = list(info.find_all("span"))[2].get_text().strip()
  opponent = list(info.find_all("span"))[3].get_text().strip()

  print("{:>15}".format(home), "{:6}".format(home_score), " - ", "{:6}".format(opponent_score), "{:15}".format(opponent), sep="  ")

journey()
