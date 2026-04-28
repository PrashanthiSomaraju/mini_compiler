import re

def lexical_analysis(code):
    pattern = r'int|print|[a-zA-Z_]\w*|\d+|[=+\-*/();]'
    return re.findall(pattern, code)