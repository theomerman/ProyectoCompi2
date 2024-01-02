
import ply.yacc as yacc
from controllers.functions import create_database
# Get the token map from the lexer.  This is required.
from controllers.compiler.lexer import tokens 
from controllers.functions import create_database,use_database, create_table, insert, alter_table
from controllers.objects.column import Column
from controllers.objects.Node import Node, traverse
from controllers.functions import select
# from controllers.compiler.grammar.concatena import p_concat, p_concatena, p_concatena_param

precedence = (
    ('right', 'PLUS', 'MINUS'),
    ('right', 'TIMES', 'DIVIDE'),
    ('right','EQUAL', 'DIFFERENT', 'GREATER', 'LESS', 'GREATER_EQUAL', 'LESS_EQUAL'),
    ('right', 'OR'),
    ('right', 'AND', 'AND_WORD'),
    ('left', 'UMINUS'),
)
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
                | select_total
                '''

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




############################# SELECT ################################
            
def p_select_total(p):
    '''
    select_total : SELECT select_columns from_statement SEMICOLON
    '''
    # print(p[2],p[3]) 
    select.select(p[2], p[3])
    


def p_select_columns(p):
    '''
    select_columns  : select_columns COMMA select_column
                    | select_column
    '''
    if len(p) == 4:
        p[0] = p[1] + [p[3]]
    elif len(p) == 2:
        p[0] = [p[1]]

def p_select_column(p):
    '''
    select_column   : concatena
                    | substraer
                    | hoy
                    | contar
                    | suma
                    | parameters_two
                    | TIMES
    '''
    p[0] = p[1]

def p_from_statement(p):
    '''
    from_statement  : FROM ids where_statement
                    | empty
    '''
    if len(p) == 4:
        if p[3] != None:
            p[0] = [p[2], p[3]]
        else:
            p[0] = [p[2]]
        # p[0] = p[2]
    else:
        p[0] = None

def p_where_statement(p):
    '''
    where_statement : WHERE expression
                    | empty
    '''
    if len(p) == 3:
        p[0] = p[2]
    else:
        p[0] = None

############################# EXPRESSION ################################
def p_expression(p):
    '''
    expression : expression PLUS expression
                | expression MINUS expression
                | expression TIMES expression
                | expression DIVIDE expression

                | expression EQUAL expression
                | expression DIFFERENT expression
                | expression GREATER expression
                | expression LESS expression
                | expression GREATER_EQUAL expression
                | expression LESS_EQUAL expression

                | expression AND expression
                | expression AND_WORD expression
                | expression OR expression
                | expression NOT_SYMBOL expression
    '''
    p[0] = Node(p[2])
    p[0].left = p[1]
    p[0].right = p[3]
    
def p_uminus_expression(p):
    'expression : MINUS expression %prec UMINUS'
    p[0] = Node(p[1])
    p[0].left =p[2]

def p_expression_primitives(p):
    '''
    expression  : LPAREN expression RPAREN
                | NUMBER
                | DECIMALES
                | STRING

    '''
    if len(p) == 4:
        p[0] = p[2]
    else:
        p[0] = Node(p[1])

def p_expresion_primitives2(p):
    '''
    expression  : ID PERIOD ID
                | ID
    '''
    if len(p) == 4:
        p[0] = Node(p[1] + "." + p[3])
    else:
        p[0] = Node(p[1])
        




########################### native_functions ###############################
    
# CONCATENA
            
def p_concatena(p):
    '''
    concatena : CONCATENA LPAREN concatena_parameters RPAREN
    '''
    p[0] = [p[1], p[3]]
        
def p_concatena_param(p):
    '''
    concatena_parameters    : concatena_parameters COMMA parameters_one
                            | parameters_one
    '''
    if len(p) == 4:
        p[0] = p[1] + [p[3]]
    elif len(p) == 2:
        p[0] = [p[1]]
    
def p_parameters_one(p):
    '''
    parameters_one  : STRING
                    | ID PERIOD ID
                    | ID
    '''
    if len(p) == 4:
        p[0] = p[1] + "." + p[3]
    else:
        p[0] = p[1]

# SUBSTRAER
def p_substraer(p):
    '''
    substraer : SUBSTRAER LPAREN parameters_one COMMA NUMBER COMMA NUMBER RPAREN
    '''
    p[0] = [p[1], [p[3], p[5], p[7]]]

# HOY
def p_hoy(p):
    '''
    hoy : HOY LPAREN RPAREN
    '''
    p[0] = [p[1], None]

# CONTAR
def p_contar(p):
    '''
    contar : CONTAR LPAREN contar_parameters RPAREN
    '''
    p[0] = [p[1], p[3]]

def p_contar_param(p):
    '''
    contar_parameters   : TIMES
                        | ID PERIOD ID
                        | ID 
    '''
    p[0] = p[1]

# SUMA
def p_suma(p):
    '''
    suma : SUMA LPAREN parameters_two RPAREN

    '''
    p[0] = [p[1], p[3]]
def p_parameters_two(p):
    '''
    parameters_two  : ID PERIOD ID
                    | ID
    '''
    if len(p) == 4:
        p[0] = p[1] + "." + p[3]
    else:
        p[0] = p[1]










# empty
def p_empty(p):
   'empty :' 
   pass

# Error rule for syntax errors
def p_error(p):
    print("Syntax error in input!")





# Build the parser
parser = yacc.yacc()



