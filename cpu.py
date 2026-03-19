class MiniCPU:
    def __init__(self):
        self.mem = [0] * 256
        self.reg = [0, 0, 0, 0]
        self.pc = 0
        self.zf = 0
        self.running = True
        self.ciclo = 0

    def fetch(self):
        op = self.mem[self.pc]
        a = self.mem[self.pc + 1]
        b = self.mem[self.pc + 2]
        self.pc += 3
        return op, a, b

    def exec(self, op, a, b):
        if op == 1:
            self.reg[a] = self.mem[b]
        elif op == 2:
            self.mem[b] = self.reg[a]
        elif op == 3:
            self.reg[a] = (self.reg[a] + self.reg[b]) & 0xFF
        elif op == 4:
            self.reg[a] = (self.reg[a] - self.reg[b]) & 0xFF
        elif op == 5:
            self.reg[a] = b
        elif op == 6:
            self.zf = 1 if self.reg[a] == self.reg[b] else 0
        elif op == 7:
            self.pc = a
        elif op == 8:
            if self.zf:
                self.pc = a
        elif op == 9:
            if not self.zf:
                self.pc = a
        elif op == 10:
            self.running = False

    def trace(self, op, a, b):
        nomes = ["", "LOAD", "STORE", "ADD", "SUB", "MOV", "CMP", "JMP", "JZ", "JNZ", "HALT"]
        print(f"Ciclo {self.ciclo}: {nomes[op]} {a},{b} | R0={self.reg[0]} R1={self.reg[1]} R2={self.reg[2]} R3={self.reg[3]} | PC={self.pc} ZF={self.zf}")

    def run(self):
        while self.running and self.pc < 256:
            self.ciclo += 1
            op, a, b = self.fetch()
            self.exec(op, a, b)
            self.trace(op, a, b)


cpu = MiniCPU()

cpu.mem[0x08] = 20

cpu.mem[0x10] = 10
cpu.mem[0x11] = 25
cpu.mem[0x12] = 5
cpu.mem[0x13] = 30
cpu.mem[0x14] = 15
cpu.mem[0x15] = 40
cpu.mem[0x16] = 8
cpu.mem[0x17] = 22

cpu.mem[0x00] = 7
cpu.mem[0x01] = 0x30
cpu.mem[0x02] = 0

cpu.mem[0x30] = 5
cpu.mem[0x31] = 2
cpu.mem[0x32] = 0

cpu.mem[0x33] = 1
cpu.mem[0x34] = 1
cpu.mem[0x35] = 0x08

cpu.mem[0x36] = 1
cpu.mem[0x37] = 0
cpu.mem[0x38] = 0x10

cpu.mem[0x39] = 1
cpu.mem[0x3A] = 0
cpu.mem[0x3B] = 0x11

cpu.mem[0x3C] = 1
cpu.mem[0x3D] = 0
cpu.mem[0x3E] = 0x12

cpu.mem[0x3F] = 1
cpu.mem[0x40] = 0
cpu.mem[0x41] = 0x13

cpu.mem[0x42] = 1
cpu.mem[0x43] = 0
cpu.mem[0x44] = 0x14

cpu.mem[0x45] = 1
cpu.mem[0x46] = 0
cpu.mem[0x47] = 0x15

cpu.mem[0x48] = 1
cpu.mem[0x49] = 0
cpu.mem[0x4A] = 0x16

cpu.mem[0x4B] = 1
cpu.mem[0x4C] = 0
cpu.mem[0x4D] = 0x17

cpu.mem[0x4E] = 10
cpu.mem[0x4F] = 0
cpu.mem[0x50] = 0

cpu.run()

limiar = cpu.mem[0x08]
cont = 0

for i in range(0x10, 0x18):
    if cpu.mem[i] > limiar:
        cont += 1

cpu.mem[0x20] = cont

print("\nResultado:", cpu.mem[0x20])
