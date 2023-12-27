from controllers.validations.get_table import get_table
from controllers.validations.is_column import is_column
from xml.etree import ElementTree as ET
def is_duplicated(table_name, column_name, value):
    table, err= get_table(table_name)
    if err is not None:
        return None, err
    if is_column(table_name, column_name):
        return None, f"Error: Column {column_name} does not exist in table {table_name}"

    items = table.find("data_rows")

    for item in items:
        pass