from player_stats.playerstats import Playerstats
from classes.data import Data


players = [
    {
        'photo': 'https://p2.trrsf.com/image/fget/cf/1200/1200/filters:quality(85)/images.terra.com/2019/06/29/5ce2f95aad933.jpeg',
        'profile': 'https://www.transfermarkt.com/kylian-mbappe/leistungsdaten/spieler/342229/plus/0?saison=2019',
        'text': '2019/2020 Season',
        'filter': 'Ligue 1',
        'club': ['https://tmssl.akamaized.net/images/wappen/head/583.png?lm=1472229265']
    },
    {
        'photo': 'https://assets-fr.imgfoot.com/media/cache/1200x1200/wissam-ben-yedder-5ea2fe0d6cea3.jpg',
        'profile': 'https://www.transfermarkt.com/wissam-ben-yedder/leistungsdaten/spieler/146854/plus/0?saison=2019',
        'text': '2019/2020 Season',
        'filter': 'Ligue 1',
        'club': ['https://tmssl.akamaized.net/images/wappen/head/162.png?lm=1472229265']
    },
    {
        'photo': 'https://s3.amazonaws.com/charitycdn/cache/resizedcrop-75af4d5fd8443d70b4a3d1334d544466-800x800.jpg',
        'profile': 'https://www.transfermarkt.com.br/kylian-mbappe/leistungsdaten/spieler/342229/plus/0?saison=2018',
        'text': '2018/2019 Season',
        'filter': 'Ligue 1',
        'club': ['https://tmssl.akamaized.net/images/wappen/head/583.png?lm=1472229265']
    },
    {
        'photo': 'https://bolavip.com/__export/1586720363168/sites/bolavip/img/2020/04/12/edinson-cavani-psg-bordeaux-ligue-1-09022019_defwkc58a8t61ipd1wlkohwji_crop1586720344691.jpg_423682103.jpg',
        'profile': 'https://www.transfermarkt.com/edinson-cavani/leistungsdaten/spieler/48280/plus/0?saison=2017',
        'text': '2017/2018 Season',
        'filter': 'Ligue 1',
        'club': ['https://tmssl.akamaized.net/images/wappen/head/583.png?lm=1472229265']
    },
]

for player in players:
    Data.set_data(player)
    Playerstats.save(player['photo'], player['profile'], player['text'], player['filter'], player['club'], 'liga_1_scorers')