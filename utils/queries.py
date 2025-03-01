MIN_SQFT_RESIDENTIAL = 7294843
MIN_SQFT_WAREHOUSES = 467836
MIN_SQFT_FACTORIES = 62015
MIN_SQFT_GARAGES = 467836
MIN_SQFT_HOTELS = 729483
MIN_SQFT_HOSPITALS = 467836
MIN_SQFT_THEATERS = 62015
MIN_SQFT_STORES = 358208
MIN_SQFT_OFFICES = 620155

def view_filtered_data(cursor):
    v_relevant = '''CREATE VIEW IF NOT EXISTS v_relevant AS SELECT '10DIGITBBL', NumBuildings, BuildingClass, KwHrYrElecSaving, LongShort2024HIGH, LongShort2030HIGH, DOF 
        FROM buildings WHERE (BuildingClass NOT LIKE '%M%' AND BuildingClass NOT LIKE '%Y%' AND BuildingClass NOT LIKE '%Q%'
        AND BuildingClass NOT LIKE 'W%' AND BuildingClass NOT LIKE 'S%' AND BuildingClass != 'R0')'''
    cursor.execute(v_relevant).fetchall()
    return 
