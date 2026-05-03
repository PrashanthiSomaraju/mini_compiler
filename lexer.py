import re

KEYWORDS = {'int', 'float', 'if', 'else', 'while', 'print'}

TOKEN_SPEC = [
    ('FLOAT',     r'\d+\.\d+'),
    ('INT',       r'\d+'),
    ('ID',        r'[A-Za-z_]\w*'),
    ('RELOP',     r'==|!=|<=|>=|<|>'),
    ('ASSIGN',    r'='),
    ('PLUS',      r'\+'),
    ('MINUS',     r'-'),
    ('MUL',       r'\*'),
    ('DIV',       r'/'),
    ('LPAREN',    r'\('),
    ('RPAREN',    r'\)'),
    ('LBRACE',    r'\{'),
    ('RBRACE',    r'\}'),
    ('SEMICOLON', r';'),
    ('SKIP',      r'[ \t]+'),
    ('NEWLINE',   r'\n'),
    ('MISMATCH',  r'.'),
]

MASTER = re.compile('|'.join(f'(?P<{n}>{p})' for n, p in TOKEN_SPEC))


class Token:
    def __init__(self, type_, value, line):
        self.type = type_
        self.value = value
        self.line = line

    def __repr__(self):
        return f"{self.type:<10} {self.value:<10} line:{self.line}"


def tokenize(code):
    tokens = []
    line = 1

    for m in MASTER.finditer(code):
        kind = m.lastgroup
        value = m.group()

        if kind == 'NEWLINE':
            line += 1
        elif kind == 'SKIP':
            continue
        elif kind == 'ID' and value in KEYWORDS:
            tokens.append(Token("KEYWORD", value, line))
        elif kind == 'MISMATCH':
            raise SyntaxError(f"Invalid character '{value}' at line {line}")
        else:
            tokens.append(Token(kind, value, line))

    return tokens
