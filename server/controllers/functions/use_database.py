import xml.etree.ElementTree as ET
from xml.dom import minidom
from controllers.validations.is_database import is_database
import os
def use_database(name) -> tuple:
    if not is_database(name):
        return None, f"Database {name} does not exist"
    
    root = ET.Element("database")
    root.text = name
    # Create a string representation with formatting
    xml_str = ET.tostring(root, encoding="unicode")
    xml_formatted = minidom.parseString(xml_str).toprettyxml(indent="    ")  # You can adjust the indentation level
    with open(f"db/database.xml", "w") as file:
        file.write(xml_formatted)
        return f"Database {name} was selected successfully", None

