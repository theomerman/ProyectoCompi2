from xml.etree import ElementTree as ET
from controllers.validations.get_current_database import get_current_database
from controllers.validations.get_database import get_database
import os

def is_table(name: str) -> tuple:
    database, err = get_database()
    if err is not None:
        return None, err
    for table in database.find("tables"):
        if table.tag == name:
            return True, None
    return False, None