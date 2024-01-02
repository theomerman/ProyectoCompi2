from controllers.validations.get_database import get_database
from controllers.validations.get_table import get_table
import xml.etree.ElementTree as ET
def select(_parameters, from_statement) -> tuple[str, str]:
    database, err = get_database()
    if err is not None:
        return None, err

    tables, err = get_tables(database, from_statement)
    if err is not None:
        return None, err
    

def get_tables(database: ET.Element, from_statement:list):
    tables = []
    unified_tables = [[]]
    if from_statement is None:
        return None, None
    for table_name in from_statement[0]:
        table, err = get_table(table_name, database )
        if err is not None:
            return None, err
        tables.append(table)
