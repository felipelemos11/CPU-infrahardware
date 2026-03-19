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

    def execute(self, op, a, b):
        if op == 0x01:
            self.reg[a] = self.mem[b]
        elif op == 0x02:
            self.mem[b] = self.reg[a]
        elif op == 0x03:
            self.reg[a] = (self.reg[a] + self.reg[b]) & 0xFF
        elif op == 0x04:
            self.reg[a] = (self.reg[a] - self.reg[b]) & 0xFF
        elif op == 0x05:
            self.reg[a] = b
        elif op == 0x06:
            self.zf = 1 if self.reg[a] == self.reg[b] else 0
        elif op == 0x07:
            self.pc = a
        elif op == 0x08:
            if self.zf:
                self.pc = a
        elif op == 0x09:
            if not self.zf:
                self.pc = a
        elif op == 0x0A:
            self.running = False

    def trace(self, op, a, b):
        nomes = {
            0x01: "LOAD",
            0x02: "STORE",
            0x03: "ADD",
            0x04: "SUB",
            0x05: "MOV",
            0x06: "CMP",
            0x07: "JMP",
            0x08: "JZ",
            0x09: "JNZ",
            0x0A: "HALT"
        }
        nome = nomes.get(op, "???")
        print(
            f"Ciclo {self.ciclo}: {nome} {a},{b} | "
            f"R0={self.reg[0]} R1={self.reg[1]} R2={self.reg[2]} R3={self.reg[3]} | "
            f"PC={self.pc} ZF={self.zf}"
        )

    def run(self):
        while self.running and self.pc < 256:
            self.ciclo += 1
            op, a, b = self.fetch()
            self.execute(op, a, b)
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

cpu.mem[0x00] = 0x07
cpu.mem[0x01] = 0x30
cpu.mem[0x02] = 0x00

cpu.mem[0x30] = 0x05
cpu.mem[0x31] = 0x02
cpu.mem[0x32] = 0x00

cpu.mem[0x33] = 0x01
cpu.mem[0x34] = 0x01
cpu.mem[0x35] = 0x08

cpu.mem[0x36] = 0x01
cpu.mem[0x37] = 0x00
cpu.mem[0x38] = 0x10

cpu.mem[0x39] = 0x01
cpu.mem[0x3A] = 0x00
cpu.mem[0x3B] = 0x11

cpu.mem[0x3C] = 0x01
cpu.mem[0x3D] = 0x00
cpu.mem[0x3E] = 0x12

cpu.mem[0x3F] = 0x01
cpu.mem[0x40] = 0x00
cpu.mem[0x41] = 0x13

cpu.mem[0x42] = 0x01
cpu.mem[0x43] = 0x00
cpu.mem[0x44] = 0x14

cpu.mem[0x45] = 0x01
cpu.mem[0x46] = 0x00
cpu.mem[0x47] = 0x15

cpu.mem[0x48] = 0x01
cpu.mem[0x49] = 0x00
cpu.mem[0x4A] = 0x16

cpu.mem[0x4B] = 0x01
cpu.mem[0x4C] = 0x00
cpu.mem[0x4D] = 0x17

cpu.mem[0x4E] = 0x0A
cpu.mem[0x4F] = 0x00
cpu.mem[0x50] = 0x00

cpu.run()

limiar = cpu.mem[0x08]
contador = 0

for i in range(0x10, 0x18):
    if cpu.mem[i] > limiar:
        contador += 1

cpu.mem[0x20] = contador

print("\nLimiar:", cpu.mem[0x08])
print("Valores:", cpu.mem[0x10:0x18])
print("Resultado em 0x20:", cpu.mem[0x20])
