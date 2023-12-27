import datetime
from controllers.validations.get_table import get_table
from controllers.validations.get_database import get_database
from controllers.validations.write_to_xml import write_to_xml
from xml.etree import ElementTree as ET

def insert(table_name, columns, values):
    table, err = get_table(table_name)
    if err is not None:
        return None, err
    dictionary, err = get_dictionary(table, columns, values)
    if err is not None:
        return None, err
    item = new_item(dictionary)
    database, err = get_database()
    if err is not None:
        return None, err

    database.find(table_name).find("data_rows").append(item) 

    success, err = write_to_xml(database)
    if err is not None:
        return None, err
    return "Item inserted successfully", None

def get_dictionary (table, columns, values):
    if len(columns) != len(values):
        return None, "Error: The number of columns and values does not match"
    if len(columns) == 0:
        return None, "Error: No columns were specified"
    if len(values) > len(table):
        return None, "Error: Too many values were specified"

    dictionary = {}

    for i in range(len(columns)):
        dictionary[columns[i]] = values[i]

    tmp_columns = []

    for column in table:
        tmp_columns.append(column.tag)

    for column in dictionary:
        if column not in tmp_columns:
            return None, f"Error: Column {column} does not exist in table"
    
    for column in table:
        if column.tag == "data_rows":
            continue
        if column.tag not in dictionary:
            if column.attrib["nullable"] == "False":
                return None, f"Error: Column {column.tag} cannot be null"
            else:
                dictionary[column.tag] = "null"

    success, err = validate_types(table, dictionary)
    if err is not None:
        return None, err

    return dictionary, None

def new_item(dictionary):
    item = ET.Element("item")
    for key in dictionary:
        ET.SubElement(item, key).text = str(dictionary[key])
    return item
                
def validate_types(table: ET.Element ,dictionary):
    for key in dictionary:
        try:
            nvarchar = int(table.find(key).attrib["type"])
            if dictionary[key] == "null":
                continue
            if len(dictionary[key].replace("'","")) > nvarchar:
                return None, f"Error: Value {dictionary[key]} exceeds the maximum length of {nvarchar}"
        except:

            if table.find(key).attrib["type"] == "int":
                try:
                    int(dictionary[key])
                except:
                    return None, f"Error: Value {dictionary[key]} is not an integer"
            elif table.find(key).attrib["type"] == "decimal":
                try:
                    float(dictionary[key])
                except:
                    return None, f"Error: Value {dictionary[key]} is not a decimal"
            elif table.find(key).attrib["type"] == "date":
                try:
                    datetime.datetime.strptime(dictionary[key].replace("'",""), '%Y-%m-%d')
                except:
                    return None, f"Error: Value {dictionary[key]} is not a date"
    return True, None
        # print(table.find(key),table.find(key).attrib["type"],dictionary[key])