from robot.robotManager import ROBOT_FOLDER_PATH

def get_desc_from_name(name):
    file = open(f"{ROBOT_FOLDER_PATH}{name}/properties.rbt", "r")
    description = file.read()
    file.close()
    return description

def get_instr_from_name(name):
    file = open(f"{ROBOT_FOLDER_PATH}{name}/instructions.rbt")
    string_instr = file.read()
    L_inst = []
    cpt = 0
    inst = ""
    len_instr = len(string_instr)
    i = 0
    while i < len_instr:
        if string_instr[i] == ';':
            while string_instr[i] != '\n':
                i += 1
            i += 1
        if string_instr[i] == '\n':
            cpt = 0
            L_inst.append(inst)
            inst = ""
            i += 1

        elif string_instr[i] == ';':
            i += 1

        else:
            inst += string_instr[i]
            cpt += 1
            i += 1

    return L_inst

if __name__ == "__main__":

    s = get_desc_from_name("Hellboy") #OK
    L = get_instr_from_name("Hellboy") #KO
    print(s)
    print(L)
