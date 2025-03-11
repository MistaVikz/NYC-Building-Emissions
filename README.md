## NYC Building Emissions Analysis
This project analyzes building emissions data for New York City. It includes scripts to filter and query the data, build scenarios, and print the results in a structured format.

### Project Structure
- `nyc_buildings_analysis.py`: Main script to run the analysis.
- `io.py`: Contains functions for data filtering and printing scenarios.
- `other_queries.py`: Contains additional query functions for the database.
- `threshold.py`: Contains threshold constants and functions for building threshold scenarios.

### Functions
`nyc_buildings_analysis.py`
   
- `main()`: Connects to the database, loads filtered data, builds scenarios, and prints the results.

`io.py`
    
- `get_filtered_data(cursor)`: Creates a view v_relevant in the database if it does not already exist. The view filters out buildings with certain BuildingClass values and selects specific columns.
    
- `print_threshold(scenario, BC_LIST, sq_factor, output_folder)`: Prints the scenario data as a DataFrame with additional information and saves it to a CSV file in its own subdirectory.
    
-   `print_bc_sqft(bc_sqft, scen_cols, output_folder, out_name, filename)`: Prints the building class square footage queries as DataFrames and saves then to  CSV files.

- `print_totals(totals_output, output_folder)`: Prints the summary totals query as a DataFrame and saves it to a CSV file.

- `create_scenario_folder(output_folder)`: Creates a subdirectory for building class square footage data within the output folder.

- `create_output_folder()`: Creates an output folder with a timestamp and filters.

`utils/scenario.py`

- `query_sum(cursor, bc_filter, min_sqft, sq_factor = 0)`: Queries the database to get the sum of various metrics for buildings that meet the specified criteria.

- `build_threshold_scenario(cursor, sq_factor = 0)`: Builds a scenario by querying the database for all building classes and aggregating the results.

`other_queries.py`

- `query_building_class(cursor)`: Queries the database to get the sum of various metrics grouped by building class.

- `query_building_class_sqft(cursor)`: Queries the database to get the sum of various metrics grouped by building class and square footage.

- `query_totals(cursor)`: Queries the database to get the sum of various metrics for all buildings.

### Usage
Ensure you have the necessary database and data files in place.
Run the main script `nyc_buildings_analysis.py` to perform the analysis and print the results.

### Dependencies
- pandas
- sqlite3

Make sure to install the required dependencies before running the scripts.
