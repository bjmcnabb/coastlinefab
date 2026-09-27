from PIL import ImageOps

class AutoOrient:
    def process(self, image):
        return ImageOps.exif_transpose(image)