import ply.lex as lex

# Define the tokens
tokens = [
    'NUMBER',
    'DECIMALES',
    'PLUS',
    'MINUS',
    'TIMES',
    'DIVIDE',
    'LPAREN',
    'RPAREN',
    'SEMICOLON',   
    'COMMA',
    'PERIOD',
    'COMPARE',
    'EQUAL',
    'ID',
    'AT',

    "DIFFERENT",
    'GREATER',
    'LESS',
    'GREATER_EQUAL',
    'LESS_EQUAL',

    'AND',
    'OR',
    'NOT_SYMBOL',
    'NOT_EQUAL',
]

reserved = {
    'create': 'CREATE',
    'data': 'DATA',
    'base': 'BASE',
    'use': 'USE',
    'table': 'TABLE',
    'int': 'INT',
    'decimal': 'DECIMAL',
    'primary': 'PRIMARY',
    'key': 'KEY',
    'nvarchar': 'NVARCHAR',
    'not': 'NOT',
    'null': 'NULL',
    'date': 'DATE',
    'reference': 'REFERENCE',

    'insert': 'INSERT',
    'into': 'INTO',
    'values': 'VALUES',
    'string': 'STRING',
    'alter': 'ALTER',
    'add': 'ADD',
    'drop': 'DROP',
    'column': 'COLUMN',

    'select': 'SELECT',
    'from': 'FROM',
    'where': 'WHERE',

    'concatena': 'CONCATENA',
    'substraer': 'SUBSTRAER',
    'hoy': 'HOY',
    'contar': 'CONTAR',
    'suma': 'SUMA',
    'cast': 'CAST',
    'and': 'AND_WORD',
}
# Tokens
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_EQUAL = r'='
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_SEMICOLON = r';'
t_COMMA = r','
t_PERIOD = r'\.'
t_AT = r'@'

# Comparison operators

t_COMPARE = r'=='
t_DIFFERENT = r'!='
t_GREATER = r'>'
t_LESS = r'<'
t_GREATER_EQUAL = r'>='
t_LESS_EQUAL = r'<='

# Logical operators
t_AND = r'&&'
t_OR = r'\|\|'
t_NOT_SYMBOL = r'!'
t_NOT_EQUAL = r'<>'


tokens = tokens + list(reserved.values())

def t_STRING(t):
    r"'([^\\']+|\\'|\\\\)*'"
    t.value = str(t.value).lower()
    return t

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value.lower(), 'ID')
    t.value = str(t.value).lower()
    return t

def t_DECIMALES(t):
    r'\d+\.\d+'
    t.value = float(t.value)
    return t

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

t_ignore = ' \t'

def t_error(t):
    print(f"********************************************Illegal character '{t.value[0]}'********************************************")
    t.lexer.skip(1)

lexer = lex.lex()

# data = '''
# SELECT tbcliente.codigocliente,CONCATENA(tbcliente.primer_nombre,tbcliente.primer_apellido),
# tbidentificacion.identificacion,tbidentificaciontipo.identificaciontipo
# FROM tbcliente,tbidentificacion ,tbidentificaciontipo 
# where tbcliente.codigocliente = tbidentificacion.codigocliente 
# && tbcliente.identificaciontipo = tbidentificacion.identificaciontipo;
# '''


# lexer.input(data)

# for tok in lexer:
#     print(tok)
