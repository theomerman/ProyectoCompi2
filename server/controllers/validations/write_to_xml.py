from controllers.validations.get_current_database import get_current_database
from xml.etree import ElementTree as ET
from xml.dom import minidom
def write_to_xml(root) -> tuple[bool, str]:
    current_database, err = get_current_database()
    if err is not None:
        return None, err
    xml_str = ET.tostring(root, encoding="unicode")
    xml_str = xml_str.replace("\n", "")
    xml_formatted = minidom.parseString(xml_str).toprettyxml(indent="    ")  # You can adjust the indentation level
    with open(f"db/databases/{current_database}.xml", "w") as file:
        file.write(xml_formatted)
        return True, None