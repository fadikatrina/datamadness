import mysql.connector as connection
import pandas as pd

try:
    db = connection.connect(
        host="localhost",
        database="F1",
        user="root",
        passwd="Hausfahrrad123",
        use_pure=True
    )
    query = "SELECT * from circuits;"
    circuits_df = pd.read_sql(query, db)
    db.close()

except Exception as e:
    db.close()
    print(str(e))