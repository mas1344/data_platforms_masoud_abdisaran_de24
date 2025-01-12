import re
from pathlib import Path

print("this is path of this script")
data_path = Path(__file__).parent / "data"

print()


with open(data_path / "ml_text_raw.txt", 'r') as file:
    raw_text = file.read()


text_fixed_spacing = re.sub(r"\s+", " ",raw_text)

#similar code as in jupiter notebook for cleaning the rest of the text

print(text_fixed_spacing)

