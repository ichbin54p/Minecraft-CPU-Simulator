from json import loads, dump
from sys import argv
from os.path import exists
from os import system
from time import sleep
from sys import exit

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

input("Warning, this program clears your terminal, are you sure you want to run? (CTRL + C to quit / Enter to start)")

def execute_instruction(id, operand):
    global instruction
    global alu_output
    match id:
        case "load-immediate":
            registers[0] = operand["v"]
        case "register-store":
            registers[operand['r']+1] = registers[0]
        case "register-load":
            registers[0] = registers[operand['r']+1]
        case "jump":
            instruction = operand["v"]
        case "port-store":
            ports[operand["p"]] = registers[0]
        case "port-load":
            registers[0] = ports[operand["p"]]
        case "update-flags":
            pass
        case "add":
            alu_output = registers[operand['a']+1] + registers[operand['b']+1]
            registers[0] = registers[operand['a']+1] + registers[operand['b']+1]

if len(argv) < 4:
    print(f"Usage: {argv[0]} <isa> <instructions> <enable display?> <execute speed>")
else:
    try:
        speed = 1/float(argv[4])/10
    except:
        print("Use base 10 for arguemnt value 4")
        exit()
    if exists(argv[1]) and exists(argv[2]):
        with open(argv[2]) as f:
            instructions = loads(f.read())
            while(instruction < len(instructions)):
                system("clear")
                print(f"Instruction {instruction}/{len(instructions)-1} ", end="")
                for rr in range(9):
                    if registers[rr] > 255:
                        registers[rr] = 0
                with open(argv[1]) as isa:
                    for j in loads(isa.read()):
                        if instructions[instruction]['id'] == j['id']:
                            cindex = 0
                            for c in j['execute']:
                                if cindex < 1:
                                    print(f"({instructions[instruction]['operands']}) ({c})", end="")
                                else:
                                    print(f" ({c})", end="")
                                execute_instruction(c, instructions[instruction]['operands'])
                                cindex += 1
                print("\n")
                if argv[3].lower() == "false":
                    print("Register values:\tPort values\tFlag values:")
                    for i in range(9):
                        print(f"\n{i}: {registers[i]}", end="")
                        if i < 8:
                            print(f"\t\t\t{i}: {ports[i]}", end="")                        
                        if i < 2:
                            print(f"\t\t{i}: {flags[i]}", end="")
                elif argv[3].lower() == "true":
                    print("Displays will be introduced in update 1.1")
                    exit()
                else:
                    print("Arguement value 3 needs to be a boolean")
                    exit()
                instruction += 1
                sleep(speed)
    else:
        print(f"Unable to locate {argv[1]} or {argv[2]}")