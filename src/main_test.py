from map.mine import *
from robot.robotParty import *
from map.map import *

matrixMap = []
for i in range(20):
    matrixMap.append([0] * 30)
print(len(matrixMap))
print(len(matrixMap[0]))
map = Map(matrixMap)
Robot1 = RobotParty(0,5,5,[], map)
Robot2 = RobotParty(1,8,3,[], map)
Robot3 = RobotParty(2,15,8, [], map)
for i in range(3):
    Robot1.print_position()
    Robot1.PS(map)
    Robot1.print_position()
    print("MONCUL")
    Robot2.print_position()
    Robot2.PS(map)
    Robot2.print_position()
    print("MESCOUILLES")
