from controllers.validations.get_table import get_table

def is_column(table_name, column_name):
    table, err = get_table(table_name)
    if err is not None:
        return None, err
    if table.find(column_name) is None:
        return False, None
    return True, None
