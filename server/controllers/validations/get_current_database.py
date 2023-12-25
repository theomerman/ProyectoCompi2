from xml.etree import ElementTree as ET
import os
def get_current_database():
    xml_file = f"db/database.xml"
    if not os.path.isfile(xml_file):
        print("file not found (database.xml)")
        return None
    current_database = ET.parse(xml_file)
    root = current_database.getroot()
    if root.text == "":
        print("No database selected")
        return None
    return root.text