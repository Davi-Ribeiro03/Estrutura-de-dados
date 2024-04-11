from stack import Stack

def imprimiInstrucoes(operacao):
    operandos = Stack(len(operacao))
    i=1

    for n in operacao:
        if n not in "* + - /":
            operandos.push(n)

        else:
            op1 = operandos.pop()
            op2 = operandos.pop()
            print(f"LD {op2}")

            if n == "*":
                print(f"ML {op1}")

            elif n == "+":
                print(f"AD {op1}")

            elif n == "-":
                print(f"SB {op1}")

            elif n == "/":
                print(f"DV {op1}")
            
            print(f"ST TEMP{i}")
            operandos.push(f"TEMP{i}")
            i+=1
             

# imprimiInstrucoes("ABC*+DE-/")
imprimiInstrucoes("34+5*")
