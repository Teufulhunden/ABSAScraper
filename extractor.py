import requests, sqlite3, os, pandas as pd
from datetime import date, timedelta


#forming the database
con = sqlite3.connect("ABSA.db")
cur = con.cursor()
cur.execute("""
    CREATE TABLE IF NOT EXISTS rawdata (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        review TEXT NOT NULL,
        rating TEXT NOT NULL,
        date TEXT NOT NULL
    )
""")
cur.execute("DELETE FROM rawdata")
cur.execute("DELETE FROM sqlite_sequence WHERE name = 'rawdata'")
con.commit()

#scraping from yelp
url = "https://yelp-scraper.omkar.cloud/businesses/reviews"
querystring = {"business":"clutch-city-cluckers-houston-10","sort_by":"newest","page_size":"49"}
headers = {"API-Key": os.getenv("omkar_api_key")}
data = requests.get(url, headers=headers, params=querystring).json()

simplified = [{"rating": r["rating"], "text": r["text"], "date": r["date"]} for r in data["reviews"]]

for r in data["reviews"]:
    if date.fromisoformat(r["date"]) >= date.today() - timedelta(days=365): #sees if the posts are more than a year old change with user settings
        cur.execute(
            "INSERT INTO rawdata (review, rating, date) VALUES (?, ?, ?)",
            (r.get("text", ""), r.get("rating", ""), r.get("date", ""))
        )

df = pd.read_sql('SELECT rating FROM rawdata', con)
df['rating'] = pd.to_numeric(df['rating'], errors='coerce')
avg = df['rating'].mean()
print(avg)

con.commit()
con.close()
