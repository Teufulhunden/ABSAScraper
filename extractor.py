import requests
import os

url = "https://yelp-scraper.omkar.cloud/businesses/reviews"

querystring = {"business":"clutch-city-cluckers-houston-10","sort_by":"newest","page_size":"49"}

headers = {"API-Key": os.getenv("omkar_api_key")}

response = requests.get(url, headers=headers, params=querystring).json()
data = response
list = []

simplified = [{"rating": r["rating"], "text": r["text"], "date": r["date"]} for r in data["reviews"]]

for r in data["reviews"]:
    list.append((r["rating"], r["text"], r["date"]))

print(list)