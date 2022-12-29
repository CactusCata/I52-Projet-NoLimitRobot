from map.mine import *
from robot.robotParty import *
from map.map import *

matrixMap = []
for i in range(20):
    matrixMap.append([0] * 30)
print(len(matrixMap))
print(len(matrixMap[0]))
matrixMap[6][8] = 1
matrixMap[6][9] = 1
matrixMap[5][9] = 1
map = Map(matrixMap)
Robot1 = RobotParty(0,5,8,[], map)
Robot2 = RobotParty(1,9,8,[], map)
for i in range(5):
    Robot1.print_position()
    Robot1.PS(map)
    Robot1.print_position()
    print("----------------------------MONCUL---------------------")
    Robot2.print_position()
    Robot2.PS(map)
    Robot2.print_position()
    print("=========================MESCOUILLES===================")
    test = ""
