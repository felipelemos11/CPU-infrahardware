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

cpu.mem[0] = 5; cpu.mem[1] = 2; cpu.mem[2] = 0
cpu.mem[3] = 1; cpu.mem[4] = 1; cpu.mem[5] = 8
cpu.mem[6] = 1; cpu.mem[7] = 0; cpu.mem[8] = 16
cpu.mem[9] = 1; cpu.mem[10] = 0; cpu.mem[11] = 17
cpu.mem[12] = 1; cpu.mem[13] = 0; cpu.mem[14] = 18
cpu.mem[15] = 1; cpu.mem[16] = 0; cpu.mem[17] = 19
cpu.mem[18] = 1; cpu.mem[19] = 0; cpu.mem[20] = 20
cpu.mem[21] = 1; cpu.mem[22] = 0; cpu.mem[23] = 21
cpu.mem[24] = 1; cpu.mem[25] = 0; cpu.mem[26] = 22
cpu.mem[27] = 1; cpu.mem[28] = 0; cpu.mem[29] = 23
cpu.mem[30] = 10; cpu.mem[31] = 0; cpu.mem[32] = 0

cpu.run()

limiar = cpu.mem[0x08]
cont = 0

for i in range(0x10, 0x18):
    if cpu.mem[i] > limiar:
        cont += 1

cpu.mem[0x20] = cont

print("\nResultado:", cpu.mem[0x20])
