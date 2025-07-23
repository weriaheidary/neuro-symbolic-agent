from datasets import load_dataset
from transformers import AutoTokenizer

from transformers import AutoModelForCausalLM, AutoTokenizer, TrainingArguments, Trainer
from peft import get_peft_model, LoraConfig, TaskType

from dotenv import load_dotenv
import os
from huggingface_hub import login

load_dotenv()

hf_token = os.getenv("HF_TOKEN")
login(token=hf_token)

model_name = "TinyLlama/TinyLlama-1.1B-Chat-v1.0"

tokenizer = AutoTokenizer.from_pretrained(model_name, token=hf_token)
model = AutoModelForCausalLM.from_pretrained(model_name, token=hf_token)

# Configure LoRA
lora_config = LoraConfig(
    task_type=TaskType.CAUSAL_LM,  # since it's a causal language model
    inference_mode=False,          # training mode
    r=8,                          # rank; adjust based on memory (typical 4-16)
    lora_alpha=32,                # LoRA scaling factor
    lora_dropout=0.1              # dropout rate
)

# Wrap the model with LoRA
model = get_peft_model(model, lora_config)


raw_dataset = load_dataset('json', data_files='./symbolic_finetuner/symbolic_gilgamesh_dataset.jsonl')['train']

def preprocess(example):
    prompt = f"Input: {example['text']}\nOutput:"
    completion = f" {example['label']}"
    full_text = prompt + completion
    tokenized = tokenizer(full_text, truncation=True, max_length=512)
    tokenized["labels"] = tokenized["input_ids"].copy()
    return tokenized

tokenized_dataset = raw_dataset.map(preprocess, remove_columns=["text", "label"])


training_args = TrainingArguments(
    output_dir="./tinyllama-lora-finetuned",
    per_device_train_batch_size=1,
    gradient_accumulation_steps=4,
    num_train_epochs=3,
    logging_steps=10,
    save_steps=500,
    save_total_limit=2,
    # evaluation_strategy="no",
    fp16=False,  # if supported by your GPU
    learning_rate=3e-4,  # typical for LoRA fine-tuning
)

trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=tokenized_dataset,
    tokenizer=tokenizer,
)

trainer.train()

model.save_pretrained("./tinyllama-lora-finetuned")
tokenizer.save_pretrained("./tinyllama-lora-finetuned")

