import frame.rootManager as rootManager
import map.mapManager as mapManager
import image.imageManager as imageManager
import robot.robotManager as robotManager

if __name__ == "__main__":
    imageManager.loadImages()
    mapManager.loadMapNames()
    robotManager.loadRobotsNames()


    rootManager.initRoot()
