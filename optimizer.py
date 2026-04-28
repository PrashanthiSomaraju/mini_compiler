def optimize(tokens):
    try:
        if tokens[0] == "print":
            return "No Optimization"

        expr = tokens[3:] if tokens[0] == "int" else tokens[2:]
        result = eval("".join(expr))

        var = tokens[1] if tokens[0] == "int" else tokens[0]
        return f"{var} = {result}"

    except:
        return "No Optimization"