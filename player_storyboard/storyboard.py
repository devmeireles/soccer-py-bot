from classes.images import Images
from classes.files import Files
from classes.stats import Stats
from classes.stats import Data
from classes.text import Text
from PIL import Image, ImageFont, ImageDraw
import textwrap


class Storyboard(object):
    @staticmethod
    def save(data, profile):
        stats, bio, ribbon = Stats.get_all_season(profile)
        for i in range(len(data)):
            sheet = Storyboard.draw_sheet(data[i], i, stats, bio, ribbon)
            sheet.show()

    @staticmethod
    def draw_sheet(data, sheet_n, stats, bio, ribbon):
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

        if sheet_n == 0:
            bio_text = Text.write_bio(stats, bio, ribbon)

            lines = textwrap.wrap(bio_text, 50)

            medium_font = ImageFont.truetype('./src/fonts/Lato-Bold.ttf', 30)
            img_width, img_height = sheet.size
            y_text = 475

            for line in lines:
                draw = ImageDraw.Draw(sheet)
                width, height = medium_font.getsize(line)
                # draw.text(((img_width - width) / 2, y_text), line, font=medium_font, fill="black")
                print(y_text)
                draw.text((50, y_text), line, font=medium_font, fill="#222222")
                y_text += height

            # draw = ImageDraw.Draw(sheet)
            # title_width, title_height = draw.textsize(bio_text, font=medium_font)
            # draw.text(((width-title_width)/2, ((height-title_height)/2) +
            #         200), bio_text, font=medium_font, fill="black")

        return sheet
