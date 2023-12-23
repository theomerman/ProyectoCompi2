import ply.lex as lex

# Define the tokens
tokens = (
    'NUMBER',
    'DECIMAL',
    'PLUS',
    'MINUS',
    'TIMES',
    'DIVIDE',
    'LPAREN',
    'RPAREN',
    'SEMICOLOM',   
)

t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_SEMICOLOM = r';'

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_DECIMAL(t):
    r'\d+\.\d+'
    t.value = float(t.value)
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

t_ignore = ' \t'

def t_error(t):
    print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)

lexer = lex.lex()

data = '''
3 + 4 * 10
  + -20 *2
'''

# lexer.input(data)

# for tok in lexer:
#     print(tok)