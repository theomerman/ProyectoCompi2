from xml.etree import ElementTree as ET
from controllers.validations.is_database import is_database 
from controllers.validations.get_current_database import get_current_database

def get_database() -> tuple[ET.Element, str]:
    current_database, err = get_current_database()
    if err is not None:
        return None, err
    
    if is_database(current_database):
        tree = ET.parse("db/databases/" + current_database + ".xml")
        root = tree.getroot()
        return root, None
    else:
        return None, f"Database {current_database} does not exists"