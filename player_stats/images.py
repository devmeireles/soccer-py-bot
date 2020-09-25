from PIL import Image, ImageFont, ImageDraw
from .files import Files
from .stats import Stats


class Images(object):
    def __init__(self, image):
        self.image = image

    @staticmethod
    def treat_image(im):
        # Resize
        im = im.resize((800, 800))

        # Check if img isn't RGBA format and then set a RGBA mode
        if im.mode != 'RGBA':
            im = im.convert('RGBA')

        # crop the image area 600x800
        crop_area = (100, 0, 700, 800)
        im = im.crop(crop_area)

        return im

    @staticmethod
    def set_gradient(im, position='full'):

        # get the w and h from img
        width, height = im.size

        # Create a new image
        gradient = Image.new(
            'L', (1, Images.check_height(height, position)), color=0xFF)

        # Loop through the real image height
        for x in range(Images.check_height(height, position)):
            gradient.putpixel(
                (0, -x), int(255 * (1 - 1. * float(x)/Images.check_height(height, position))))

        # Apply the gradient to the image
        alpha = gradient.resize(im.size)
        black_im = Image.new('RGBA', (width, height), color=0)  # i.e. black
        black_im.putalpha(alpha)
        gradient_im = Image.alpha_composite(im, black_im)

        return gradient_im

    @staticmethod
    def apply_image(im, new_img, position, size):

        # Apply the Data Science logo
        logo = new_img.resize(size)
        im.paste(logo, position, logo)

        return im

    @staticmethod
    def check_height(height, position):
        if position == 'footer':
            return int(height / 2)
        else:
            return height

    @staticmethod
    def get_crest_position(im, crest, title, crest_i, crest_len):
        width, height = im.size
        crest_width, crest_height = crest.size

        draw = ImageDraw.Draw(im)
        title_font = ImageFont.truetype('./src/fonts/Lato-Bold.ttf', 60)
        title_width, title_height = draw.textsize(title, font=title_font)

        print(int((((width-crest_width) / 2) + (crest_i*2)) ), 445)

        if crest_len == 1:
            return (int((((width-crest_width) / 2) / crest_i) ), 445)
        elif crest_len == 2:
            if crest_i == 1:
                return (int((((width-crest_width) / crest_len) - 75) ), 445)
            elif crest_i == 2:
                return (int((((width-crest_width) / 2) + 75) ), 445)
        elif crest_len == 3:
            if crest_i == 1:
                return (int((((width-crest_width) / crest_len)) - 25 ), 445)
            elif crest_i == 2:
                return (int((((width-crest_width) / 2)) ), 445)
            elif crest_i == 3:
                return (int((((width-crest_width) / 2) + (crest_width+20))), 445)

    @ staticmethod
    def set_stats(im, stats, text):

        # writing text
        title = stats['player']
        subtitle = text
        apps = stats['apps']
        goals = stats['goals']
        assists = stats['assists']
        apps_text = 'Apps'
        goals_text = 'Goals'
        assists_text = 'Assists'

        title_font = ImageFont.truetype('./src/fonts/Lato-Bold.ttf', 60)
        medium_font = ImageFont.truetype('./src/fonts/Lato-Bold.ttf', 30)
        subtitle_font = ImageFont.truetype('./src/fonts/Lato-Light.ttf', 19)

        width, height = im.size

        # Draw the title
        draw = ImageDraw.Draw(im)
        title_width, title_height = draw.textsize(title, font=title_font)
        draw.text(((width-title_width)/2, ((height-title_height)/2) +
                   200), title, font=title_font, fill="white")

        # Draw the subtitle
        subtitle_width, subtitle_height = draw.textsize(
            subtitle, font=subtitle_font)
        draw.text(((width-subtitle_width)/2, ((height-subtitle_height)/2) +
                   250), subtitle, font=subtitle_font, fill="white")

        # Apps number
        apps_width, apps_height = draw.textsize(apps, font=medium_font)
        draw.text((((width-apps_width)/2-100), ((height-apps_height)/2) +
                   300), apps, font=medium_font, fill="white")

        # Apps text
        apps_text_width, apps_text_height = draw.textsize(
            apps_text, font=subtitle_font)
        draw.text((((width-apps_text_width)/2-100), ((height-apps_text_height)/2) +
                   325), apps_text, align='center', font=subtitle_font, fill="white")

        # Goals number
        goals_width, goals_height = draw.textsize(apps, font=medium_font)
        draw.text((((width-goals_width)/2), ((height-goals_height)/2)+300),
                  goals, font=medium_font, fill="white")

        # Goals text
        goals_text_width, goals_text_height = draw.textsize(
            goals_text, font=subtitle_font)
        draw.text((((width-goals_text_width)/2), ((height-goals_text_height)/2) +
                   325), goals_text, font=subtitle_font, fill="white")

        # Assists number
        assists_width, assists_height = draw.textsize(
            assists, font=medium_font)
        draw.text((((width-assists_width)/2+100), ((height-assists_height)/2) +
                   300), assists, font=medium_font, fill="white")

        # Assists text
        assists_text_width, assists_text_height = draw.textsize(
            assists_text, font=subtitle_font)
        draw.text((((width-assists_text_width)/2+100), ((height-assists_text_height)/2) +
                   325), assists_text, font=subtitle_font, fill="white")

        return im

    @ staticmethod
    def save(photo, profile, text, filter, crest, folder):
        # Open the image
        background_image = Files.open_url(photo)

        # Resize and crop
        background_image = Images.treat_image(background_image)

        # Set the black grandient layer
        background_image = Images.set_gradient(background_image, 'full')

        background_image = Images.set_gradient(background_image, 'footer')

        # Apply the Data Science logo
        logo = Files.open_local('./src/images/logo.png')
        background_image = Images.apply_image(
            background_image, logo, (10, 10), (75, 75))

        # Stats
        if profile:
            stats = Stats.get_player_data(profile, filter)
            background_image = Images.set_stats(background_image, stats, text)

        # Apply the club crest
        if crest:
            thumb_size = 125, 125
            for i in range(len(crest)):
                crest_i = i+1
                crest_len = len(crest)
                crest_item = Files.open_url(crest[i])
                crest_item.thumbnail(thumb_size, Image.ANTIALIAS)
                crest_position = Images.get_crest_position(background_image, crest_item, stats['player'], crest_i, crest_len)
                background_image = Images.apply_image(
                    background_image, crest_item, crest_position, (crest_item.size))

        file_name=Files.get_file_name(stats['player'], text)
        Files.save(background_image, folder, file_name)

        # background_image.show()

    @staticmethod
    def draw_square(size, position, color):
        im = Image.new('RGB', size, color=color)
        return im