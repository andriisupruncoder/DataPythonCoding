import pandas as pd
import json

df = pd.DataFrame({
    "File": ["F1", "F1", "F2", "F3"],
    "Hour": [1, 2, 1, 1],
})

# Convert the DataFrame to a JSON string
json_string = json.dumps(df.to_json(orient="records"))

# Write the JSON string to a file
with open("output.json", "w") as f:
    f.write(json_string)