from transformers import pipeline
from setfit import AbsaModel
import os, sqlite3, pandas as pd

access_token = os.getenv("HF_token_key")

model = AbsaModel.from_pretrained(
    "tomaarsen/setfit-absa-bge-small-en-v1.5-restaurants-aspect",
    "tomaarsen/setfit-absa-bge-small-en-v1.5-restaurants-polarity",
    token=access_token,
)

con = sqlite3.connect("ABSA.db")
reviews = pd.read_sql("SELECT review FROM rawdata", con)

preds = model.predict(reviews['review'].tolist())

for i in preds:
    print(i)

    

