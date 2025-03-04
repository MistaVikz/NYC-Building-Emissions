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

def query_sum(cursor, bc_filter, min_sqft, sq_factor = 1):
    q_sum = f'''SELECT SUM(NumBuildings), SUM(KwHrYrElecSaving), SUM(LongShort2024HIGH), SUM(LongShort2030HIGH) FROM buildings 
        WHERE DOF >= {min_sqft} * {sq_factor} AND {bc_filter}'''
    output = cursor.execute(q_sum).fetchall()
    return output

def build_scenario(cursor, scenario, sq_factor = 1):
    # Use WHERE_FILTERS to query all building classes
    for filter, min_sqft in WHERE_FILTERS.items():
        res = query_sum(cursor,filter, min_sqft, sq_factor)
        result = list(res[0])
        scenario.append(result)
    return
    