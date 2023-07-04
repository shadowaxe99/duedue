```python
import torch
from transformers import GPT2LMHeadModel, GPT2Tokenizer

class AIModel:
    def __init__(self, model_name='gpt2', trained_model_path='ai_model_development/trained_model.pth'):
        self.tokenizer = GPT2Tokenizer.from_pretrained(model_name)
        self.model = GPT2LMHeadModel.from_pretrained(model_name)
        self.load_model(trained_model_path)

    def load_model(self, model_path):
        self.model.load_state_dict(torch.load(model_path))

    def generate_article(self, prompt, max_length=500):
        inputs = self.tokenizer.encode(prompt, return_tensors='pt')
        outputs = self.model.generate(inputs, max_length=max_length, num_return_sequences=1)
        return self.tokenizer.decode(outputs[0])

trained_model = AIModel()
```