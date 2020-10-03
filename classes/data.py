import re
from classes.files import Files


class Data(object):
    @staticmethod
    def set_data(data):
        item = Data.get_data(data)
        Files.save_json('./src/data/data.json', item)

    @staticmethod
    def get_data(data):
        keys = data.keys()

        player = {
            'id': '',
            'name': '',
            'season': '',
            'club_id': '',
            'photo': '',
        }

        for key in keys:
            if key == 'profile':
                player['name'], player['id'], player['season'] = Data.read_profile(
                    data['profile'])

            if key == 'club':
                player['club_id'] = Data.read_club_crest(data['club'])

            if key == 'photo':
                player['photo'] = data['photo']

        return player

    @staticmethod
    def read_profile(url):
        split_url = url.split('/')
        saison = split_url[-1].split('=')

        return (split_url[3], split_url[6], saison[1])

    @staticmethod
    def read_club_crest(urls):
        ids = []
        for url in urls:
            split_url = url.split('/')
            split_url = split_url[6].split('.')
            ids.append(split_url[0])

        return (ids)

    @staticmethod
    def format_position(position):
        if position == 'Attacking Midfield':
            return 'Attacking Midfielder'
        elif position == 'Central Midfield':
            return 'Central Midfielder'

    @staticmethod
    def get_bio(data, country):
        player = {
            'name': '',
            'position': '',
            'birth_date': '',
            'contract': '',
            'place_birth': '',
            'country_birth': '',
            'citizenship': '',
            'current_international': '',
            'national_apps': '',
            'national_goals': '',
        }

        for values in data:
            split_value = values.split(':')

            if split_value[0] == 'name':
                player['name'] = split_value[1]

            if split_value[0] == 'Position':
                player['position'] = Data.format_position(split_value[1])

            if split_value[0] == 'Date of birth/Age':
                player['birth_date'] = split_value[1]

            if split_value[0] == 'Contract expires':
                player['contract'] = split_value[1]

            if split_value[0] == 'Place of birth':
                player['place_birth'] = split_value[1]

            if split_value[0] == 'Place of birth':
                player['place_birth'] = split_value[1]

            if split_value[0] == 'Citizenship':
                player['citizenship'] = split_value[1]

            if split_value[0] == 'Current international':
                player['current_international'] = split_value[1]

            if split_value[0] == 'Former International':
                player['current_international'] = split_value[1]

            if split_value[0] == 'National player':
                player['current_international'] = split_value[1]

            if split_value[0] == 'Current iget_bionternational':
                player['current_international'] = split_value[1]

            if split_value[0] == 'Caps/Goals':
                split_national = split_value[1].split('/')
                player['national_apps'] = split_national[0]
                player['national_goals'] = split_national[1]

        if len(country[0]) > 0:
            player['country_birth'] = country[0]

        return player
