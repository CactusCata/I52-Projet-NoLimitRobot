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
Robot2 = RobotParty(1,7,5,[], map)
Robot1.print_position()
Robot2.print_position()
#Robot2.MI(map)
#Robot2.MI(map)
#Robot2.MI(map)
#Robot2.MI(map)
#for m in mineingame:
#    m.print_position()
#    m.print_id()
#Robot2.print_energy()
#Robot2.print_position()
#Robot2.print_id()
Robot2.DD('H', map)
Robot2.DD('H', map)
Robot1.print_position()
Robot2.print_position()
#Robot2.print_energy()
