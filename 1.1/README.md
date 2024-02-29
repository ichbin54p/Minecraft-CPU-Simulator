# 54p's Minecraft CPU simulator BETA

## How do I make an ISA?

```json
[
    {
        "id": "The name of your instruction",
        "operands": [
            "operand name"
        ],
        "execute": [
            "execute ID"
        ]
    }
]
```

## How do I run programs?

```json
[
    {
        "id": "The name of an instruction in your ISA",
        "operands": {
            "operand name": "operand value"
        }
    }
]
```

## How do I make a settings file?

```json
{
    "speed": integer (speed which your program will execute),
    "output": {
        "logs": "filename for logging, example: logs.txt"
    },
    "display": {
        "hide": boolean (hide the display when simulating your program) NOTE: if you do not hide the display, you will not be able to view data like register values, etc,
        "ports": {
            "x": integer (which port register to use for the X axis when plotting pixels),
            "y": integer (which port register to use for the Y axis when plotting pixels)
        }
    }
}
```

## Execute ID's

- ### load-immedate
    Replace reg acc with the immediate value (`v`)
    operands: `v`
- ### register-store
    Replace a register (`r`) with reg acc's value
    operands: `r`
- ## register-load
    Replace reg acc with a register's (`r`) value
    operands: `r`
- ## jump
    Jump to an instruction (`v`)
    operands: `v`
- ## branch
    Jump to an instruction (`v`) if a condition is true (flag `f`)
    operands: `f`, `v`
- ## port-store
    Replace a port (`p`) with reg acc's value
    operands: `p`
- ## port-load
    Replace reg acc with a port's (`p`) value
    operands: `p`
- ## update-flags
    Update the flags based of the last time the ALU was used
- ## increment
    Increment a register (`r`)
- ## add
    Math: register (`a`) + register (`b`) save into reg acc
    operands: `a`, `b`
- ## xor
    Math: register (`a`) xor register (`b`) save into reg acc
    operands: `a`, `b`
- ## display-write
    Update the displays ram
    operands: `none`
- ## display-update
    Update the dispalys pixels based on it's ram
    operands: `none`
- ## display-clear
    Clear the display ram. **NOTE**: you still have to execute display-update to clear the pixels