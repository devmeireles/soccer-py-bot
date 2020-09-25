from .files import Files
import requests
from bs4 import BeautifulSoup as bs
import pandas as pd
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

    @staticmethod
    def get_all_season(url):

        headers = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36"}

        html = requests.get(url, headers=headers)
        soup = bs(html.content, features="html.parser")

        soup = soup.select('.responsive-table > .grid-view > .items > tbody')[0]
        stats = []
        try:
            for cells in soup.find_all(True, {"class": re.compile("^(even|odd)$")}):
                season = cells.find_all('td')[0].text
                league = cells.find_all('td')[1].img['title']
                club = cells.find_all('td')[3].img['alt']
                squad = cells.find_all('td')[4].text
                apps = cells.find_all('td')[5].a.text
                goals = cells.find_all('td')[7].text
                assists = cells.find_all('td')[7].text

                stats_item = {
                    'season': season,
                    'league': league,
                    'club': club,
                    'squad': squad,
                    'apps': apps,
                    'goals': goals,
                    'assists': assists,
                }

                stats.append(stats_item)
        except IndexError:
            pass

        return stats

        # read data from URL with header
        # table = pd.read_html(requests.get(
        #     url, headers={'User-agent': 'Mozilla/5.0'}).text, attrs={"class": "items"})[0]

        # # drop columns
        # table = table.drop(table.columns[[1, 3, 4, 6]], axis=1)

        # # rename columns
        # table = table.rename(columns={
        #     table.columns[0]: "season",
        #     table.columns[1]: "competition",
        #     table.columns[2]: "apps",
        #     table.columns[3]: "goals",
        #     table.columns[4]: "assists",
        #     table.columns[5]: "own_goals",
        #     table.columns[6]: "substituted_on",
        #     table.columns[7]: "substituted_off",
        #     table.columns[8]: "yellow_card",
        #     table.columns[9]: "second_yellow",
        #     table.columns[10]: "red_card",
        #     table.columns[11]: "penalty_goal",
        #     table.columns[12]: "minutes_per_goal",
        #     table.columns[13]: "minutes_played",
        # })

        # print(table)
