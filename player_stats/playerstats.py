from classes.files import Files
from classes.images import Images
from classes.stats import Stats
from PIL import Image

class Playerstats(object):

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
                crest_position = Images.get_crest_position(
                    background_image, crest_item, stats['player'], crest_i, crest_len)
                background_image = Images.apply_image(
                    background_image, crest_item, crest_position, (crest_item.size))

        file_name = Files.get_file_name(stats['player'], text)
        Files.save(background_image, folder, file_name)

        # background_image.show()
