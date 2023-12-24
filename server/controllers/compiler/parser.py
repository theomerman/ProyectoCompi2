
import ply.yacc as yacc
from db.functions import create_database
# Get the token map from the lexer.  This is required.
from controllers.compiler.lexer import tokens 

from db.functions import create_database,use_database




# INIT
def p_init(p):
    '''init : statement init
            | statement
            '''

# statement
def p_statement(p):
    '''statement : create_database
                | use_database
                | create_table
                
                '''
    p[0] = p[1]


# create_database
def p_create_database(p):
    '''create_database : CREATE DATA BASE ID SEMICOLOM'''
    p[0] = p[4]

    if create_database.create_database(p[4]):
        print(f"Database {p[4]} was created successfully")


# use_database
def p_use_database(p):
    '''use_database : USE ID SEMICOLOM'''
    p[0] = p[2]
    use_database.use_database(p[2]) 


# create_table 
def p_create_table(p):
    '''
    create_table : CREATE TABLE ID LPAREN columns RPAREN SEMICOLOM
    '''
    print("table created")
def p_columns(p):
    '''
    columns : columns COMMA column
            | column

    column : ID type attributes

    '''

def p_type(p):
    '''
    type : INT
         | DATE
         | NVARCHAR LPAREN NUMBER RPAREN
         | DECIMAL
    '''

def p_attributes(p):
    '''
    attributes : attributes attribute
               | attribute
    '''

def p_attribute(p):
    '''
    attribute : PRIMARY KEY
              | REFERENCE ID LPAREN ID RPAREN
              | nullable
    '''

def p_nullable(p):
    '''
    nullable : NOT NULL
             | empty
    '''


# empty
def p_empty(p):
   'empty :' 

# Error rule for syntax errors
def p_error(p):
    print("Syntax error in input!")




# Build the parser
parser = yacc.yacc()



