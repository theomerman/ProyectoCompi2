import os

def is_database(database: str) -> bool:
    # return True if database exists (database is an xml file)
    return os.path.isfile(f"db/databases/{database}.xml")