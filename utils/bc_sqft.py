def query_building_class(cursor):
    q_sum = f'''SELECT SUM(NumBuildings), SUM(KwHrYrElecSaving), SUM(LongShort2024HIGH), SUM(LongShort2030HIGH) FROM buildings 
        WHERE DOF >= 5'''
    output = cursor.execute(q_sum).fetchall()
    output = list(output[0])
    return output

def query_building_class_sqft(cursor):
    q_sum = f'''SELECT SUM(NumBuildings), SUM(KwHrYrElecSaving), SUM(LongShort2024HIGH), SUM(LongShort2030HIGH) FROM buildings 
        WHERE DOF >= 5'''
    output = cursor.execute(q_sum).fetchall()
    output = list(output[0])
    return output