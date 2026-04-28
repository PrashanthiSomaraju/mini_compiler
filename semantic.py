symbol_table = {}

def evaluate_expression(tokens):
    expr = ""

    for t in tokens:
        if t in symbol_table:
            expr += str(symbol_table[t])
        else:
            expr += t

    return eval(expr)

def semantic_analysis(tokens):
    global symbol_table

    # Declaration
    if tokens[0] == "int":
        var = tokens[1]

        if var in symbol_table:
            return f"Error: {var} already declared"

        if len(tokens) > 3:
            value = evaluate_expression(tokens[3:])
            symbol_table[var] = value
        else:
            symbol_table[var] = 0

        return f"{var} declared successfully"

    # Print
    elif tokens[0] == "print":
        var = tokens[2]
        if var in symbol_table:
            return f"Value of {var} = {symbol_table[var]}"
        return "Variable not found"

    # Assignment
    else:
        var = tokens[0]

        if var not in symbol_table:
            return f"Error: {var} not declared"

        value = evaluate_expression(tokens[2:])
        symbol_table[var] = value
        return f"{var} updated successfully"