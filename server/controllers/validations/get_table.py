from controllers.validations.get_database import get_database
from xml.etree import ElementTree as ET

def get_table(table_name) -> ET.Element:
    database, err = get_database()
    if err is not None:
        return None, err
    for table in database:
        if table.tag == table_name:
            return table, None
    return None, f"Table {table_name} does not exist"
