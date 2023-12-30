
import ply.yacc as yacc
from controllers.functions import create_database
# Get the token map from the lexer.  This is required.
from controllers.compiler.lexer import tokens 
from controllers.functions import create_database,use_database, create_table, insert, alter_table
from controllers.objects.column import Column


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
                | insert_into
                | alter_table
                '''
    p[0] = p[1]

# create_database
def p_create_database(p):
    '''create_database : CREATE DATA BASE ID SEMICOLON'''
    p[0] = p[4]

    success , err = create_database.create_database(p[4])
    if err:
        print(err)
    else:
        print(success)


# use_database
def p_use_database(p):
    '''use_database : USE ID SEMICOLON'''
    p[0] = p[2]

    success , err = use_database.use_database(p[2])
    if err:
        print(err)
    else:
        print(success)

# create_table 
def p_create_table(p):
    '''
    create_table : CREATE TABLE ID LPAREN columns RPAREN SEMICOLON

    '''
    success, err = create_table.create_table(p[3], p[5])
    if err:
        print(err)
    else:
        print(success)


def p_columns(p):
    '''
    columns : columns COMMA column
            | column
    '''
    if len(p) == 4:
        p[0] = p[1] + [p[3]]
    elif len(p) == 2:
        p[0] = [p[1]]
    

def p_column(p):
    '''
    column : ID type attributes
    '''
    tmp = Column(p[1], p[2])
    if p[3] == None:
        tmp.nullable = True
        tmp.primary_key = False
        tmp.reference = None
    else:
    # iterate dictionary
        for key, value in p[3].items():
            if key == 'nullable':
                tmp.nullable = value
            elif key == 'primary':
                tmp.primary_key = value
            elif key == 'reference':
                tmp.reference = value
    p[0] = tmp

def p_type(p):
    '''
    type : INT
         | DATE
         | NVARCHAR LPAREN NUMBER RPAREN
         | DECIMAL
    '''
    if p[1] == 'int':
        p[0] = 'int'
    elif p[1] == 'date':
        p[0] = 'date'
    elif p[1] == 'nvarchar':
        p[0] = int(p[3])
    elif p[1] == 'decimal':
        p[0] = 'decimal'

def p_attributes(p):
    '''
    attributes : attributes attribute
               | attribute
               | empty
    '''
    if len(p) == 3:
        if p[2] == 'not':
            p[1]["nullable"] = False
            p[0] = p[1]
        elif p[2] == 'primary':
            p[1]["primary"] = True
            p[0] = p[1]
        elif "." in p[2]:
            p[1]["reference"] = p[2]
            p[0] = p[1]
    elif len(p) == 2:
        if p[1] != None:
            if p[1] == 'not':
                p[0] = {'nullable': False}
            elif p[1] == 'primary':
                p[0] = {'primary': True}
            elif "." in p[1]:
                p[0] = {'reference': p[1]}

def p_attribute(p):
    '''
    attribute : PRIMARY KEY
              | REFERENCE ID LPAREN ID RPAREN
              | NOT NULL
    '''
    if p[1] == 'primary':
        p[0] = 'primary'
    elif p[1] == 'reference':
        p[0] = p[2] + "." + p[4]
    elif p[1] == 'not':
        p[0] = "not"
    
def p_insert_into(p):
    '''
    insert_into : INSERT INTO ID LPAREN ids RPAREN VALUES LPAREN primitives RPAREN SEMICOLON
    '''
    success, err, = insert.insert(p[3], p[5], p[9])
    if err:
        print(err)
    else:
        print(success)
    # insert(p[3], p[5], p[9])
    # print(p[5])
    # print(p[9])
    
def p_ids(p):
    '''
    ids : ids COMMA ID
        | ID
    '''
    if len(p) == 4:
        p[0] = p[1] + [p[3]]
    elif len(p) == 2:
        p[0] = [p[1]]
def p_primitives(p):
    '''
    primitives  : primitives COMMA primitive
                | primitive
    '''
    if len(p) == 4:
        p[0] = p[1] + [p[3]]
    elif len(p) == 2:
        p[0] = [p[1]]
def p_primitive(p):
    '''
    primitive   : NUMBER
                | DECIMALES
                | STRING
    '''
    p[0] = p[1]


def p_alter_table(p):
    '''
    alter_table : ALTER TABLE ID ADD COLUMN ID type SEMICOLON
                | ALTER TABLE ID DROP COLUMN ID SEMICOLON
    '''
    if p[4] == 'add':
        success, err = alter_table.add_column(p[3], p[6], p[7])
        if err:
            print(err)
        else:
            print(success)
    elif p[4] == 'drop':
        success, err = alter_table.drop_column(p[3], p[6])
        if err:
            print(err)
        else:
            print(success)

# empty
def p_empty(p):
   'empty :' 
   pass

# Error rule for syntax errors
def p_error(p):
    print("Syntax error in input!")




# Build the parser
parser = yacc.yacc()



