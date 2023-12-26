from controllers.validations.get_database import get_database
from xml.etree import ElementTree as ET

def get_table(table_name) -> ET.Element:
    database = get_database()
    if database is None:
        return None
    for table in database:
        if table.tag == table_name:
            return table
    print(f"Table {table_name} does not exist")
    return None
