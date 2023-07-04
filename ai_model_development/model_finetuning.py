```python
import torch
from transformers import GPT2LMHeadModel, GPT2Config, GPT2Tokenizer

# Load the trained model
model_path = "../deliverables/ai_model.py"
trained_model = GPT2LMHeadModel.from_pretrained(model_path)

# Load the tokenizer
tokenizer = GPT2Tokenizer.from_pretrained('gpt2')

# Fine-tuning parameters
learning_rate = 1e-5
optimizer = torch.optim.Adam(trained_model.parameters(), lr=learning_rate)
criterion = torch.nn.CrossEntropyLoss()

# Fine-tuning the model
def fine_tune_model(model, tokenizer, dataset, epochs=1):
    model.train()
    for epoch in range(epochs):
        for step, batch in enumerate(dataset):
            inputs, labels = batch
            inputs = inputs.to('cuda')
            labels = labels.to('cuda')
            outputs = model(inputs, labels=labels)
            loss = outputs[0]
            loss.backward()
            optimizer.step()
            optimizer.zero_grad()
            print(f"Epoch: {epoch}, Loss:  {loss.item()}")

# Load the dataset
dataset_path = "../ai_model_development/dataset_preparation.py"
dataset = torch.load(dataset_path)

# Fine-tune the model
fine_tune_model(trained_model, tokenizer, dataset)

# Save the fine-tuned model
torch.save(trained_model.state_dict(), "../deliverables/ai_model.py")
```