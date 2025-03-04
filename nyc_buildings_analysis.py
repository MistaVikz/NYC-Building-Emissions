import sqlite3
from utils.scenario import *
from utils.io import *

DB_PATH = 'data/nyc_buildings.db'

def main():
    # Load Filtered Data
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()       
    get_filtered_data(cursor)
    
    # Get Scenario Results
    i=1
    while (i <= 2):
        scenario = build_scenario(cursor,i)
        print(scenario) # Replace with io function to create and print dataframes
        i+=0.1
    
    # Cleanup
    conn.commit()
    conn.close()

if __name__ == '__main__':
    main()