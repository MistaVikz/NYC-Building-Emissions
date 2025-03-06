## NYC Building Emissions Analysis
This project analyzes building emissions data for New York City. It includes scripts to filter and query the data, build scenarios, and print the results in a structured format.

### Project Structure
`nyc_buildings_analysis.py`: Main script to run the analysis.
`io.py:` Contains functions for data filtering and printing scenarios.
`scenario.py`: Contains functions for querying the database and building scenarios.

### Functions
- `main()`: Connects to the database, loads filtered data, builds scenarios, and prints the results.

- `get_filtered_data(cursor)`: Creates a view v_relevant in the database if it does not already exist. The view filters out buildings with certain `BuildingClass` values and selects specific columns.

- `print_scenario(scenario, sq_factor)`: Prints the scenario data as a DataFrame with additional information. The function builds a DataFrame from the scenario data, fills missing values with 0, converts the `'Number of Buildings'` column to integers, and adds a `'Building Class'` column. It then prints the DataFrame with a header indicating the scenario type.

- `query_sum(cursor, bc_filter, min_sqft, sq_factor = 0)`: Queries the database to get the sum of various metrics for buildings that meet the specified criteria.

- `build_scenario(cursor, sq_factor = 0)`: Builds a scenario by querying the database for all building classes and aggregating the results.

### Usage
Ensure you have the necessary database and data files in place.
Run the main script `nyc_buildings_analysis.py` to perform the analysis and print the results.

### Dependencies
- pandas
- sqlite3

Make sure to install the required dependencies before running the scripts.
