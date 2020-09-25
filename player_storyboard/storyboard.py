from player_stats.images import Images
from player_stats.files import Files
from player_stats.stats import Stats
from PIL import Image, ImageFont, ImageDraw


class Storyboard(object):
    @staticmethod
    def save(data, profile):
        # stats = Stats.get_all_season(profile)
        # print(stats)
        for item in data:
            sheet = Storyboard.draw_sheet(item)
            sheet.show()

    @staticmethod
    def draw_sheet(data):
        sheet = Image.new('RGB', (800, 800), color=data['bg_color_2'])
        draw = ImageDraw.Draw(sheet)
        draw.rectangle((0, 600, 800, 0), fill=data['bg_color_1'])
        draw.rectangle((20, 780, 780, 20), fill='#FFF')

        thumb_size = 761, 600

        player_image = Files.open_url(data['photo'])
        player_image = player_image.convert('RGBA')
        player_image.thumbnail(thumb_size, Image.ANTIALIAS)

        sheet = Images.apply_image(
            sheet, player_image, (20, 20), (player_image.size))

        return sheet