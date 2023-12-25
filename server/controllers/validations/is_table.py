from xml.etree import ElementTree as ET
from controllers.validations.get_current_database import get_current_database
from controllers.validations.get_database import get_database
import os

def is_table(name: str) -> bool:
    if get_current_database() is None:
        return None
    if get_database() is None:
        return None
    database = get_database()

    for table in database:
        print(table.tag)
        if table.tag == name:
            return True