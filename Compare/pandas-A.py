import pandas as pd
import json

df = pd.DataFrame({
    "File": ["F1", "F1", "F2", "F3"],
    "Hour": [1, 2, 1, 1]
})

df_list = df.to_dict(orient="records")

json_string = json.dumps(df_list)

with open("output.json", "w") as f:
    f.write(json_string)
    
df.to_json("output.json", orient="records")