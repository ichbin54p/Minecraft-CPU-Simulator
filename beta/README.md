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

- ### immedate
    description: replace reg acc with the immediate value (`v`)
    operands: `v`
- ### register-store
    description: replace a register (`r`) with reg acc's value
    operands: `r`
- ### register-load
    description: replace reg acc with a register's (`r`) value
    operands: `r`
