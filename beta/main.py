from json import loads, dump
from sys import argv
from os.path import exists
from time import sleep

registers = [0, 0, 0, 0, 0, 0, 0, 0, 0]

def execute_instruction(instruction, operand):
    match instruction:
        case "immediate":
            registers[0] = operand["v"]
        case "register-store":
            registers[operand['r']+1] = registers[0]
        case "register-load":
            registers[0] = registers[operand['r']+1]

if len(argv) < 2:
    print(f"Usage: {argv[0]} <isa> <instructions>")
else:
    if exists(argv[1]) and exists(argv[2]):
        with open(argv[2]) as f:
            for i in loads(f.read()):
                with open(argv[1]) as isa:
                    for j in loads(isa.read()):
                        if i['id'] == j['id']:
                            for c in j['execute']:
                                execute_instruction(c, i['operands'])
                print(registers)
    else:
        print(f"Unable to locate {argv[1]} or {argv[2]}")