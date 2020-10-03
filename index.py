# from player_stats.images import Images
# from player_stats.data import Data

# from player_stats.playerstats import Playerstats

# players = [
#     {
#         'photo': 'https://assets-es.imgfoot.com/media/cache/1200x1200/luis-suarez-barca-2020.jpg',
#         'profile': 'https://www.transfermarkt.com/luis-suarez/leistungsdaten/spieler/44352/plus/0?saison=2019',
#         'text': '2019/2020 Season',
#         'filter': '',
#         'club': ['https://tmssl.akamaized.net/images/wappen/head/131.png?lm=1406739548']
#     },
# ]

# for player in players:
#     # Data.set_data(player)
#     Playerstats.save(player['photo'], player['profile'], player['text'], player['filter'], player['club'], 'new-suarez2')


from player_storyboard.storyboard import Storyboard


data = [
    {
        'bg_color_1': '#d7402c',
        'bg_color_2': '#fbf144',
        'photo': 'https://images.daznservices.com/di/library/GOAL/a8/8a/donny-van-de-beek-manchester-united-2020_tjlxhbci1wmp1atuobo9xotq0.jpg?t=-1408125100&quality=100',
    },
    {
        'bg_color_1': 'red',
        'bg_color_2': 'white',
        'photo': 'https://www.fcbarcelonanoticias.com/uploads/s1/11/65/07/6/van-de-beek-madrid.jpeg',
    },
    {
        'bg_color_1': '#ca5d25',
        'bg_color_2': '#132771',
        'photo': 'https://www.rousingthekop.com/static/uploads/4/2019/06/GettyImages-1148441987-1440x960.jpg',
    }
]

profile = 'https://www.transfermarkt.com/kai-havertz/leistungsdatendetails/spieler/288255/saison//verein/0/liga/0/wettbewerb//pos/0/trainer_id/0/plus/1'

Storyboard.save(data, profile, '288255')