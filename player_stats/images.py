from PIL import Image

class Images(object):
    def __init__(self, image):
        self.image = image

    @staticmethod
    def treat_image(im):
        #Resize
        im = im.resize((800, 800))

        # Check if img isn't RGBA format and then set a RGBA mode
        if im.mode != 'RGBA':
            im = im.convert('RGBA')

        #crop the image area 600x800
        crop_area = (100, 0, 700, 800)
        im = im.crop(crop_area)

        return im

    @staticmethod
    def set_gradient(im, position='full'):

        # get the w and h from img
        width, height = im.size

        # Create a new image
        gradient = Image.new('L', (1, Images.check_height(height, position)), color=0xFF)

        # Loop through the real image height
        for x in range(Images.check_height(height, position)):
            gradient.putpixel((0, -x), int(255 * (1 - 1. * float(x)/Images.check_height(height, position))))

        #Apply the gradient to the image
        alpha = gradient.resize(im.size)
        black_im = Image.new('RGBA', (width, height), color=0) # i.e. black
        black_im.putalpha(alpha)
        gradient_im = Image.alpha_composite(im, black_im)

        return gradient_im
    
    @staticmethod
    def apply_image(im, new_img, position, size):

        #Apply the Data Science logo
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
    def get_crest_position(im):
        width, height = im.size

        return (int((width-125)/2), 525)