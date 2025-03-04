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
    scenario_base = []
    build_scenario(cursor,scenario_base,1)
    scenario_10 = []
    build_scenario(cursor,scenario_10,1.1)
    scenario_20 = []
    build_scenario(cursor,scenario_20,1.2)
    scenario_30 = []
    build_scenario(cursor,scenario_30,1.3)
    scenario_40 = []
    build_scenario(cursor,scenario_40,1.4)
    scenario_50 = []
    build_scenario(cursor,scenario_50,1.5)
    scenario_60 = []
    build_scenario(cursor,scenario_60,1.6)
    scenario_70 = []
    build_scenario(cursor,scenario_70,1.7)
    scenario_80 = []
    build_scenario(cursor,scenario_80,1.8)
    scenario_90 = []
    build_scenario(cursor,scenario_90,1.9)
    scenario_100 = []
    build_scenario(cursor,scenario_100,2)

    # Cleanup
    conn.commit()
    conn.close()

if __name__ == '__main__':
    main()