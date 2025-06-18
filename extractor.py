import fitz  # PyMuPDF
from transformers import pipeline

# HuggingFace NER pipeline
ner_pipeline = pipeline("ner", model="dslim/bert-base-NER", grouped_entities=True)

def extract_text_from_pdf(path):
    doc = fitz.open(path)
    return "\n".join([page.get_text() for page in doc])

def extract_entities(text):
    # Truncate for performance if needed
    return ner_pipeline(text[:2000])
