import re
import pandas as pd
from itertools import groupby

class Text(object):

    @staticmethod
    def format_text(text):
        regex = re.compile(r'[\n\r\t]')
        text = regex.sub('', text)

        return " ".join(text.split())

    
    @staticmethod
    def get_nationality(country):
        df = pd.read_csv('https://raw.githubusercontent.com/Dinuks/country-nationality-list/master/countries.csv')

        if country == 'England':
            return 'English'
        else:
            nationality = df.loc[df['en_short_name'] == country]
            nationality = nationality['nationality'].values

            return nationality[0]

    @staticmethod
    def write_bio(stats, bio, ribbon):
        print(bio)
        nationality = Text.get_nationality(bio['current_international'])

        youth_clubs = ['FC Barcelona B']

        youth = False
        for club in stats:
            # print(f"{club['club']}")
            if 'U17' in club['club'] or 'U17' in club['club'] or club['club'] in youth_clubs:
                youth = True

        clubs = []
        for club in stats:
            clubs.append(club['club'])

        former_club = stats[-1]['club']

        text = f"{bio['name']} is a {nationality} {bio['position']} "

        if youth:
            text += f"who started his football career with {former_club} base teams. "

        if ribbon:
            split_ribbon = ribbon.split(';')
            joined_from = split_ribbon[0]
            fee = split_ribbon[2].split(':')
            fee = fee[1]
            new_club = stats[0]['club']

            split_contract = bio['contract'].split('.')
            if len(split_contract[2]) > 0:
                contract_years = int(int(split_contract[2]) - 2020)

            if len(fee) > 0 and contract_years:
                text += f"Recently the {nationality} signed a {contract_years}-years contract with {new_club} who disbursed{fee}"
            elif len(fee) < 1:
                text += f"Recently the {nationality} signed a contract with {new_club} until {bio['contract']}"

        return text
