```python
from flask import Flask
from flask_cors import CORS

# Initialize Flask application
app = Flask(__name__)
CORS(app)

# Server address
server_address = "http://localhost:5000"

@app.route('/')
def home():
    return "AI Article Generator Server is running!"

if __name__ == '__main__':
    app.run(debug=True)
```