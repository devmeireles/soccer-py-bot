from classes.files import Files
from classes.text import Text
from classes.data import Data
import requests
from bs4 import BeautifulSoup as bs
import pandas as pd
import re
import sys


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

        player = soup.select(
            '.dataMain > .dataTop > .dataName > h1')[0].text

        player = f"name:{player}"

        table = soup.select('.responsive-table > .grid-view > .items > tbody')[0]
        profile = soup.select('.dataContent > .dataBottom > .dataDaten')
        ribbon = soup.select('.dataRibbon > a')

        if len(ribbon) > 0:
            ribbon = ribbon[0]['title']

        player_bio = []
        country = []
        for items in profile:
            for p in items.find_all('p'):
                for datavalue in p.find_all(True, {"class": re.compile("^(dataValue)$")}):
                    if len(datavalue.find_all('img')) > 0:
                        country.append(datavalue.find_all('img')[0]['title'])

                bio_data = Text.format_text(p.text)
                player_bio.append(bio_data)

        player_bio.append(player)
        bio = Data.get_bio(player_bio, country)
        
        stats = []
        try:
            for cells in table.find_all(True, {"class": re.compile("^(even|odd)$")}):
                season = cells.find_all('td')[0].text
                league = cells.find_all('td')[1].img['title'] if cells.find_all('td')[1].img else ''
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

        # print(stats)
        return stats, bio, ribbon
