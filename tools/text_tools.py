# tools/text_tools.py

def word_count(text: str) -> dict:
    """Count words, characters, sentences in a text."""
    words = text.split()
    sentences = [s.strip() for s in text.replace("!", ".").replace("?", ".").split(".") if s.strip()]
    return {
        "words": len(words),
        "characters": len(text),
        "characters_no_spaces": len(text.replace(" ", "")),
        "sentences": len(sentences),
        "paragraphs": len([p for p in text.split("\n\n") if p.strip()]),
    }


def reverse_text(text: str) -> str:
    """Reverse a string."""
    return text[::-1]


def text_to_uppercase(text: str) -> str:
    """Convert text to uppercase."""
    return text.upper()


def text_to_lowercase(text: str) -> str:
    """Convert text to lowercase."""
    return text.lower()


def count_vowels(text: str) -> dict:
    """Count vowels and consonants in text."""
    vowels = set("aeiouAEIOU")
    vowel_count = sum(1 for c in text if c in vowels)
    consonant_count = sum(1 for c in text if c.isalpha() and c not in vowels)
    return {
        "vowels": vowel_count,
        "consonants": consonant_count,
        "letters_total": vowel_count + consonant_count,
    }


def count_character(text: str, character: str) -> dict:
    """Count how many times a specific character appears in a text (case-insensitive)."""
    text_lower = text.lower()
    char_lower = character.lower()
    count = text_lower.count(char_lower)
    positions = [i for i, c in enumerate(text_lower) if c == char_lower]
    return {
        "character": character,
        "count": count,
        "positions": positions,
        "text_length": len(text),
    }


def character_frequency(text: str) -> dict:
    """Return frequency of every character in the text, sorted by count."""
    from collections import Counter
    freq = Counter(c.lower() for c in text if c.strip())
    return {
        "frequency": dict(sorted(freq.items(), key=lambda x: x[1], reverse=True)),
        "unique_characters": len(freq),
        "total_characters": sum(freq.values()),
    }


def extract_emails(text: str) -> list[str]:
    """Extract all email addresses from a block of text."""
    import re
    pattern = r"[a-zA-Z0-9._%+\-]+@[a-zA-Z0-9.\-]+\.[a-zA-Z]{2,}"
    return re.findall(pattern, text)


def generate_password(length: int = 16, include_symbols: bool = True) -> str:
    """Generate a random secure password."""
    import random
    import string
    chars = string.ascii_letters + string.digits
    if include_symbols:
        chars += "!@#$%^&*()-_=+"
    return "".join(random.choices(chars, k=length))
