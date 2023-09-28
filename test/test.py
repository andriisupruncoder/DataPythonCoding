import pandas as pd

# Constants for configuration
feedback_data = {
    "Product ID": ["P001", "P002"],
    "Rating": [4, 5],
    "Feedback Text": ["Good quality but expensive.", "Loved it! Super fast delivery."],
    "Date": ["2021-07-01", "2021-07-02"],
    "Location": ["Online", "In-Store"],
    "Responded": ["Yes", "No"],
    "User Profile": ["Registered", "Guest"]
}

customer_data = {
    "Product ID": ["P001", "P002"],
    "Location": ["Online", "In-Store"],
    "Customer Name": ["Jane Smith", "John Doe"],
    "Email": ["jane.smith@example.com", "john.doe@example.com"]
}
JOIN_KEYS = ["Product ID", "Location"]
SELECTED_COLUMNS = ["Product ID", "Rating", "Feedback Text", "Date", "Location", "User Profile", "Customer Name", "Email"]

def merge_feedback_with_customer(feedback_data: dict, customer_data: dict) -> pd.DataFrame:
    """
    Merge feedback data with customer data based on Product ID and Location.
    
    Args:
    - feedback_data (dict): Dictionary containing feedback data.
    - customer_data (dict): Dictionary containing customer data.
    
    Returns:
    - pd.DataFrame: Merged data.
    """
    
    # Convert dictionaries to DataFrames
    feedback_df = pd.DataFrame(feedback_data)
    customer_df = pd.DataFrame(customer_data)
    
    # Join the datasets based on the specified keys
    merged_df = pd.merge(feedback_df, customer_df, on=JOIN_KEYS, how="inner")
    
    # Select the desired columns and return
    return merged_df[SELECTED_COLUMNS]

# Test the function with sample data
result_df = merge_feedback_with_customer(feedback_data, customer_data)
print(result_df)
