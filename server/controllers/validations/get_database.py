from xml.etree import ElementTree as ET
from controllers.validations.is_database import is_database 
from controllers.validations.get_current_database import get_current_database
import os

def get_database() -> ET.Element :
    if get_current_database() is None:
        return None  
    if is_database(get_current_database()):
        tree = ET.parse("db/databases/" + get_current_database() + ".xml")
        root = tree.getroot()
        return root
    else:
        print("Database does not exist")
        return None