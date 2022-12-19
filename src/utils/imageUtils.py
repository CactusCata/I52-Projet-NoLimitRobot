from PIL import Image

def applyColor(image, color):
    """
    - image need to be a simple image, not
    tk image.
    - color is triplet (R, G, B)

    return image simple
    """
    matrixColor = Image.new('RGB', image.size, color)
    matrixAlpha = Image.new('RGBA', image.size, (0, 0, 0, 123))
    colorMatrix = Image.composite(image, matrixColor, matrixAlpha).convert('RGB')
    return colorMatrix
