class Registers:
    def __init__(self, registers: int):
        self._registers = [0] * registers

    def read(self, read: int):
        print(f"+ registers - reading &{read} -> {self._registers[read]}")
        return self._registers[read]

    def write(self, dest: int, val: int):
        print(f"+ registers - writing {val} -> &{dest}")
        self._registers[dest] = val & 0xF
        self.print_registers()

    def print_registers(self):
        s = ""
        for i in range(len(self._registers)):
            s += f"r{i}:[{self._registers[i]}] "
        print(s)
