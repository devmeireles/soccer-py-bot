from .files import Files
from .images import Images

class Stats(object):

    def __init__ (self, photo, profile, text, filter, club, folder):
        self.photo = photo
        self.profile = profile
        self.text = text
        self.filter = filter
        self.club = club
        self.folder = folder
    
    def save(self):
        #Open the image
        background_image = Files.open_url(self.photo)
        
        #Resize and crop
        background_image = Images.treat_image(background_image)

        #Set the black grandient layer
        background_image = Images.set_gradient(background_image, 'full')
        background_image = Images.set_gradient(background_image, 'footer')

        #Apply the Data Science logo
        logo = Files.open_local('./src/images/logo.png')
        background_image = Images.apply_image(background_image, logo, (10, 10), (75, 75))

        #Apply the club crest
        if self.club:
            crest = Files.open_url(self.club)
            background_image = Images.apply_image(background_image, crest, Images.get_crest_position(background_image), (125, 125))
        
        background_image.show()
