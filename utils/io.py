import pandas as pd
import os
import datetime

BC_LIST = ['Residential', 'Warehouses', 'Factories', 'Garages', 'Hotels', 'Hospitals', 'Theaters', 'Stores', 'Offices']

def get_filtered_data(cursor):
    """
    Creates a view 'v_relevant' in the database if it does not already exist.
    
    The view filters out buildings with certain BuildingClass values and selects specific columns.
    
    Args:
        cursor (sqlite3.Cursor): The database cursor to execute the SQL command.
    
    Returns:
        None
    """
    v_relevant = '''CREATE VIEW IF NOT EXISTS v_relevant AS SELECT '10DIGITBBL', NumBuildings, BuildingClass, KwHrYrElecSaving, 
        LongShort2024HIGH, LongShort2030HIGH, DOF FROM buildings WHERE (BuildingClass NOT LIKE 'M%' AND BuildingClass NOT LIKE 'Y%' 
        AND BuildingClass NOT LIKE 'Q%' AND BuildingClass NOT LIKE 'W%' AND BuildingClass NOT LIKE 'S%' AND BuildingClass != 'R0')'''
    cursor.execute(v_relevant).fetchall()
    
    return 

def print_threshold(scenario, sq_factor, output_folder):
    """
    Prints the scenario data as a DataFrame with additional information and saves it to a CSV file.
    
    The function builds a DataFrame from the scenario data, fills missing values with 0, 
    converts the 'Number of Buildings' column to integers, and adds a 'Building Class' column.
    It then prints the DataFrame with a header indicating the scenario type and saves it to a CSV file.
    
    Args:
        scenario (list): A list of lists containing scenario data.
        sq_factor (float): The square footage factor to be displayed in the header.
        output_folder (str): The path to the folder where the CSV file will be saved.
    
    Returns:
        None
    """
    # Build Scenario Dataframe
    scen_cols = ['Min Sqft Needed','Number of Buildings', 'Total KW/H Savings', 'Long/Short 2024', 'Long/Short 2030']
    df_scen = pd.DataFrame(scenario, columns=scen_cols)
    df_scen.fillna(0,inplace=True)
    df_scen['Number of Buildings'] = df_scen['Number of Buildings'].astype(int)
    df_scen['Building Class'] = BC_LIST

    # Print Scenario Dataframe
    if(sq_factor == 0):
        print('Scenario (Baseline)')
    else:
        print(f'Scenario (Min Sqft Needed +{sq_factor * 100:.2f}%)')
    print('------------------------------------------------------------------------------------------------------------')
    print(df_scen)
    print('\n')

    # Create subdirectory for sqft_threshold
    threshold_dir = os.path.join(output_folder, 'SQFT-Threshold')
    os.makedirs(threshold_dir, exist_ok=True)

    # Save DataFrame to CSV
    csv_filename = f'sqft_threshold_{sq_factor * 100:.2f}%.csv'
    csv_filepath = os.path.join(threshold_dir, csv_filename)
    df_scen.to_csv(csv_filepath, index=False)
    print(f'Squarefoot Threshold Scenario saved to {csv_filepath}')

    return

def print_bc_sqft(bc_sqft, scen_cols, output_folder, out_name, filename):
    """
    Prints the building class square footage data as a DataFrame and saves it to a CSV file.
    
    The function builds a DataFrame from the building class square footage data
    and prints the DataFrame with a header indicating the scenario type.
    It then saves the DataFrame to a CSV file.
    """
    # Build BC Sqft Dataframe
    df_bc_sqft = pd.DataFrame(bc_sqft, columns=scen_cols)
    df_bc_sqft = df_bc_sqft.iloc[1:]

    # Print BC Sqft Dataframe
    print(f'{out_name}')
    print('------------------------------------------------------------------------------------------------------------')
    print(df_bc_sqft)
    print('\n')

    # Save DataFrame to CSV
    csv_filename = f'{filename}.csv'
    csv_filepath = os.path.join(output_folder, csv_filename)
    df_bc_sqft.to_csv(csv_filepath, index=False)
    print(f'{out_name} saved to {csv_filepath}')
    
    return

def create_scenario_folder(output_folder):
        # Create subdirectory for bc_sqft
    bc_sqft_dir = os.path.join(output_folder, "High-Low-KWHrs-TonnesPerYear")
    os.makedirs(bc_sqft_dir, exist_ok=True)
    
    return bc_sqft_dir

def create_output_folder():
    """
    Create an output folder with a timestamp and filters.

    Returns:
        str: The path to the created output folder.
    """
    # Get the current date and time and filters
    now = datetime.datetime.now()
    date_time = now.strftime("%Y%m%d_%H%M%S")
    folder_string = f"Scenario Output - {date_time}"

    # Get the current directory of the script
    current_dir = os.path.dirname(__file__)

    # Construct the path to the output directory
    output_dir = os.path.join(current_dir, '..', 'output')

    # Create a new folder with the timestamp and filters
    folder_name = os.path.join(output_dir, folder_string)
    os.makedirs(folder_name, exist_ok=True)

    return folder_name