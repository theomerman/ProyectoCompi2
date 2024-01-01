from controllers.functions import alter_table
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

