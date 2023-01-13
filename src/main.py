import frame.rootManager as rootManager
import map.mapManager as mapManager
import image.imageManager as imageManager
import robot.robotManager as robotManager
import param.paramManager as paramManager
import utils.instructionUtils as instructionUtils

if __name__ == "__main__":
    instructionUtils.loadInstructions()
    imageManager.loadImages()
    mapManager.loadMapNames()
    robotManager.loadRobotsNames()
    paramManager.loadParam()

    rootManager.initRoot()

    # Save changes from parameters
    paramManager.saveParam()
