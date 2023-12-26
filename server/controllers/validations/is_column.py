from controllers.validations.get_table import get_table

def is_column(table_name, column_name):
    table = get_table(table_name)
    if table is None:
        return False
    for column in table:
        if column.tag == column_name:
            return True
    return False