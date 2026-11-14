from setfit import AbsaModel
import os

access_token = os.getenv("HF_token_key")
model = AbsaModel.from_pretrained(
    "tomaarsen/setfit-absa-bge-small-en-v1.5-restaurants-aspect",
    "tomaarsen/setfit-absa-bge-small-en-v1.5-restaurants-polarity",
    token=access_token,
)

# Run predictions on your scraped text
reviews = [
    "The food was great, but the venue is just way too busy.",
    "I always loved clutch city cluckers but they fucked me up. The employee promised  it was shellfish free when it wasnt and i had an allergic reaction. The food is usually good but i am not coming back. zero stars",
]

preds = model.predict(reviews)
print(preds)
