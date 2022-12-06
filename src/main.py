import frame.rootManager as rootManager
import map.mapManager as mapManager
import image.imageManager as imageManager

if __name__ == "__main__":
    imageManager.loadImages()
    mapManager.loadMapNames()

    rootManager.initRoot()
