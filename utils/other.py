def query_building_class(cursor):
    q_bc = '''SELECT BuildingClass, SUM(EmYr2024HIGH), SUM(LongShort2024HIGH), SUM(LongShort2030HIGH),
        SUM(EmYr2024LOW), SUM(LongShort2024LOW), SUM(LongShort2030LOW), SUM(KwHrYrElecSaving), SUM(TotYrEmRedVar2024LOW) FROM buildings 
        GROUP BY BuildingClass'''
    output = cursor.execute(q_bc).fetchall()
    output = [list(x) for x in output]
    return output

def query_building_class_sqft(cursor):
    q_bc_sqft = '''SELECT BuildingClass, DOF AS SQFT, SUM(EmYr2024HIGH), SUM(LongShort2024HIGH), SUM(LongShort2030HIGH),
        SUM(EmYr2024LOW), SUM(LongShort2024LOW), SUM(LongShort2030LOW), SUM(KwHrYrElecSaving), SUM(TotYrEmRedVar2024LOW) FROM buildings 
        GROUP BY BuildingClass, DOF'''
    output = cursor.execute(q_bc_sqft).fetchall()
    output = [list(x) for x in output]
    return output

def query_totals(cursor):
    q_totals = '''SELECT SUM(EmYr2024HIGH), SUM(LongShort2024HIGH), SUM(LongShort2030HIGH), SUM(EmYr2024LOW), 
        SUM(LongShort2024LOW), SUM(LongShort2030LOW), SUM(KwHrYrElecSaving), SUM(TotYrEmRedVar2024LOW) FROM buildings'''
    output = cursor.execute(q_totals).fetchall()
    output = [list(x) for x in output]
    return output