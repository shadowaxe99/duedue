```python
import json
import xml.etree.ElementTree as ET
import markdown

supported_formats = ["xml", "json", "md"]

def read_file(file_path):
    file_extension = file_path.split('.')[-1]
    if file_extension not in supported_formats:
        raise Exception(f"Unsupported file format. Supported formats are {supported_formats}")

    with open(file_path, 'r') as file:
        content = file.read()

    if file_extension == 'json':
        return json.loads(content)
    elif file_extension == 'xml':
        return ET.fromstring(content)
    elif file_extension == 'md':
        return markdown.markdown(content)

def write_file(file_path, data):
    file_extension = file_path.split('.')[-1]
    if file_extension not in supported_formats:
        raise Exception(f"Unsupported file format. Supported formats are {supported_formats}")

    with open(file_path, 'w') as file:
        if file_extension == 'json':
            file.write(json.dumps(data, indent=4))
        elif file_extension == 'xml':
            file.write(ET.tostring(data).decode())
        elif file_extension == 'md':
            file.write(markdown.markdown(data))
```