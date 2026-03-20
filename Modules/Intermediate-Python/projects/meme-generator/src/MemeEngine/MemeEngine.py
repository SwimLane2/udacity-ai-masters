"""Create memes by drawing quote text onto images."""

import os
import random
from PIL import Image, ImageDraw


class MemeEngine:
    """Generate meme images with quote text and author text."""

    def __init__(self, output_dir):
        """Create a MemeEngine.

        :param output_dir: Directory where generated meme images will be saved.
        """
        self.output_dir = output_dir

    def make_meme(self, img_path, text, author, width=500) -> str:
        """Create a meme image and return the saved output path.

        :param img_path: Path to the source image.
        :param text: Quote body text to draw on the image.
        :param author: Quote author to draw on the image.
        :param width: Maximum width of the output image.
        :return: Path to the generated meme image.
        """
        try:
            img = Image.open(img_path)
            if img.width > width:
                ratio = width / img.width
                new_height = int(img.height * ratio)
                img = img.resize((width, new_height))

            draw = ImageDraw.Draw(img)
            message = f'"{text}"\n- {author}'

            x = random.randint(10, max(10, img.width - 200))
            y = random.randint(10, max(10, img.height - 100))

            draw.text((x, y), message, fill='white')

            if not os.path.exists(self.output_dir):
                os.makedirs(self.output_dir)

            out_path = os.path.join(
                self.output_dir,
                f'meme_{random.randint(0, 1000000)}.jpg'
            )

            img.save(out_path)

            return out_path
        except (FileNotFoundError, OSError, ValueError) as e:
            raise ValueError(f'Error while creating meme: {e}') from e
