def sort_data(data, columns, ascending=True):
    # Convert single column and order into list
    if not isinstance(columns, list):
        columns = [columns]
    if not isinstance(ascending, list):
        ascending = [ascending] * len(columns)

    # Check if the input data is a list of dictionaries (JSON)
    if isinstance(data, list) and isinstance(data[0], dict):
        sorted_data = sorted(data, key=lambda x: [x[col] if idx < len(ascending) and ascending[idx] else -x[col] if isinstance(x[col], (int, float)) else x[col] for idx, col in enumerate(columns)])
        return sorted_data
    # Check if the input data is a list of lists (table)
    elif isinstance(data, list) and isinstance(data[0], list):
        col_indices = [data[0].index(col) for col in columns]
        sorted_data = sorted(data[1:], key=lambda x: [x[col] if idx < len(ascending) and ascending[idx] else -x[col] if isinstance(x[col], (int, float)) else x[col] for idx, col in enumerate(col_indices)])
        return [data[0]] + sorted_data
    else:
        raise ValueError("Input data format not supported. Please provide a list of dictionaries or a list of lists.")

# Example usage for list of dictionaries:
data_dicts = [
    {"Product ID": "P001", "Rating": 4, "Feedback Text": "Good quality but expensive.", "Date": "2021-07-01", "Location": "Online", "Responded": "Yes", "User Profile": "Registered"},
    {"Product ID": "P002", "Rating": 5, "Feedback Text": "Loved it! Super fast delivery.", "Date": "2021-07-02", "Location": "In-Store", "Responded": "No", "User Profile": "Guest"},
    # Add more data here
]

sorted_data_dicts = sort_data(data_dicts, columns=["Rating", "Date"], ascending=[False, True])
print(sorted_data_dicts)
