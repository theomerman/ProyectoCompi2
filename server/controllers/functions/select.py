from controllers.objects.Node import Node, traverse, copy_tree, set_values
from controllers.validations.get_database import get_database
from controllers.validations.get_table import get_table
import xml.etree.ElementTree as ET
def select(_parameters, from_statement:[[],Node]) -> tuple[str, str]:
    database, err = get_database()
    sorted_rows = []

    if err is not None:
        return None, err

    unified_tables,table_names, err = get_tables(database, from_statement)
    if err is not None:
        return None, err
    


    if len(from_statement) == 2:
        for row in unified_tables:
            try:
                tmp_tree = copy_tree(from_statement[1])
                set_values(tmp_tree, row, table_names)
                tmp = traverse(tmp_tree)
                # print(tmp)
                if tmp :
                    sorted_rows.append(row)
            except Exception as e:
               return None, str(e)
    else:
        for row in unified_tables:
            sorted_rows.append(row)

    print(len(sorted_rows))
    print(len(unified_tables))
    # print(table_names)
    # for row in sorted_rows:
    #     print(row)

    # for row in unified_tables:
    #     print(row)
    return "Select", None







def get_tables(database: ET.Element, from_statement:list):
    tables = [ET.Element]
    raw_tables = []
    unified_tables = [[]]
    column_names = []

    for table_name in from_statement[0]:
        # print(table_name)
        table, err = get_table(table_name, database )
        # print(type(table))
        if err is not None:
            return None, None, err
        tmp_table_two = []
        for column in table.find('columns'):
            column_names.append(table.tag+"."+column.tag)
        for item in table.find('data_rows'):
            tmp_table = []
            for tpm_column in item:
                tmp_table.append(tpm_column.text)
                # print(tpm_column.text)
            tmp_table_two.append(tmp_table) 
        raw_tables.append(tmp_table_two)
    

    unified_tables = cartesian_product_matrices(raw_tables)

    return unified_tables, column_names, None

def cartesian_product_matrices(matrices):

  if len(matrices) == 0:
    return []
  if len(matrices) == 1:
    return matrices[0]
  
  product = cartesian_product_matrices(matrices[1:])

  combined_product = []
  for row in matrices[0]:
    for element in product:
      combined_product.append(row + element)

  return combined_product