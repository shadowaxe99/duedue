```python
import os
import subprocess

def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

# List of necessary libraries
libraries = ["torch", "transformers", "flask", "requests"]

def main():
    for library in libraries:
        print(f"Installing {library}...")
        install(library)
        print(f"Installed {library}")

if __name__ == "__main__":
    main()
```