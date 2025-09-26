class Decoder:
    def __init__(self, master: object, isa: dict):
        # self.master = master
        self.isa = isa

        self.db = None

    def fetch(self, instruction: int):
        current_instruction = instruction
        self.decode_execute(current_instruction)

    def decode_execute(self, current_instruction: int):
        opcode = (current_instruction >> 6) & 0b11

        if opcode == 0b00:  # HLT
            self.isa["hlt"]["callback"]()

        elif opcode == 0b01:  # LDI
            dest = (current_instruction >> 4) & 0b11  # 2 bits
            val = current_instruction & 0b1111  # 4 bits
            print(f":: decode - ldi   dest:&{dest}   val:#{val}")
            self.isa["ldi"]["callback"](dest, val)

        elif opcode == 0b10:  # ADD
            dest = (current_instruction >> 4) & 0b11  # 2 bits
            read_a = (current_instruction >> 2) & 0b11  # 2 bits
            read_b = current_instruction & 0b11  # 2 bits
            print(
                f":: decode - add "
                f"dest:&{dest} "
                f"read_a:&{read_a} "
                f"read_b:&{read_b}"
            )
            self.isa["add"]["callback"](dest, read_a, read_b)

        elif opcode == 0b11:  # JMP
            dest = (current_instruction >> 3) & 0b111  # 3 bits
            print(f":: decode - jmp   dest:&{dest}")
            self.isa["jmp"]["callback"](dest)


# byte long instructions -> 00 00 00 00
#
# HLT
# 00		-		-		-
#
# LDI		DEST		VAL
# 01		00		0000		-
#
# ADD		DEST		READ		READ
# 10		00		00		00
#
# JMP		DEST
# 11		000		-		-
