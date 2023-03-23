from bs4 import BeautifulSoup
import requests
import numpy as np
import pandas as pd

url_maccabi = "https://www.maccabi.co.il/season.asp"
html = requests.get(url_maccabi).content
soup = BeautifulSoup(html, "html.parser", from_encoding="iso-8859-8")
games = soup.find_all("div", {"class": "line he"})

def parser(game: BeautifulSoup):
    game_data = game.find("div", {"class": "gameDate"}).text.split()
    convert_mounts = {"ינואר": '01', "פברואר": '02', "מרץ": '03', "אפריל": '04', "מאי": '05', "יוני": '06', "יולי": '07', "אוגוסט": '08', "ספטמבר": '09', "אוקטובר": '10', "נובמבר": '11', "דצמבר": '12'}
    complementary_zero = '0' if len(game_data[0]) == 1 else ''
    date_game = complementary_zero + game_data[0] + '/' + convert_mounts[game_data[1][1:]] + '/2023'
    day_game = game_data[2]
    time_game = game_data[3] if len(game_data) == 6 else np.nan
    cycle = game_data[-1]
    league = game.find("div", {"class": "leagueIcon"}).img.attrs['alt']
    home = game.find("div", {"class": "transportation"})
    home = home.img.attrs['alt'] if home.img else np.nan
    return {
        'day game': day_game,
        'cycle': cycle,
        'league': league,
        'date game': date_game,
        'time game': time_game,
        'hospitality': home,
    }

games_parsed = [parser(game) for game in games]
games_parsed_df = pd.DataFrame(games_parsed)
print(games_parsed_df)
