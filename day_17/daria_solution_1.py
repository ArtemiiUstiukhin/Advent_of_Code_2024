def combo_val(op, A, B, C):
    if op <= 3:
        return op
    elif op == 4:
        return A
    elif op == 5:
        return B
    elif op == 6:
        return C


with open("day_17/test_input.txt") as f:
    lines = [l.strip() for l in f if l.strip()]

A = int(lines[0].split(":")[1].strip())
B = int(lines[1].split(":")[1].strip())
C = int(lines[2].split(":")[1].strip())

prog_str = lines[3].split(":")[1].strip()
program = list(map(int, prog_str.split(",")))

ip = 0
output = []

while ip < len(program):
    opcode = program[ip]
    if ip + 1 >= len(program):
        break
    operand = program[ip + 1]

    if opcode == 0: 
        denom = 2 ** (combo_val(operand, A, B, C))
        A = A // denom
        ip += 2
    elif opcode == 1:  
        B = B ^ operand
        ip += 2
    elif opcode == 2: 
        val = combo_val(operand, A, B, C) % 8
        B = val
        ip += 2
    elif opcode == 3: 
        if A != 0:
            ip = operand
        else:
            ip += 2
    elif opcode == 4:
        B = B ^ C
        ip += 2
    elif opcode == 5: 
        val = combo_val(operand, A, B, C) % 8
        output.append(val)
        ip += 2
    elif opcode == 6: 
        denom = 2 ** (combo_val(operand, A, B, C))
        B = A // denom
        ip += 2
    elif opcode == 7:
        denom = 2 ** (combo_val(operand, A, B, C))
        C = A // denom
        ip += 2
    else:
        break

print(",".join(map(str, output)))
