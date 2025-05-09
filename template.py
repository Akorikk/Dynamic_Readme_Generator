import os 
from pathlib import Path 
import logging


logging.basicConfig(level=logging.INFO, format="[%(asctime)s]:%(message)s:")


list = [
    f"src/__init__.py",
    f"src/helper.py",
    ".env",
    "requirements.txt",
    "setup.py",
    "app.py",
    "research/trails.ipynb",
]

for filepath in list:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)


    if filedir !="":
        os.makedirs(filedir, exist_ok=True)
