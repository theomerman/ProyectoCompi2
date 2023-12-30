import xml.etree.ElementTree as ET
from xml.dom import minidom
from controllers.validations.is_database import is_database

def create_database(name):
    if is_database(name):
        return None, f"Database {name} already exists"
    root = ET.Element(name)
    ET.SubElement(root, "tables")
    ET.SubElement(root, "stored_procedures")
    ET.SubElement(root, "functions")
    # Create a string representation with formatting
    xml_str = ET.tostring(root, encoding="unicode")
    xml_formatted = minidom.parseString(xml_str).toprettyxml(indent="    ")  # You can adjust the indentation level
    with open(f"db/databases/{name}.xml", "w") as file:
        file.write(xml_formatted)
        return f"Database {name} was created successfully", None