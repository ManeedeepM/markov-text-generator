import os
import random
from collections import defaultdict

# Resolve project root directory safely (VS Code proof)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

INPUT_FILE = os.path.join(BASE_DIR, "data", "input.txt")
OUTPUT_FILE = os.path.join(BASE_DIR, "output", "generated_text.txt")


def load_text():
    if not os.path.exists(INPUT_FILE):
        raise FileNotFoundError("input.txt not found inside data folder")

    with open(INPUT_FILE, "r", encoding="utf-8") as file:
        words = file.read().lower().split()

    if len(words) < 2:
        raise ValueError("Input text must contain at least two words")

    return words


def build_markov_chain(words):
    chain = defaultdict(list)
    for i in range(len(words) - 1):
        chain[words[i]].append(words[i + 1])
    return chain


def generate_text(chain, length=30):
    current_word = random.choice(list(chain.keys()))
    result = [current_word]

    for _ in range(length - 1):
        next_words = chain.get(current_word)

        # ✅ Prevent IndexError
        if not next_words:
            break

        current_word = random.choice(next_words)
        result.append(current_word)

    return " ".join(result)


def save_output(text):
    os.makedirs(os.path.dirname(OUTPUT_FILE), exist_ok=True)
    with open(OUTPUT_FILE, "w", encoding="utf-8") as file:
        file.write(text)


def main():
    words = load_text()
    chain = build_markov_chain(words)
    generated_text = generate_text(chain, 40)
    save_output(generated_text)

    print("✅ Text Generated Successfully!\n")
    print(generated_text)


if __name__ == "__main__":
    main()
