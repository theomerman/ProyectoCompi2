from xml.etree import ElementTree as ET
from controllers.validations.get_current_database import get_current_database
from controllers.validations.get_database import get_database
from controllers.validations.is_table import is_table
from controllers.validations.write_to_xml import write_to_xml
from controllers.validations.get_table import get_table
from controllers.validations.is_column import is_column
from xml.dom import minidom


def create_table(_table: str, columns: list) -> tuple:
    database, err = get_database()
    if err is not None:
        return None, err
    is_table_value, err = is_table(_table)
    if is_table_value:
        return None, f"Table {_table} already exists" 


    table = ET.SubElement(database.find("tables"), _table)
    tmp_columns = []
    ET.SubElement(table, "columns")
    ET.SubElement(table, "data_rows")
    for column in columns:
        column.change_nullability()
        if column.name in tmp_columns:
            return None, f"Column {column.name} already exists and was not added or modified to table {_table}"
        if column.reference is not None:
            # print(column.reference,"*************************************")
            reference_table_name = column.reference.split('.')[0]
            reference_column_name = column.reference.split('.')[1]
            _, err = validate_reference(reference_table_name, reference_column_name)
            if err is not None:
                return None, err
        ET.SubElement(table.find("columns"), column.name, attrib={"type": str(column.type), "primary_key": str(column.primary_key), "nullable": str(column.nullable), "reference": str(column.reference)})
        tmp_columns.append(column.name)
    writer, err = write_to_xml(database)
    if err is not None:
        return None, err
    else:
        return f"Table {_table} created successfully", None

def validate_reference(table_name, column_name):
    table, err = get_table(table_name)
    if err is not None:
        return None, f"Error: Reference table {table_name} does not exist"
    if table.find("columns").find(column_name) is None:
        return None, f"Error: Reference column {column_name} does not exist in table {table_name}"
    return True, None
