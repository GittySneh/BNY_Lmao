import sqlite3

# Connect to the database
conn = sqlite3.connect('financial_data.db')
cursor = conn.cursor()

# Get all table names except the internal sqlite_sequence table
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = cursor.fetchall()

# Drop all tables except sqlite_sequence
for table_name in tables:
    if table_name[0] != 'sqlite_sequence':  # Skip internal SQLite table
        cursor.execute(f"DROP TABLE IF EXISTS {table_name[0]};")
        print(f"Deleted table: {table_name[0]}")
    else:
        print("Skipped sqlite_sequence table.")

# Commit changes
conn.commit()

# Optionally reclaim space
cursor.execute("VACUUM;")
print("Database vacuumed to reclaim space.")

# Close the connection
conn.close()
