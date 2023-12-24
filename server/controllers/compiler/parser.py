# Yacc example

import ply.yacc as yacc
from db.functions import create_database
# Get the token map from the lexer.  This is required.
from controllers.compiler.lexer import tokens 

from db.functions import create_database, use_database


def p_init(t):
    '''init : statement init
            | statement'''

def p_statement(t):
    '''statement : create_database
                | use_database'''
    t[0] = t[1]

def p_create_database(t):
    '''create_database : CREATE DATA BASE ID SEMICOLOM'''
    t[0] = t[4]
    create_database.create_database(t[4])
    print(f"Database {t[4]} was created successfully")

def p_use_database(t):
    '''use_database : USE ID SEMICOLOM'''
    t[0] = t[2]
    use_database.use_database(t[2]) 

# Error rule for syntax errors
def p_error(p):
    print("Syntax error in input!")

# Build the parser
parser = yacc.yacc()



