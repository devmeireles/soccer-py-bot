# from player_stats.images import Images
# from player_stats.data import Data

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
#     Data.set_data(player)
#     Images.save(player['photo'], player['profile'], player['text'], player['filter'], player['club'], 'new-suarez')


from player_storyboard.storyboard import Storyboard


data = [
    {
        'bg_color_1': '#034694',
        'bg_color_2': '#d1d3d4',
        'photo': 'https://allmysportsnews.com/wp-content/uploads/2020/09/csportfoto22_GettyImages-1228616806-820x410.jpg',
        'text': 'lorem lorem lorem lore'
    },
    {
        'bg_color_1': 'red',
        'bg_color_2': 'black',
        'photo': 'https://www.lance.com.br/files/article_main/uploads/2020/04/15/5e975e2acf24d.jpeg',
    }
]

profile = 'https://www.transfermarkt.com/kai-havertz/leistungsdatendetails/spieler/309400/saison//verein/0/liga/0/wettbewerb//pos/0/trainer_id/0/plus/1'

Storyboard.save(data, profile)