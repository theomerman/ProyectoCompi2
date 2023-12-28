from controllers.validations.get_table import get_table
from controllers.validations.is_column import is_column
from xml.etree import ElementTree as ET
def is_duplicated(table_name, column_name, value) -> tuple[bool, str]:
    table, err= get_table(table_name)
    if err is not None:
        return None, err
    if is_column(table_name, column_name):
        return None, f"Error: Column {column_name} does not exist in table {table_name}"

    items = table.find("data_rows")

    for item in items:
        if item.find(column_name).text == value:
            return True, None


def is_duplicated_pk(table: ET.Element, new_item: ET.Element) -> bool:
    cols = []
    for column in table:
        if column.tag == "data_rows":
            continue
        if column.attrib["primary_key"] == "True":
            cols.append(column.tag)
    items = table.find("data_rows")
    for item in items:
        tmp = 0
        for col in cols:
            if item.find(col).text == new_item.find(col).text:
                tmp += 1
        if tmp == len(cols):
            return True
    return False