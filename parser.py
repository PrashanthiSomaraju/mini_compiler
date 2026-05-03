class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.pos = 0

    def current(self):
        return self.tokens[self.pos] if self.pos < len(self.tokens) else None

    def eat(self, expected_type=None, expected_value=None):
        tok = self.current()
        if not tok:
            raise SyntaxError("Unexpected end of input")

        if expected_type and tok.type != expected_type:
            raise SyntaxError(f"Expected {expected_type}, got {tok.type}")

        if expected_value and tok.value != expected_value:
            raise SyntaxError(f"Expected {expected_value}, got {tok.value}")

        self.pos += 1
        return tok

    # -------------------------
    # Program
    # -------------------------
    def parse_program(self):
        stmts = []
        while self.current():
            stmts.append(self.parse_stmt())
        return stmts

    # -------------------------
    # Statement Dispatcher
    # -------------------------
    def parse_stmt(self):
        tok = self.current()

        if tok.type == 'KEYWORD' and tok.value in ('int', 'float'):
            return self.parse_decl()

        elif tok.type == 'KEYWORD' and tok.value == 'print':
            return self.parse_print()

        elif tok.type == 'KEYWORD' and tok.value == 'if':
            return self.parse_if()

        elif tok.type == 'KEYWORD' and tok.value == 'while':
            return self.parse_while()

        elif tok.type == 'ID':
            return self.parse_assign()

        else:
            raise SyntaxError(f"Invalid statement starting with {tok.value}")

    # -------------------------
    # Declaration
    # -------------------------
    def parse_decl(self):
        dtype = self.eat('KEYWORD')
        var = self.eat('ID')

        if self.current() and self.current().type == 'ASSIGN':
            self.eat('ASSIGN')
            expr = self.parse_expr()
        else:
            expr = None

        self.eat('SEMICOLON')
        return ("DECL", dtype.value, var.value, expr)

    # -------------------------
    # Assignment
    # -------------------------
    def parse_assign(self):
        var = self.eat('ID')
        self.eat('ASSIGN')
        expr = self.parse_expr()
        self.eat('SEMICOLON')
        return ("ASSIGN", var.value, expr)

    # -------------------------
    # Print
    # -------------------------
    def parse_print(self):
        self.eat('KEYWORD', 'print')
        self.eat('LPAREN')
        expr = self.parse_expr()
        self.eat('RPAREN')
        self.eat('SEMICOLON')
        return ("PRINT", expr)

    # -------------------------
    # Expressions
    # -------------------------
    def parse_expr(self):
        left = self.parse_term()

        while self.current() and self.current().type in ('PLUS', 'MINUS'):
            op = self.eat().value
            right = self.parse_term()
            left = ("BINOP", op, left, right)

        return left

    def parse_term(self):
        left = self.parse_factor()

        while self.current() and self.current().type in ('MUL', 'DIV'):
            op = self.eat().value
            right = self.parse_factor()
            left = ("BINOP", op, left, right)

        return left

    def parse_factor(self):
        tok = self.current()

        if tok.type in ('INT', 'FLOAT'):
            self.eat()
            return ("NUM", tok.value)

        elif tok.type == 'ID':
            self.eat()
            return ("VAR", tok.value)

        elif tok.type == 'LPAREN':
            self.eat('LPAREN')
            expr = self.parse_expr()
            self.eat('RPAREN')
            return expr

        else:
            raise SyntaxError(f"Unexpected token {tok.value}")
