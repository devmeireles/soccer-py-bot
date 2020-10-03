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
    def most_frequent(List): 
        return max(set(List), key = List.count)

    
    @staticmethod
    def get_nationality(country):
        df = pd.read_csv('https://raw.githubusercontent.com/Dinuks/country-nationality-list/master/countries.csv')

        if country == 'England':
            return 'English'
        else:
            nationality = df.loc[df['en_short_name'] == country]
            nationality = nationality['nationality'].values

            split_nationality = nationality[0].split(',')

            if len(split_nationality) > 0:
                return split_nationality[0]
            else:
                return nationality

    @staticmethod
    def get_club_stats(stats, club):
        df = pd.DataFrame.from_dict(stats)

        club_stats = df.query(f"club == @club")

        club_stats["apps"]= club_stats["apps"].replace('-', 0)
        club_stats["goals"]= club_stats["goals"].replace('-', 0)
        club_stats["assists"]= club_stats["assists"].replace('-', 0)
        club_stats["squad"]= club_stats["squad"].replace('-', 0)


        club_stats['apps'] = club_stats['apps'].apply(int)
        club_stats['goals'] = club_stats['goals'].apply(int)
        club_stats['assists'] = club_stats['assists'].apply(int)
        club_stats['squad'] = club_stats['squad'].apply(int)

        club_stats = club_stats.sum()
        
        return club_stats['apps'], club_stats['goals'], club_stats['assists']

    @staticmethod
    def write_bio(stats, bio, ribbon):
        nationality = Text.get_nationality(bio['current_international'])

        youth_clubs = ['FC Barcelona B', 'AFC Ajax Sub-19']

        youth = False
        for club in stats:
            if 'U17' in club['club'] or 'U17' in club['club'] or club['club'] in youth_clubs or 'U19' in club['club']:
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

    @staticmethod
    def write_stats(stats, bio, ribbon):
        nationality = Text.get_nationality(bio['current_international'])

        clubs = []
        for club in stats:
            clubs.append(club['club'])

        frequent_club = Text.most_frequent(clubs)

        apps, goals, assists = Text.get_club_stats(stats, frequent_club)


        text = f"Playing for the {frequent_club}, the {bio['position']} scored {goals} goals and {assists} assists in {apps} matches"

        return text

    @staticmethod
    def write_national_stats(bio):
        nationality = Text.get_nationality(bio['current_international'])

        goals = 'goals' if int(bio['national_goals']) > 1 else 'goal'


        if bio['national_goals'] == '0':
            text = f"{bio['name']} played {bio['national_apps']} games and still scored no goals for the {nationality} national team"
        else:
            text = f"{bio['name']} played {bio['national_apps']} games and scored {bio['national_goals']} {goals} for the {nationality} national team"

        return text
