import requests
from bs4 import BeautifulSoup

def print_line(position, team, games, wins, draws, losts, scored_goals, conceded_goals, points):
  print("{:^6}".format(position), "{:^20}".format(team), "{:^4}".format(games),  "{:^4}".format(wins),  "{:^4}".format(draws),  "{:^4}".format(losts),  "{:^4}".format(scored_goals),  "{:^4}".format(conceded_goals),  "{:^4}".format(points))

def obtain_team_info(team_info):
  position = list(team_info.find_all("td"))[1].get_text().strip()
  team = list(team_info.find("td", class_="team").children)[1].get_text().strip()
  number_of_games = list(team_info.find_all("td"))[4].get_text().strip()
  number_of_wins = list(team_info.find_all("td"))[5].get_text().strip()
  number_of_draws = list(team_info.find_all("td"))[6].get_text().strip()
  number_of_losts = list(team_info.find_all("td"))[7].get_text().strip()
  number_of_scored_goals = list(team_info.find_all("td"))[8].get_text().strip()
  number_of_scored_conceded = list(team_info.find_all("td"))[9].get_text().strip()
  points = list(team_info.find_all("td"))[10].get_text().strip()
  
  print_line(position, team, number_of_games, number_of_wins, number_of_draws, number_of_losts, number_of_scored_goals, number_of_scored_conceded, points)

def classification(): 
  myResults_file = requests.get("http://www.maisfutebol.iol.pt/resultadoseclassificacoes/128/Portugal/Primeira-Liga")

  soup = BeautifulSoup(myResults_file.content, "html.parser")

  table = soup.find("table", class_="tableJogosClass")
  tr_tag = list(table.find_all("tr"))

  size_of_array = len(tr_tag)

  # to elimnate two arrows that are not necessary
  tr_tag = tr_tag[0:size_of_array-2]

  # print header
  print("{:^6}".format("Pos"), "{:^20}".format("Equipa"), "{:^4}".format("J"),  "{:^4}".format("V"),  "{:^4}".format("E"),  "{:^4}".format("D"),  "{:^4}".format("GM"),  "{:^4}".format("GS"),  "{:^4}".format("Pts"))
  for team_info in tr_tag:
    # Because i only want the basic information
    if "moreInfoJogos" in team_info.get("class"):
      continue

    obtain_team_info(team_info)


classification()  
