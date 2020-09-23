# from player_stats.player import Player
from player_stats.handlers.stats import Stats

# polly = Player("Gabriel", "Meireles")

# print(polly.get_player_data())

players = [
    {
        'photo': 'https://media.bleacherreport.com/f_auto,w_800,h_800,q_auto,c_fill/br-img-images/003/639/593/hi-res-fd8369d335bdceb402b4ecf7c08d778c_crop_north.jpg',
        'profile': 'https://www.transfermarkt.com/carlos-tevez/leistungsdaten/spieler/4276/plus/0?saison=2010',
        'text': '2010/2011 Season',
        'filter': 'Premier League',
        'club': 'https://www.logolynx.com/images/logolynx/s_02/0273fa5940eab11efd0e3f3eb3f1fe13.png'
    }
]

for player in players:
    stats = Stats(player['photo'], player['profile'], player['text'], player['filter'], player['club'], 'testing')
    print(stats.save())