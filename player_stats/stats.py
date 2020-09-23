from .files import Files
import requests
from bs4 import BeautifulSoup as bs
import re


class Stats(object):

    def __init__(self, photo, profile, text, filter, club, folder):
        self.photo = photo
        self.profile = profile
        self.text = text
        self.filter = filter
        self.club = club
        self.folder = folder

    @staticmethod
    def get_player_data(url, filter):
        headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36"}

        html = requests.get(url, headers=headers)
        soup = bs(html.content, features="html.parser")

        player = soup.select(
            '.dataMain > .dataTop > .dataName > h1 > b')[0].text

        if filter:
            table = soup.select(
                '.responsive-table > .grid-view > .items > tbody')[0]
            leagues = table.find_all('tr')

            for league in leagues:
                if league.td.img['title'] == filter:
                    apps = 0 if league.find_all(
                        'td')[2].text == '-' else league.find_all('td')[2].text
                    goals = 0 if league.find_all(
                        'td')[3].text == '-' else league.find_all('td')[3].text
                    assists = 0 if league.find_all(
                        'td')[4].text == '-' else league.find_all('td')[4].text
        else:
            tfoot = soup.select(
                '.responsive-table > .grid-view > .items > tfoot')[0]
            values = tfoot.find_all(
                True, {"class": re.compile("^(zentriert)$")})

            apps = values[0].text
            goals = values[1].text
            assists = values[2].text

        return {
            'apps': apps, 'goals': goals, 'assists': assists, 'player': player
        }
