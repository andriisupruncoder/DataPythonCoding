from google.cloud import bigquery

# Initialize a client for BigQuery Service
client = bigquery.Client()

# Define the SQL query
sql = """
SELECT 
  `Age Group` AS UserGroup,
  `Region`,
  `Device Type` AS Device,
  AVG(`Session Duration (seconds)`) AS AverageSessionDuration
FROM 
  `your_project_id.your_dataset_name.user_activity_logs`
GROUP BY
  UserGroup,
  Region,
  Device
ORDER BY
  UserGroup,
  Region,
  Device;
"""

# Run the query
query_job = client.query(sql)

# Print the results
for row in query_job:
    print(row)
