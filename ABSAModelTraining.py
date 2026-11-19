from setfit import AbsaModel
from datasets import load_dataset
import os

model = AbsaModel.from_pretrained(
    "microsoft/deberta-v3-small",
    "microsoft/deberta-v3-base",
    spacy_model = "en_core_web_sm",
    token=os.getenv("HF_token_key")
)

dataset = load_dataset("jaimik69/Yelp-Restaurant-Dataset", split="train")