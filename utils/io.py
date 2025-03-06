import pandas as pd

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

def print_scenario(scenario, sq_factor):
    """
    Prints the scenario data as a DataFrame with additional information.
    
    The function builds a DataFrame from the scenario data, fills missing values with 0, 
    converts the 'Number of Buildings' column to integers, and adds a 'Building Class' column.
    It then prints the DataFrame with a header indicating the scenario type.
    
    Args:
        scenario (list): A list of lists containing scenario data.
        sq_factor (float): The square footage factor to be displayed in the header.
    
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
    return
