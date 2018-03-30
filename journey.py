import requests, sys
from bs4 import BeautifulSoup

# if journey number is -1, it means that i want the last one
def journey(journey_number): 
  if journey_number is -1:
    myResults_file = requests.get("http://www.maisfutebol.iol.pt/resultadoseclassificacoes/128/Portugal/Primeira-Liga/")
  else:
    myResults_file = requests.get("http://www.maisfutebol.iol.pt/resultadoseclassificacoes/128/Portugal/Primeira-Liga/jogos_resultados_jornada.html?jornadaVisible=" + journey_number + "&filtro=ajax&competicao=128&epoca=9298&jtotal=34")

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
    elif "live" in info.get("class"):
      printLiveGame(info)  
    else:
      printGame(info)  

def printDate(info):
  print()
  print(info.get_text().strip())  


def printGame(info):

  home = list(info.find_all("span"))[0].get_text().strip()
  time = list(info.find_all("span"))[1].get_text().strip()
  opponent = list(info.find_all("span"))[2].get_text().strip()

  print("{:>20}".format(home), "{:6}".format(time), "{:20}".format(opponent), sep="  ")
      
def printFinishedGame(info):

  home = list(info.find_all("span"))[0].get_text().strip()
  home_score = list(info.find_all("span"))[1].get_text().strip()
  opponent_score = list(info.find_all("span"))[2].get_text().strip()
  opponent = list(info.find_all("span"))[3].get_text().strip()

  print("{:>20}".format(home), "{:>2}".format(home_score), ":", "{:3}".format(opponent_score), "{:20}".format(opponent), sep=" ")


def printLiveGame(info):

  live = list(info.find_all("span"))[0].get_text().strip()
  home = list(info.find_all("span"))[1].get_text().strip()
  home_score = list(info.find_all("span"))[2].get_text().strip()
  opponent_score = list(info.find_all("span"))[3].get_text().strip()
  opponent = list(info.find_all("span"))[4].get_text().strip()

  print("{:>20}".format(home), "{:>2}".format(home_score), ":", "{:3}".format(opponent_score), "{:20}".format(opponent), live, sep=" ")


def main():

  if len(sys.argv) > 1:  
    value_requested = int(sys.argv[1])

    if value_requested > 0 and value_requested < 35:
      journey(sys.argv[1])
    else:
      print("The journey that you requested does not exist, there are only 34 journeys")  
  else:
    journey(-1)
    

if __name__ == "__main__":
    main()