
def p_concatena(p):
    '''
    concatenar : CONCATENA LPAREN concatena_parameters RPAREN
    '''
    

def p_concatena_param(p):
    '''
    concatena_parameters    : concatena_parameters COMMA concat
                            | concat
    '''
    


def p_concat(p):
    '''
    concat  : STRING
            | ID PERIOD ID
            | ID
    '''
    # print(p[1])
