import sqlite3
import csv 

db_path = 'data/nyc_buildings.db'
file_path = 'data/nyc_buildings_Jan2021.csv'
q_create_table = '''CREATE TABLE IF NOT EXISTS buildings
    (ID INT,BBL INT,ReportWaterData TEXT,Boro INT,Block INT,Lot INT,NumBuildings INT,TaxClass INT,BuildingClass TEXT,StreetNum INT,StreetName TEXT,ZipCode TEXT,
    Borough TEXT,DOF INT,PumpKwHrYearFixed REAL,PumpKwHrYearVar REAL,KwHrYrElecSaving REAL,EmYr2024LOW REAL,EmCap2024LOW REAL,LongShort2024LOW REAL,
    TotYrEmRedVar2024LOW REAL,EmCap2030LOW REAL,LongShort2030LOW REAL,EmYr2024HIGH REAL,EmCap2024HIGH REAL,LongShort2024HIGH REAL,TotYrEmRedVar2024HIGH REAL,
    EmCap2030HIGH REAL,LongShort2030HIGH REAL,TimeStamp TEXT)'''
q_insert = '''INSERT INTO buildings (ID, BBL, ReportWaterData, Boro, Block, Lot, NumBuildings, TaxClass, BuildingClass,
    StreetNum, StreetName, ZipCode, Borough, DOF, PumpKwHrYearFixed, PumpKwHrYearVar, KwHrYrElecSaving, EmYr2024LOW, EmCap2024LOW,
    LongShort2024LOW, TotYrEmRedVar2024LOW, EmCap2030LOW, LongShort2030LOW, EmYr2024HIGH, EmCap2024HIGH, LongShort2024HIGH,
    TotYrEmRedVar2024HIGH, EmCap2030HIGH, LongShort2030HIGH, TimeStamp) 
    VALUES (?, ?,?, ?,?, ?,?, ?,?, ?,?, ?,?, ?,?, ?,?, ?,?, ?,?, ?,?, ?,?, ?,?, ?,?, ?);'''
q_select = '''SELECT * FROM buildings LIMIT(10)'''

def main():    
    # Connect to Database
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Create Buildings table
    cursor.execute(q_create_table)

    # Load CSV into buildings table
    with open(file_path,'r') as f: 
        to_db = csv.reader(f)
        cursor.executemany(q_insert, to_db)

    # Print first 10 entries
    rows = cursor.execute(q_select).fetchall()
    [print(r) for r in rows]

    # Clean up
    conn.commit()
    conn.close()

if __name__ == '__main__':
    main()
