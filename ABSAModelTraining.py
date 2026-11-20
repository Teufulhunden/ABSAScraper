from setfit import AbsaModel, AbsaTrainer, TrainingArguments
from transformers import EarlyStoppingCallback
from datasets import load_dataset
import os

model = AbsaModel.from_pretrained(
    "sentence-transformers/all-MiniLM-L6-v2",
    "sentence-transformers/all-mpnet-base-v2",
    spacy_model = "en_core_web_sm",
    token=os.getenv("HF_token_key")
)

dataset = load_dataset("tomaarsen/setfit-absa-semeval-restaurants", split="train")
train_dataset = dataset.select(range(128))
eval_dataset = dataset.select(range(128, 256))
args = TrainingArguments(
    output_dir="models",
    num_epochs=5,
    batch_size=32,
    eval_strategy="steps",
    eval_steps=50,
    save_steps=50,
    load_best_model_at_end=True,
)

trainer = AbsaTrainer(
    model,
    args=args,
    train_dataset=train_dataset,
    eval_dataset=eval_dataset,
    callbacks=[EarlyStoppingCallback(early_stopping_patience=5)],
)
trainer.train()
model.save_pretrained("models/yelp-absa")