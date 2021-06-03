"""Using Pillow to crop an image, add a text and save it."""

import os
from time import time
from PIL import Image, ImageDraw, ImageFont
from random import randint


class MemeGenerator:
    """Change an image and save it."""

    def __init__(self, output_dir):
        """Initialize the class state."""
        self.output_dir = output_dir
        if not os.path.exists(self.output_dir):
            os.makedirs(self.output_dir)

    def make_meme(self, img_path, text, author, width=500) -> str:
        """Creating a meme."""
        # load an image
        input_image = Image.open(img_path)
        #print(f'input_image.size[0] = {input_image.size[0]}')
        #print(f'input_image.size[1] = {input_image.size[1]}')
        
        # transform the image parameters
        transform_width = min(width, 500)
        transform_ratio = transform_width / float(input_image.size[0])
        transform_height = int(transform_ratio * float(input_image.size[1]))
        
        #print(f'transform_width = {transform_width}')
        #print(f'transform_height = {transform_height}')
        
        # resize an input image
        resized_image = input_image.resize(
            (transform_width, transform_height), Image.NEAREST
        )

        # add a text to the resized image
        text_length = len(text) + len(author)
        text_body = f'{text} - {author}'
        #print(f'text = {text_body}')
        
        draw_image = ImageDraw.Draw(resized_image)
        
        font_image = ImageFont.truetype('./fonts/impact.ttf',
                                        size=24)
        
        text_coordinates = (randint(0, text_length), randint(0, text_length))
        #print(f'text_coordinates = {text_coordinates}')
        
        draw_image.text(
            text_coordinates,
            text_body,
            font=font_image,
            fill='white'
        )

        # write the image with the text do a disk
        out_path = os.path.join(self.output_dir,
                                f'image was created at {time()}.png')

        resized_image.save(out_path)

        return out_path
