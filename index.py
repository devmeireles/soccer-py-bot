from player_stats.images import Images
from player_stats.data import Data

players = [
    {
        'photo': 'https://assets-es.imgfoot.com/media/cache/1200x1200/luis-suarez-barca-2020.jpg',
        'profile': 'https://www.transfermarkt.com/luis-suarez/leistungsdaten/spieler/44352/plus/0?saison=2019',
        'text': '2019/2020 Season',
        'filter': '',
        'club': ['https://tmssl.akamaized.net/images/wappen/head/131.png?lm=1406739548']
    },
    {
        'photo': 'https://cdn.vox-cdn.com/thumbor/YpWCMoXRf2ZGCwNvwqkFDEnYfLk=/1400x1400/filters:format(jpeg)/cdn.vox-cdn.com/uploads/chorus_asset/file/19229489/1170821923.jpg.jpg',
        'profile': 'https://www.transfermarkt.com/luis-suarez/leistungsdaten/spieler/44352/plus/0?saison=2018',
        'text': '2018/2019 Season',
        'filter': '',
        'club': ['https://tmssl.akamaized.net/images/wappen/head/131.png?lm=1406739548']
    },
    {
        'photo': 'https://cdn.vox-cdn.com/thumbor/2_vCa_QSaXTC07kvgGk7VTh9sYU=/1400x1400/filters:format(jpeg)/cdn.vox-cdn.com/uploads/chorus_asset/file/11518261/960625848.jpg.jpg',
        'profile': 'https://www.transfermarkt.com/luis-suarez/leistungsdaten/spieler/44352/plus/0?saison=2017',
        'text': '2017/2018 Season',
        'filter': '',
        'club': ['https://tmssl.akamaized.net/images/wappen/head/131.png?lm=1406739548']
    },
    {
        'photo': 'https://cdn.vox-cdn.com/thumbor/6U3Q-rQ1DWmdxqDj23Q-9iWZN7U=/1400x1400/filters:format(jpeg)/cdn.vox-cdn.com/uploads/chorus_asset/file/9633957/844990382.jpg',
        'profile': 'https://www.transfermarkt.com/luis-suarez/leistungsdaten/spieler/44352/plus/0?saison=2016',
        'text': '2016/2017 Season',
        'filter': '',
        'club': ['https://tmssl.akamaized.net/images/wappen/head/131.png?lm=1406739548']
    },
    {
        'photo': 'https://cdn.vox-cdn.com/thumbor/OM-TsssWd6aIrWmzI41_dXGppMI=/0x0:4100x2733/1400x1400/filters:focal(0x0:4100x2733):format(jpeg)/cdn.vox-cdn.com/uploads/chorus_image/image/50309505/GettyImages-585714660.0.jpg',
        'profile': 'https://www.transfermarkt.com/luis-suarez/leistungsdaten/spieler/44352/plus/0?saison=2015',
        'text': '2015/2016 Season',
        'filter': '',
        'club': ['https://tmssl.akamaized.net/images/wappen/head/131.png?lm=1406739548']
    },
    {
        'photo': 'https://p2.trrsf.com/image/fget/cf/1200/1200/filters:quality(85)/images.terra.com/2014/09/24/esportes-fut-suarez-gols.JPG',
        'profile': 'https://www.transfermarkt.com/luis-suarez/leistungsdaten/spieler/44352/plus/0?saison=2014',
        'text': '2014/2015 Season',
        'filter': '',
        'club': ['https://tmssl.akamaized.net/images/wappen/head/131.png?lm=1406739548']
    },
    {
        'photo': 'https://img.bleacherreport.net/img/images/photos/002/696/777/hi-res-459715843-luis-suarez-of-liverpool-looks-on-during-the-barclays_crop_exact.jpg?w=1200&h=1200&q=50',
        'profile': 'https://www.transfermarkt.com/luis-suarez/leistungsdaten/spieler/44352/plus/0?saison=2013',
        'text': '2013/2014 Season',
        'filter': 'Premier League',
        'club': ['https://tmssl.akamaized.net/images/wappen/head/31.png?lm=1456567819']
    },
    {
        'photo': 'https://i.ibb.co/PMH7y43/output-onlinepngtools-1.png',
        'profile': 'https://www.transfermarkt.com/luis-suarez/leistungsdaten/spieler/44352/plus/0?saison=2012',
        'text': '2012/2013 Season',
        'filter': '',
        'club': ['https://tmssl.akamaized.net/images/wappen/head/31.png?lm=1456567819']
    },
    {
        'photo': 'https://img.fifa.com/image/upload/t_s2/i7fq5seejpxirebliskx.jpg',
        'profile': 'https://www.transfermarkt.com/luis-suarez/leistungsdaten/spieler/44352/plus/0?saison=2011',
        'text': '2011/2012 Season',
        'filter': '',
        'club': [
            'https://tmssl.akamaized.net/images/wappen/head/31.png?lm=1456567819',
        ]
    },
    {
        'photo': 'https://images2.minutemediacdn.com/image/upload/c_fill,w_912,h_912,f_auto,q_auto,g_auto/shape/cover/sport/liverpool-s-uruguayan-striker-luis-suare-5e5934bd12eb9af8d2000002.jpg',
        'profile': 'https://www.transfermarkt.com/luis-suarez/leistungsdaten/spieler/44352/plus/0?saison=2010',
        'text': '2010/2011 Season',
        'filter': '',
        'club': [
            'https://tmssl.akamaized.net/images/wappen/head/610.png?lm=1458894971',
            'https://tmssl.akamaized.net/images/wappen/head/31.png?lm=1456567819',
        ]
    },
    {
        'photo': 'https://img.fifa.com/image/upload/t_s2/qs5h0sf7y2v16fguvprs.jpg',
        'profile': 'https://www.transfermarkt.com/luis-suarez/leistungsdaten/spieler/44352/plus/0?saison=2009',
        'text': '2009/2010 Season',
        'filter': '',
        'club': [
            'https://tmssl.akamaized.net/images/wappen/head/610.png?lm=1458894971',
        ]
    },
    {
        'photo': 'https://i.ibb.co/7z7nFRW/1070926-1.jpg',
        'profile': 'https://www.transfermarkt.com/luis-suarez/leistungsdaten/spieler/44352/plus/0?saison=2008',
        'text': '2008/2009 Season',
        'filter': '',
        'club': [
            'https://tmssl.akamaized.net/images/wappen/head/610.png?lm=1458894971',
        ]
    },
    {
        'photo': 'https://scontent.fgru5-1.fna.fbcdn.net/v/t31.0-8/p960x960/28061734_1481766805279427_2603314061192597639_o.jpg?_nc_cat=101&_nc_sid=8024bb&_nc_ohc=u4EykcQHjUkAX-42tFQ&_nc_oc=AQmhbHMNOYpJb8wWe9WEOZ_T4u42pd3JTPffkXLZu5ocWSaZ3piaTEcVOIiho3gofxBgejvzd-Fzkfz6Rz8AZ32b&_nc_ht=scontent.fgru5-1.fna&tp=6&oh=757dd9332a4e19012cfc605bcd6abd0d&oe=5F9362DB',
        'profile': 'https://www.transfermarkt.com/luis-suarez/leistungsdaten/spieler/44352/plus/0?saison=2007',
        'text': '2007/2008 Season',
        'filter': '',
        'club': [
            'https://tmssl.akamaized.net/images/wappen/head/610.png?lm=1458894971',
        ]
    },
    {
        'photo': 'https://i.guim.co.uk/img/media/7bc21d9d3dd768c4c1504b23a22e0bfdaa2a15d9/0_177_2362_2361/master/2362.jpg?width=700&quality=85&auto=format&fit=max&s=bc2a4d473e0bb3a4c64f9617c2cd7088',
        'profile': 'https://www.transfermarkt.com/luis-suarez/leistungsdaten/spieler/44352/plus/0?saison=2006',
        'text': '2006/2007 Season',
        'filter': '',
        'club': [
            'https://tmssl.akamaized.net/images/wappen/head/202.png?lm=1458894971',
        ]
    },
]

for player in players:
    Data.get_data(player)
    Data.set_data(player)
    Images.save(player['photo'], player['profile'], player['text'], player['filter'], player['club'], 'new-suarez')