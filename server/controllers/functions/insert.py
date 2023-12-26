from controllers.validations.get_table import get_table

def insert(table_name, columns, values):
    table = get_table(table_name)
    if table is None:
        return None
    if len(columns) != len(values):
        print("Error: The number of columns and values does not match")
        return False
    for i in range(len(columns)):
        column = columns[i]
        value = values[i]
        if column not in table.columns:
            return None
        if table.columns[column].type != value.type:
            return None
    return table.insert(columns, values)