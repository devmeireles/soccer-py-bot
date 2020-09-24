import re
from .files import Files

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
                player['name'], player['id'], player['season'] = Data.read_profile(data['profile'])

            if key == 'club':
                player['club_id'] = Data.read_club_crest(data['club'])

            if key == 'photo':
                player['photo'] = data['photo']

        return player
    
    @staticmethod
    def read_profile(url):
        split_url = url.split('/')
        saison = split_url[-1].split('=')

        return (split_url[3] , split_url[6], saison[1])

    @staticmethod
    def read_club_crest(urls):
        ids = []
        for url in urls:
            split_url = url.split('/')
            split_url = split_url[6].split('.')
            ids.append(split_url[0])

            
        return (ids)