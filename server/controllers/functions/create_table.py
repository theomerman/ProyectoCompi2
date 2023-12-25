from xml.etree import ElementTree as ET
from controllers.validations.is_database import is_database
from controllers.validations.get_current_database import get_current_database
from controllers.validations.get_database import get_database
from controllers.validations.is_table import is_table
from xml.dom import minidom
import os
import sys


def create_table(_table: str, columns: list) -> bool:

    database = get_database()
    if database is None:
        return False
    table = ET.SubElement(database, _table)

    for column in columns:
        if is_table(_table):
            print(f"Table {_table} already exists")
            return False 
        column.change_nullability()
        ET.SubElement(table, column.name, attrib={"type": str(column.type), "primary_key": str(column.primary_key), "nullable": str(column.nullable), "reference": str(column.reference)})

    # Create a string representation with formatting
    xml_str = ET.tostring(database, encoding="unicode")
    xml_str = xml_str.replace("\n", "")
    xml_formatted = minidom.parseString(xml_str).toprettyxml(indent="    ")  # You can adjust the indentation level
    with open(f"db/databases/{get_current_database()}.xml", "w") as file:
        file.write(xml_formatted)
        print(f"Table {_table} was selected successfully")
        return True


