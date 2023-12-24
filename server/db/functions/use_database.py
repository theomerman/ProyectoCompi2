import xml.etree.ElementTree as ET
from xml.dom import minidom

def use_database(name):
    root = ET.Element("database")

    root.text = name
    # Create a string representation with formatting
    xml_str = ET.tostring(root, encoding="unicode")
    xml_formatted = minidom.parseString(xml_str).toprettyxml(indent="    ")  # You can adjust the indentation level
    with open(f"controllers/compiler/database.xml", "w") as file:
        file.write(xml_formatted)