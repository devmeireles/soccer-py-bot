from classes.images import Images
from classes.files import Files
from classes.stats import Stats
from classes.stats import Data
from classes.text import Text
from PIL import Image, ImageFont, ImageDraw
import textwrap


class Storyboard(object):
    @staticmethod
    def save(data, profile, folder):
        stats, bio, ribbon = Stats.get_all_season(profile)
        for i in range(len(data)):
            sheet = Storyboard.draw_sheet(data[i], i, stats, bio, ribbon)
            file_name=Files.get_file_name(bio['name'], str(i))
            Files.save(sheet, folder, file_name)

    @staticmethod
    def draw_sheet(data, sheet_n, stats, bio, ribbon):
        sheet = Image.new('RGB', (800, 800), color=data['bg_color_2'])
        draw = ImageDraw.Draw(sheet)
        draw.rectangle((0, 700, 800, 0), fill=data['bg_color_1'])
        draw.rectangle((10, 790, 790, 10), fill='#FFF')

        thumb_size = 800, 800

        player_image = Files.open_url(data['photo'])
        player_image = player_image.convert('RGBA')
        player_image.thumbnail(thumb_size, Image.ANTIALIAS)

        player_image_w, player_image_h = player_image.size

        sheet = Images.apply_image(
            sheet, player_image, (0, 0), (player_image.size))

         # Apply the Data Science logo
        logo = Files.open_local('./src/images/logo.png')
        sheet = Images.apply_image(
            sheet, logo, (10, 10), (75, 75))

        if sheet_n == 0:
            bio_text = Text.write_bio(stats, bio, ribbon)

            lines = textwrap.wrap(bio_text, 50)

            medium_font = ImageFont.truetype('./src/fonts/Lato-Bold.ttf', 30)
            img_width, img_height = sheet.size
            y_text = player_image_h + 15

            for line in lines:
                draw = ImageDraw.Draw(sheet)
                width, height = medium_font.getsize(line)
                draw.text((50, y_text), line, font=medium_font, fill="#222222")
                y_text += height


        if sheet_n == 1:
            stats_text = Text.write_stats(stats, bio, ribbon)
            lines = textwrap.wrap(stats_text, 50)

            medium_font = ImageFont.truetype('./src/fonts/Lato-Bold.ttf', 30)
            img_width, img_height = sheet.size
            y_text = player_image_h + 50

            for line in lines:
                draw = ImageDraw.Draw(sheet)
                width, height = medium_font.getsize(line)
                draw.text((50, y_text), line, font=medium_font, fill="#222222")
                y_text += height


        if sheet_n == 2:
            national_stats_text = Text.write_national_stats(bio)
            lines = textwrap.wrap(national_stats_text, 50)

            medium_font = ImageFont.truetype('./src/fonts/Lato-Bold.ttf', 30)
            img_width, img_height = sheet.size
            y_text = player_image_h + 50

            for line in lines:
                draw = ImageDraw.Draw(sheet)
                width, height = medium_font.getsize(line)
                draw.text((50, y_text), line, font=medium_font, fill="#222222")
                y_text += height
            


        return sheet
