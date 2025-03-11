def query_building_class(cursor):
    """
    Queries the database to get the sum of various metrics grouped by building class.
    
    Args:
        cursor (sqlite3.Cursor): The database cursor to execute the SQL command.
    
    Returns:
        list: A list of lists, where each inner list contains the results for a specific building class.
    """
    q_bc = '''SELECT BuildingClass, SUM(EmYr2024HIGH), SUM(LongShort2024HIGH), SUM(LongShort2030HIGH),
        SUM(EmYr2024LOW), SUM(LongShort2024LOW), SUM(LongShort2030LOW), SUM(KwHrYrElecSaving), SUM(TotYrEmRedVar2024LOW) FROM buildings 
        GROUP BY BuildingClass'''
    output = cursor.execute(q_bc).fetchall()
    output = [list(x) for x in output]
    return output

def query_building_class_sqft(cursor):
    """
    Queries the database to get the sum of various metrics grouped by building class and square footage.
    
    Args:
        cursor (sqlite3.Cursor): The database cursor to execute the SQL command.
    
    Returns:
        list: A list of lists, where each inner list contains the results for a specific building class and square footage.
    """
    q_bc_sqft = '''SELECT BuildingClass, DOF AS SQFT, SUM(EmYr2024HIGH), SUM(LongShort2024HIGH), SUM(LongShort2030HIGH),
        SUM(EmYr2024LOW), SUM(LongShort2024LOW), SUM(LongShort2030LOW), SUM(KwHrYrElecSaving), SUM(TotYrEmRedVar2024LOW) FROM buildings 
        GROUP BY BuildingClass, DOF'''
    output = cursor.execute(q_bc_sqft).fetchall()
    output = [list(x) for x in output]
    return output

def query_totals(cursor):
    """
    Queries the database to get the sum of various metrics for all buildings.
    
    Args:
        cursor (sqlite3.Cursor): The database cursor to execute the SQL command.
    
    Returns:
        list: A list containing the sum of various metrics for all buildings.
    """
    q_totals = '''SELECT SUM(NumBuildings), SUM(EmYr2024HIGH), SUM(LongShort2024HIGH), SUM(LongShort2030HIGH), SUM(EmYr2024LOW), 
        SUM(LongShort2024LOW), SUM(LongShort2030LOW), SUM(KwHrYrElecSaving), SUM(TotYrEmRedVar2024LOW) FROM buildings'''
    output = cursor.execute(q_totals).fetchall()
    output = [list(x) for x in output]
    return output