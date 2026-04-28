def target_code(tokens):
    output = []

    if tokens[0] == "print":
        output.append(f"OUT {tokens[2]}")
        return output

    var = tokens[1] if tokens[0] == "int" else tokens[0]

    expr = tokens[3:] if tokens[0] == "int" else tokens[2:]

    if len(expr) == 1:
        output.append(f"MOV R1, {expr[0]}")
        output.append(f"MOV {var}, R1")

    elif len(expr) == 3:
        output.append(f"MOV R1, {expr[0]}")
        output.append(f"MOV R2, {expr[2]}")

        if expr[1] == '+':
            output.append("ADD R1, R2")
        elif expr[1] == '-':
            output.append("SUB R1, R2")
        elif expr[1] == '*':
            output.append("MUL R1, R2")
        elif expr[1] == '/':
            output.append("DIV R1, R2")

        output.append(f"MOV {var}, R1")

    return output