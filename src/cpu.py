from time import sleep

from src.registers import Registers
from src.decoder import Decoder


class CPU:
    def __init__(self, program: list[int], clock: float):
        self.program = program
        self.clock = clock

        self.pc = 0
        self.running = False
        self.isa = {
            "hlt": {"callback": self._hlt, "layout": (6, 0, 0, 0)},
            "ldi": {"callback": self._ldi, "layout": (6, 4, 0, 0)},
            "add": {"callback": self._add, "layout": (6, 4, 2, 0)},
            "jmp": {"callback": self._jmp, "layout": (6, 3, 0, 0)},
        }

        self.registers = Registers(4)
        self.decoder = Decoder(self, self.isa)

        print(
            "===========\n"
            f"CPU INIT:\n"
            f"PC: {self.pc}\n"
            f"registers: {self.registers._registers}\n"
            "==========="
        )

    def _hlt(self):
        print("$ halting cpu")
        self.running = False

    def _ldi(self, dest: int, val: int):
        print(f"$ loading imediate value #{val} to &{dest}")
        self.registers.write(dest, val)

    def _add(self, dest: int, read_a: int, read_b: int):
        print(f"$ adding &{read_a} + &{read_b} to &{dest}")
        n = self.registers.read(read_a) + self.registers.read(read_b)
        self.registers.write(dest, n & 0xF)

    def _jmp(self, dest: int):
        print(f"$ jumping to instruction at &{dest}")
        self.pc = dest

    def run(self):
        self.running = True
        while self.running:
            if self.pc > (len(self.program) - 1):
                self.pc = 0

            print(f"\nEXECUTING INSTRUCtION AT &{self.pc}")

            pc_before = self.pc
            self.decoder.fetch(self.program[self.pc])

            if self.pc == pc_before:
                self.pc += 1

            sleep(self.clock)
