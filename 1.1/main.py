from json import loads
from sys import argv
from os.path import exists
from os import system, remove
from time import sleep
from sys import exit
from platform import system as operating_system

speed = 0
alu_output = 0
instruction = 0
flags = [0, 0]
ports = [0, 0, 0, 0, 0, 0, 0, 0]
registers = [0, 0, 0, 0, 0, 0, 0, 0, 0]
display = [
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0]
]
update_display = False

def execute_instruction(id, operand, dp, logsdir):
    global instruction
    global alu_output
    global flags
    global update_display
    global display
    if not exists(logsdir):
        logs = ""
    else:
        with open(logsdir, "r") as f:
            logs = f.read()
    match id:
        case "load-immediate":
            logs += f"\n\n loaded an immediate with the value of {operand['v']}"
            registers[0] = operand["v"]
        case "register-store":
            logs += f"\n\nloaded value {registers[0]} into register {operand['r']+1} which had the value of {registers[operand['r']+1]}"
            registers[operand['r']+1] = registers[0]
        case "register-load":
            logs += f"\n\nloaded value {registers[operand['r']+1]} which was from register {operand['r']+1} into reg acc"
            registers[0] = registers[operand['r']+1]
        case "jump":
            logs += f"\n\njumped to instruction {operand['v']}"
            instruction = operand["v"]
        case "port-store":
            logs += f"\n\nstored value {registers[0]} which was from reg acc into port {operand['p']} which had the value {ports[operand['p']]}"
            ports[operand["p"]] = registers[0]
        case "port-load":
            logs += f"\n\nloaded value {ports[operand['p']]} from port {operand['p']} into reg acc which had the value of {registers[0]}"
            registers[0] = ports[operand["p"]]
        case "update-flags":
            logs += f"\n\nupdated flags"
            if alu_output == 0:
                flags[0] = 1
            else:
                flags[0] = 0
            if alu_output > 255:
                flags[1] = 1
            else:
                flags[1] = 0
        case "add":
            logs += f"\n\nadded {registers[operand['a']+1]} which was from reg {operand['a']+1} with {registers[operand['b']+1]} which was from reg {operand['b']+1}"
            alu_output = registers[operand['a']+1] + registers[operand['b']+1]
            registers[0] = registers[operand['a']+1] + registers[operand['b']+1]
        case "display-write":
            logs += f"\n\nwrote to the display"
            display[ports[dp['y']]][ports[dp['x']]] = 1
        case "display-update":
            logs += f"\n\nupdated the display"
            update_display = True
        case "display-clear":
            logs += f"\n\ncleared the display"
            display = [
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0]
            ]
        case "xor":
            logs += f"\n\nxor'd {registers[operand['a']+1]} which was from reg {operand['a']+1} with {registers[operand['b']+1]} which was from reg {operand['b']+1}"
            alu_output = registers[operand['a']+1] ^ registers[operand['b']+1]
            registers[0] = registers[operand['a']+1] ^ registers[operand['b']+1]
        case "branch":
            logs += f"\n\ntrying to branch to instruction {operand['v']}. checking flag {operand['f']}"
            if flags[operand['f']] == 0:
                logs += f"\tsuccessfully branched"
                instruction = operand['v']
        case "increment":
            logs += f"\n\nincrementing register {operand['r']+1} which has the value of {registers[operand['r']+1]} --> {registers[operand['r']+1]+1}"
            registers[0] = registers[operand['r']+1]+1
    with open(logsdir, "w") as f:
        f.write(logs)
if len(argv) < 3:
    print(f"Usage: {argv[0]} <isa> <instructions> <settings>")
else:
    if exists(argv[1]) and exists(argv[2]) and exists(argv[3]):
        with open (argv[3]) as s:
            settings = loads(s.read())
            if exists(settings['output']['logs']):
                remove(settings['output']['logs'])
            try:
                speed = 1/float(settings['speed'])/10
            except:
                print("Use float for speed in settings file")
                exit()
            with open(argv[2]) as f:
                instructions = loads(f.read())
                while(instruction < len(instructions)):
                    if settings['display']['hide'] == True:
                        if operating_system().lower() == "linux":
                            system("clear")
                        else:
                            system("cls")
                    if settings['display']['hide'] == True:
                        print(f"Instruction {instruction}/{len(instructions)-1} ", end="")
                    for rr in range(9):
                        if registers[rr] > 255:
                            registers[rr] = 0
                    with open(argv[1]) as isa:
                        for j in loads(isa.read()):
                            if instructions[instruction]['id'] == j['id']:
                                cindex = 0
                                for c in j['execute']:
                                    if settings['display']['hide'] == True:
                                        if cindex < 1:
                                            print(f"({instructions[instruction]['operands']}) ({c})", end="")
                                        else:
                                            print(f" ({c})", end="")
                                    execute_instruction(c, instructions[instruction]['operands'], settings['display']['ports'], settings['output']['logs'])
                                    cindex += 1
                    print("\n")
                    if update_display:
                        if operating_system().lower() == "linux":
                            system("clear")
                        else:
                            system("cls")
                    if settings['display']['hide'] == True:
                        print("Register values:\tPort values\tFlag values:")
                        for i in range(9):
                            print(f"\n{i}: {registers[i]}", end="")
                            if i < 8:
                                print(f"\t\t\t{i}: {ports[i]}", end="")                        
                            if i < 2:
                                print(f"\t\t{i}: {flags[i]}", end="")
                    elif settings['display']['hide'] == False:
                        if update_display:
                            for row in display:
                                for pixel in row:
                                    if pixel == 0:
                                        print("\033[40m\033[30m--\033[0m", end="")
                                    else:
                                        print("\033[47m\033[37m--\033[0m", end="")
                                print()
                    else:
                        print("display --> hide needs to be a boolean in settings file")
                        exit()
                    instruction += 1
                    sleep(speed)
    else:
        print(f"Unable to locate {argv[1]} or {argv[2]} or {argv[2]}")
