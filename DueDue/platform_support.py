```python
import platform

# Shared dependencies
platforms = ["Windows", "macOS", "Linux"]

def check_platform():
    current_platform = platform.system()

    if current_platform in platforms:
        return True, current_platform
    else:
        return False, current_platform
```