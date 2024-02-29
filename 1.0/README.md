# 54p's Minecraft CPU simulator BETA

## How do I make an ISA?

``` 
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

```
[
    {
        "id": "The name of an instruction in your ISA",
        "operands": {
            "operand name": "operand value"
        }
    }
]
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
- ## port-store
    Replace a port (`p`) with reg acc's value
    operands: `p`
- ## port-load
    Replace reg acc with a port's (`p`) value
    operands: `p`
- ## add
    Math: register (`a`) + register (`b`) save into reg acc
    operands: `a`, `b`