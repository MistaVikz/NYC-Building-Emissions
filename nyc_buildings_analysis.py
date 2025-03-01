from scripts.nyc_buildings_db import *

MIN_SQFT_RESIDENTIAL = 7294843
MIN_SQFT_WAREHOUSE = 467836
MIN_SQFT_FACTORIES = 62015
MIN_SQFT_GARAGES = 467836
MIN_SQFT_HOTELS = 729483
MIN_SQFT_HOSPITALS = 467836
MIN_SQFT_THEATERS = 62015
MIN_SQFT_STORES = 358208
MIN_SQFT_OFFICES = 620155

def main():
    # Connect to Database
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # REMOVE
    rows = cursor.execute(q_select).fetchall()
    [print(r) for r in rows]


if __name__ == '__main__':
    main()