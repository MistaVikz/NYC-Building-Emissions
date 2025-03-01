from scripts.nyc_buildings_db import *
from utils.queries import *

def main():
    # Load Filtered Data
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()       
    view_filtered_data(cursor)

    # TESTING
    rows = cursor.execute("SELECT * FROM v_relevant").fetchall()
    [print(r) for r in rows]

    # Cleanup
    conn.commit()
    conn.close()

if __name__ == '__main__':
    main()