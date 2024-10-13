import pandas as pd
import json

# Load the CSV file into a DataFrame
df = pd.read_csv('ff.csv')  # Replace 'your_file.csv' with the actual path to your CSV file

# Initialize an empty dictionary to store the results
singular_plural_dict = {}

# Loop through each row in the DataFrame
for index, row in df.iterrows():
    singular = row['singular']
    plural = row['plural']
    
    # Populate the dictionary with plural forms as keys
    singular_plural_dict[plural] = {
        "NOUN": singular  # Assuming all entries are nouns for this example
    }

# Display the resulting dictionary
print(singular_plural_dict)

# Save the dictionary to a JSON file named 'plurals.json'
with open('plurals.txt', 'w', encoding="utf-8") as json_file:
    json.dump(singular_plural_dict, json_file, indent=4)

print("Dictionary saved to plurals.json")
