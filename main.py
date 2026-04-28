from lexer import lexical_analysis
from parser import syntax_analysis
from semantic import semantic_analysis, symbol_table
from intermediate import generate_ic
from optimizer import optimize
from codegen import target_code

print("="*55)
print("         MINI COMPILER USING PYTHON")
print("="*55)

print("\nEnter Multiple Statements")
print("Example:")
print("int a = 5;")
print("int b = 3;")
print("int c;")
print("c = a + b;")
print("print(c);")
print("Type END to finish input\n")

lines = []

while True:
    line = input()

    if line.upper() == "END":
        break

    lines.append(line)

program = " ".join(lines)
statements = program.split(";")

for stmt in statements:
    stmt = stmt.strip()

    if stmt == "":
        continue

    print("\n" + "="*55)
    print("SOURCE STATEMENT :", stmt + ";")
    print("="*55)

    tokens = lexical_analysis(stmt)

    print("\n1. LEXICAL ANALYSIS")
    print(tokens)

    print("\n2. SYNTAX ANALYSIS")
    if syntax_analysis(tokens):
        print("Valid Syntax")
    else:
        print("Invalid Syntax")
        continue

    print("\n3. SEMANTIC ANALYSIS")
    print(semantic_analysis(tokens))

    print("\n4. INTERMEDIATE CODE")
    ic = generate_ic(tokens)
    for i in ic:
        print(i)

    print("\n5. CODE OPTIMIZATION")
    print(optimize(tokens))

    print("\n6. TARGET CODE")
    tc = target_code(tokens)
    for i in tc:
        print(i)

print("\n" + "="*55)
print("FINAL SYMBOL TABLE")
print("="*55)

print("Variable\tValue")
for key, value in symbol_table.items():
    print(f"{key}\t\t{value}")

print("\nCompilation Completed Successfully")