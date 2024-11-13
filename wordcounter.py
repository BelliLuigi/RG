import PyPDF2
from collections import Counter
import re

def extract_text_from_pdf(pdf_path):
    text = ""
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        for page_num in range(len(reader.pages)):
            page = reader.pages[page_num]
            text += page.extract_text() + " "
    return text

def get_most_used_words(pdf_path, top_n=10):
    text = extract_text_from_pdf(pdf_path)
    # Remove punctuation and split by whitespace
    words = re.findall(r'\b\w+\b', text.lower())
    word_counts = Counter(words)
    # Return the most common words
    return word_counts.most_common(top_n)

# Example usage
pdf_path = 'main.pdf'  # replace with your PDF file path
top_words = get_most_used_words(pdf_path, top_n=100)
for word, count in top_words:
    print(f"{word}: {count}")

