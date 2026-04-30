import requests
import pandas as pd

# NEW Working API - No key needed
url = "https://api.sportsdata.io/v3/nba/scores/json/Players"

print("Fetching data from API...")

# Using a free public JSON API instead
url = "https://jsonplaceholder.typicode.com/users"
response = requests.get(url)

print("Status Code:", response.status_code)

data = response.json()

# Extract Data
users = []
for user in data:
    users.append({
        "ID":       user["id"],
        "Name":     user["name"],
        "Username": user["username"],
        "Email":    user["email"],
        "City":     user["address"]["city"],
        "Company":  user["company"]["name"],
    })

# Clean Data
df = pd.DataFrame(users)
df.dropna(inplace=True)
df.drop_duplicates(inplace=True)

# Save to Excel
df.to_excel("api_data.xlsx", index=False)

print("Done! Data saved to api_data.xlsx")
print(df)