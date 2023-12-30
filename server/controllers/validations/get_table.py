from controllers.validations.get_database import get_database
from xml.etree import ElementTree as ET

def get_table(table_name, _database = None) -> tuple[ET.Element, str]:
    database = _database
    if database is None:
        database, err = get_database()
        if err is not None:
            return None, err
    
    for table in database.find("tables"):
        if table.tag == table_name:
            return table, None
    return None, f"Error: Table {table_name} does not exist"
