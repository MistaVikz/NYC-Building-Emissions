
def get_filtered_data(cursor):
    v_relevant = '''CREATE VIEW IF NOT EXISTS v_relevant AS SELECT '10DIGITBBL', NumBuildings, BuildingClass, KwHrYrElecSaving, 
        LongShort2024HIGH, LongShort2030HIGH, DOF FROM buildings WHERE (BuildingClass NOT LIKE 'M%' AND BuildingClass NOT LIKE 'Y%' 
        AND BuildingClass NOT LIKE 'Q%' AND BuildingClass NOT LIKE 'W%' AND BuildingClass NOT LIKE 'S%' AND BuildingClass != 'R0')'''
    cursor.execute(v_relevant).fetchall()
    return 
