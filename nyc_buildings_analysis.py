import sqlite3
from utils.scenario import *
from utils.io import *

DB_PATH = 'data/nyc_buildings.db'

def main():
    # Load Filtered Data
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()       
    get_filtered_data(cursor)
    
    scenario = []
    build_scenario(cursor,scenario,1)
    print(scenario)
    
    # Cleanup
    conn.commit()
    conn.close()

if __name__ == '__main__':
    main()