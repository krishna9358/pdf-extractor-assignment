database = []

def add_invoice_to_database(file_path, text, features):
    database.append((file_path, text, features))

def get_database():
    return database
