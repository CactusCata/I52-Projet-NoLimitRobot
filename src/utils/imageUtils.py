from PIL import Image

def applyColor(image, color):
    """
    - image need to be a simple image, not
    tk image.
    - color is triplet (R, G, B)

    return image simple
    """
    matrixColor = Image.new('RGB', image.size, color)
    matrixAlpha = Image.new('RGBA', image.size, (0, 0, 0, 150))
    colorMatrix = Image.composite(image, matrixColor, matrixAlpha).convert('RGB')
    return colorMatrix

def createTransparent(image, alphaValue):
    """
    Crée une version transparente de l'image donnée
    """
    newImage = image.copy()

    # Create a new image with an alpha channel
    alpha = Image.new('L', newImage.size, 255)

    for x in range(newImage.size[0]):
        for y in range(newImage.size[1]):
            alpha.putpixel((x, y), alphaValue)

    newImage.putalpha(alpha)
    return newImage