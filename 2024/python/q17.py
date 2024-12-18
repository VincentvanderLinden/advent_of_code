from time import sleep
# Combo operands 0 through 3 represent literal values 0 through 3.
# Combo operand 4 represents the value of register A.
# Combo operand 5 represents the value of register B.
# Combo operand 6 represents the value of register C.
# Combo operand 7 is reserved and will not appear in valid programs.


program = [2,4,1,1,7,5,0,3,4,3,1,6,5,5,3,0]

A, B, C = 18427963, 0, 0
combos = {0: 0, 1: 1, 2: 2, 3: 3, 4: A, 5: B, 6: C}

output = []
pointer = 0
while pointer < len(program): 
    jump = False
    op, combo = program[pointer:pointer + 2]
    if op == 0: 
        A = int(A / (2**combos[combo]))
        combos[4] = A
    elif op == 1:
        B = B ^ combo  
        combos[5] = B 
    elif op == 2: 
        B = combos[combo] % 8
        combos[5] = B
    elif op == 3: 

        if A == 0: 
            next
        else: 
            jump = True
            pointer = combo

    elif op == 4: 
        B = B ^ C
        combos[5] = B
    elif op == 5: 
        output.append(str(combos[combo]%8))
    elif op == 6: 
        B = A // 2**combos[combo]
        combos[5] = B
    elif op == 7: 
        C = A // 2**combos[combo]
        combos[6] = C
    
    if not jump: 
        pointer += 2
    
print(A)
print(f"Output: {','.join(output)}") 



