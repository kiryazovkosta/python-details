import os
import re

BASE_FILES_DIR = "files"
WORDS_FILE = "words.txt"
INPUT_FILE = "input.txt"
OUTPUT_FILE = "output.txt"

words_path = os.path.join(os.curdir, BASE_FILES_DIR, WORDS_FILE)
input_path = os.path.join(os.curdir, BASE_FILES_DIR, INPUT_FILE)
output_path = os.path.join(os.curdir, BASE_FILES_DIR, OUTPUT_FILE)

with open(words_path, "r") as words_file:
    words = words_file.read().lower().split()
with open(input_path, "r") as inputs_file:
    text = inputs_file.read()

matching = { }

for word in words:
    pattern = rf"\b{word}\b"
    result = re.findall(pattern, text, re.IGNORECASE)
    matching[word] = len(result)

with open(output_path, "w", newline="\n") as writer:
    for key, value in sorted(matching.items(), key = lambda item: -item[1]):
        writer.write(f"{key} - {value}\n")