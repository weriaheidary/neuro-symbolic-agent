# For supervised fine-tuning of SBERT

from sentence_transformers import SentenceTransformer, losses, InputExample
from torch.utils.data import DataLoader
import json
import itertools
from pathlib import Path

# Step 1: Load your dataset
dataset_path = Path(__file__).parent / "symbolic_gilgamesh_dataset.json"
with open(dataset_path, "r") as f:
    examples = json.load(f)

# Step 2: Group by label
from collections import defaultdict
grouped = defaultdict(list)
for ex in examples:
    grouped[ex["label"]].append(ex["text"])

# Step 3: Create sentence pairs with same label
input_examples = []
for sentences in grouped.values():
    for a, b in itertools.combinations(sentences, 2):
        input_examples.append(InputExample(texts=[a, b], label=1.0))  # positive pair

# Step 4: DataLoader and model
train_dataloader = DataLoader(input_examples, shuffle=True, batch_size=8) # type: ignore
model = SentenceTransformer("all-MiniLM-L6-v2")

# Step 5: Train with cosine similarity loss
train_loss = losses.CosineSimilarityLoss(model)
model.fit(train_objectives=[(train_dataloader, train_loss)], epochs=4, warmup_steps=10)

# Step 6: Save fine-tuned model
output_path = Path(__file__).parent.parent / "neuro_agent/fine_tuned_sbert"
model.save(str(output_path))
print("Fine-tuned model saved.")

