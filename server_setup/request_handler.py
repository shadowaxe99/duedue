```python
from flask import Flask, request, jsonify
import json
from ai_model_development.model_finetuning import generate_article

app = Flask(__name__)

@app.route('/generate', methods=['POST'])
def handle_request():
    data = request.get_json()
    seed = data.get('seed', '')
    prompt = data.get('prompt', '')
    
    try:
        article_data = generate_article(seed, prompt)
        response_data = {
            'status': 'success',
            'article_data': article_data
        }
    except Exception as e:
        response_data = {
            'status': 'error',
            'message': str(e)
        }
    
    return jsonify(response_data)

if __name__ == '__main__':
    app.run(host=server_address, port=5000)
```