from controllers.validations.get_database import get_database
from controllers.validations.get_table import get_table
def add_column(table_name, column_name, column_type) -> tuple:
    database, err = get_database()
    if err:
        return None, err
    table = database.get_table(table_name)
    