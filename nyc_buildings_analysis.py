import sqlite3
from utils.threshold import *
from utils.io import *
from utils.other import *

DB_PATH = 'data/nyc_buildings.db'

# Scenario Constants
THRESHOLD_LIST = [0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1]
BC_SQFT_COLUMNS = {1 : ['Building Class', 'EmYr2024HIGH', 'LongShort2024HIGH', 'LongShort2030HIGH',
              'EmYr2024LOW', 'LongShort2024LOW', 'LongShort2030LOW', 'KwHrYrElecSaving', 'TotYrEmRedVar2024LOW']
              , 2 : ['Building Class', 'SQFT', 'EmYr2024HIGH', 'LongShort2024HIGH', 'LongShort2030HIGH',
              'EmYr2024LOW', 'LongShort2024LOW', 'LongShort2030LOW', 'KwHrYrElecSaving', 'TotYrEmRedVar2024LOW']}
BC_SQFT_OUTPUT_NAMES = {1 : 'High Scenario / Low Scenario / KWHrs / TonnesPerYear by BuildingClass',
                        2 : 'High Scneario / Low Scenario / KWHrs / TonnesPerYear by BuildingClass and SQFT'}
BC_SQFT_FILE_NAMES = {1 : 'High-Low-KWHrs-TonnesPerYear-By-BuildingClass',
                 2 : 'High-Low-KWHrs-TonnesPerYear-By-BuildingClass-SQFT'}

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
        print_threshold(scenario, t, output_folder)

    # Create Subdirectory for BC_SQFT Queries
    scen_output_folder = create_scenario_folder(output_folder)
    
    # High Scenario/ Low Scenario / KWHrs /TonnesPerYear by BuildingClass
    bc_output = query_building_class(cursor)
    print_bc_sqft(bc_output, BC_SQFT_COLUMNS[1], scen_output_folder, BC_SQFT_OUTPUT_NAMES[1], BC_SQFT_FILE_NAMES[1])

    # High Scenario/ Low Scenario / KWHrs /TonnesPerYear by BuildingClass and SQFT
    bc_sqft_output = query_building_class_sqft(cursor)
    print_bc_sqft(bc_sqft_output, BC_SQFT_COLUMNS[2], scen_output_folder, BC_SQFT_OUTPUT_NAMES[2], BC_SQFT_FILE_NAMES[2])

    # Totals
    totals_output = query_totals(cursor)

    # Cleanup
    conn.commit()
    conn.close()

if __name__ == '__main__':
    main()