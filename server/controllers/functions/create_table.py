from xml.etree import ElementTree as ET
from controllers.validations.get_current_database import get_current_database
from controllers.validations.get_database import get_database
from controllers.validations.is_table import is_table
from controllers.validations.write_to_xml import write_to_xml
from xml.dom import minidom


def create_table(_table: str, columns: list) -> tuple:
    database, err = get_database()
    if err is not None:
        return None, err
    is_table_value, err = is_table(_table)
    if is_table_value:
        return None, f"Table {_table} already exists" 

    table = ET.SubElement(database, _table)
    tmp_columns = []

    for column in columns:
        column.change_nullability()
        if column.name in tmp_columns:
            return None, f"Column {column.name} already exists and was not added or modified to table {_table}"
        ET.SubElement(table, column.name, attrib={"type": str(column.type), "primary_key": str(column.primary_key), "nullable": str(column.nullable), "reference": str(column.reference)})
        tmp_columns.append(column.name)
    ET.SubElement(table, "data_rows")
    writer, err = write_to_xml(database)
    if err is not None:
        return None, err
    else:
        return f"Table {_table} created successfully", None

