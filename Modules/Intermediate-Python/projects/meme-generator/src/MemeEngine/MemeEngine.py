"""Create memes by drawing quote text onto images."""


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
        pass
