MIN_SQFT_RESIDENTIAL = 7294843
MIN_SQFT_WAREHOUSES = 467836
MIN_SQFT_FACTORIES = 62015
MIN_SQFT_GARAGES = 467836
MIN_SQFT_HOTELS = 729483
MIN_SQFT_HOSPITALS = 467836
MIN_SQFT_THEATERS = 62015
MIN_SQFT_STORES = 358208
MIN_SQFT_OFFICES = 620155

RES_FILTER = '''(BuildingClass LIKE 'C%' OR BuildingClass LIKE 'D%' OR BuildingClass LIKE 'L%')'''
WARE_FILTER = '''(BuildingClass LIKE 'E%')'''
FAC_FILTER = '''(BuildingClass LIKE 'F%')'''
GAR_FILTER = '''(BuildingClass LIKE 'G%')'''
HOT_FILTER = '''(BuildingClass LIKE 'H%')'''
HOS_FILTER = '''(BuildingClass LIKE 'I%')'''
THEA_FILTER = '''(BuildingClass LIKE 'J%')'''
STORE_FILTER = '''(BuildingClass LIKE 'K%' OR BuildingClass LIKE 'P%')'''
OFF_FILTER = '''(BuildingClass LIKE 'O%')'''

WHERE_FILTERS = {RES_FILTER : MIN_SQFT_RESIDENTIAL,
                 WARE_FILTER : MIN_SQFT_WAREHOUSES,
                 FAC_FILTER : MIN_SQFT_FACTORIES,
                 GAR_FILTER : MIN_SQFT_GARAGES,
                 HOT_FILTER : MIN_SQFT_HOTELS,
                 HOS_FILTER : MIN_SQFT_HOSPITALS,
                 THEA_FILTER : MIN_SQFT_THEATERS,
                 STORE_FILTER : MIN_SQFT_STORES,
                 OFF_FILTER : MIN_SQFT_OFFICES}

def query_sum(cursor, bc_filter, min_sqft, sq_factor = 0):
    """
    Queries the database to get the sum of various metrics for buildings that meet the specified criteria.
    
    Args:
        cursor (sqlite3.Cursor): The database cursor to execute the SQL command.
        bc_filter (str): The filter condition for the building class.
        min_sqft (int): The minimum square footage required for the building class.
        sq_factor (float, optional): The square footage factor to adjust the minimum square footage. Defaults to 0.
    
    Returns:
        list: A list containing the adjusted minimum square footage and the sum of various metrics.
    """
    min_sqft_needed = min_sqft * sq_factor
    q_sum = f'''SELECT SUM(NumBuildings), SUM(KwHrYrElecSaving), SUM(LongShort2024HIGH), SUM(LongShort2030HIGH) FROM buildings 
        WHERE DOF >= {min_sqft_needed} AND {bc_filter}'''
    output = cursor.execute(q_sum).fetchall()
    output = list(output[0])
    output = [min_sqft_needed] + output
    return output

def build_threshold_scenario(cursor, sq_factor = 0):
    """
    Builds a scenario by querying the database for all building classes and aggregating the results.
    
    Args:
        cursor (sqlite3.Cursor): The database cursor to execute the SQL command.
        sq_factor (float, optional): The square footage factor to adjust the minimum square footage. Defaults to 0.
    
    Returns:
        list: A list of lists, where each inner list contains the results for a specific building class.
    """
    scenario = []
    # Use WHERE_FILTERS to query all building classes
    for filter, min_sqft in WHERE_FILTERS.items():
        result = query_sum(cursor,filter, min_sqft, sq_factor)
        scenario.append(result)
    return scenario
    