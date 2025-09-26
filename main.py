from src.cpu import CPU


if __name__ == "__main__":

    pg = [0b01000000, 0b01010001, 0b10000001, 0b10010001, 0b11010000]
    cpu = CPU(pg, 1)
    cpu.run()
