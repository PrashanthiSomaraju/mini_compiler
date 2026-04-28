def generate_ic(tokens):
    code = []

    if tokens[0] == "print":
        code.append(f"PRINT {tokens[2]}")
        return code

    var = tokens[1] if tokens[0] == "int" else tokens[0]

    if len(tokens) == 4:
        code.append(f"{var} = {tokens[3]}")

    elif len(tokens) >= 6:
        code.append(f"t1 = {' '.join(tokens[3:] if tokens[0]=='int' else tokens[2:])}")
        code.append(f"{var} = t1")

    return code