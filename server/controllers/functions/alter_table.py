from controllers.validations.get_database import get_database
from controllers.validations.get_table import get_table
from controllers.validations.write_to_xml import write_to_xml
from controllers.validations.is_column import is_column
from xml.etree import ElementTree as ET
def add_column(table_name, column_name, column_type) -> tuple:
    database, err = get_database()
    if err:
        return None, err
    table, err = get_table(table_name, database)
    if err is not None:
        return None, err

    if table.find("columns").find(column_name) is not None:
        return None, f"Error: Column {column_name} already exists in table {table_name}"
    ET.SubElement(table.find("columns"), column_name, attrib={"type": str(column_type), "primary_key": str(False), "nullable": str(True), "reference": str(None)})

    for item in table.find('data_rows'):
        item.append(ET.Element(column_name))
        item.find(column_name).text = 'null'

    _, err = write_to_xml(database)
    if err is not None:
        return None, err
    else:
        return f"Column {column_name} added successfully", None
    

def drop_column(table_name, column_name) -> tuple:
    database , err = get_database()
    if err:
        return None, err
    table, err = get_table(table_name, database)
    if err is not None:
        return None, err
    if table.find("columns").find(column_name) is None:
        return None, f"Error: Column {column_name} does not exists in table {table_name}"
    for _table in database.find('tables'):
        if _table.tag == table_name:
            continue
        for _column in _table.find('columns'):
            if _column.get('reference') == f"{table_name}.{column_name}":
                return None, f"Error: Column {column_name} is being referenced by {_table.tag}.{_column.tag} and cannot be deleted"
    table.find("columns").remove(table.find("columns").find(column_name))
    for item in table.find('data_rows'):
        item.remove(item.find(column_name))
    _, err = write_to_xml(database)
    if err is not None:
        return None, err
    else:
        return f"Column {column_name} dropped successfully", None