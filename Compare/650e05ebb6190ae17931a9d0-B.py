import sqlite3

class CrudOperations:
    def __init__(self, db_file):
        self.db = sqlite3.connect(db_file)

    def create(self, table_name, data):
        """Create a new record in the database."""
        cursor = self.db.cursor()
        cursor.execute("INSERT INTO {} ({}) VALUES ({})".format(
            table_name,
            ",".join(data.keys()),
            ",".join(["?" for _ in data.keys()]),
        ), data)
        self.db.commit()

    def read(self, table_name, id):
        """Read a record from the database."""
        cursor = self.db.cursor()
        cursor.execute("SELECT * FROM {} WHERE id = ?".format(table_name), (id,))
        record = cursor.fetchone()
        return record

    def update(self, table_name, data, id):
        """Update a record in the database."""
        cursor = self.db.cursor()
        cursor.execute("UPDATE {} SET {} WHERE id = ?".format(
            table_name,
            ",".join(["{} = ?".format(key) for key in data.keys()]),
        ), data.values() + (id,))
        self.db.commit()

    def delete(self, table_name, id):
        """Delete a record from the database."""
        cursor = self.db.cursor()
        cursor.execute("DELETE FROM {} WHERE id = ?".format(table_name), (id,))
        self.db.commit()

# Example usage

crud = CrudOperations("database.db")

# Create a new record

crud.create("users", {"name": "John Doe", "age": 30})

# Read a record

record = crud.read("users", 1)

# Update a record

crud.update("users", {"age": 31}, 1)

# Delete a record

crud.delete("users", 1)