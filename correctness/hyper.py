import tableauhyperapi as th

# Connect to the Hyper file
with th.Connection('my_data.hyper') as connection:
    # Get the table definition
    table_definition = connection.catalog.get_table_definition('Extract')

    # Create a Hyper API cursor
    cursor = connection.cursor()

    # Execute the query to fetch the first few rows
    cursor.execute_query('SELECT * FROM Extract LIMIT 10')

    # Retrieve the results
    results = cursor.fetchall()

    # Print the first few rows
    for row in results[:5]:
        print(row)