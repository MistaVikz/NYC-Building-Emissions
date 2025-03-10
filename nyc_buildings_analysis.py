import sqlite3
from utils.threshold import *
from utils.io import *

DB_PATH = 'data/nyc_buildings.db'
THRESHOLD_LIST = [0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1]

def main():
    # Load Filtered Data
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()       
    get_filtered_data(cursor)
    
    # Create Output Folder
    output_folder = create_output_folder()
    
    # Calculate and Print the Threshold Scenarios
    for t in THRESHOLD_LIST:
        scenario = build_threshold_scenario(cursor,1 + t)
        print_scenario(scenario, t, output_folder)

    # Do Building Class and BC/SQFT Queries

    # Cleanup
    conn.commit()
    conn.close()

if __name__ == '__main__':
    main()