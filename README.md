# Scientific-PDF-Entity-Extractor
### 🔍 What is it?

**Scientific PDF Entity Extractor** is a Python-based tool designed to automatically extract named entities (like scientific fields, organizations, and keywords) from academic PDF documents using a pre-trained NLP model. It helps researchers, students, and data scientists quickly identify and structure key terms from scientific literature.

---

### 🎯 Why we built it

Scientific papers often contain critical domain-specific terms buried in complex text. Manually identifying these entities is time-consuming. This project automates that process using modern **Natural Language Processing (NLP)** techniques, making it easier to:

* Build structured datasets from unstructured PDFs
* Classify and index papers by topics
* Accelerate literature reviews and academic research workflows

---

### ⚙️ How it works

1. **PDF Parsing**:
   We use `PyMuPDF` to extract raw text from uploaded scientific PDFs.

2. **Entity Recognition**:
   The extracted text is passed through a **HuggingFace `transformers` pipeline**, specifically the `dslim/bert-base-NER` model, which identifies relevant named entities like organizations, fields, methods, etc.

3. **Output Options**:

   * Entities and their confidence scores are shown in the console.
   * Results are saved in both **JSON** and **SQLite `.db`** formats for further use or analysis.

---

### 📁 File Structure

1. **`main.py`**
   The main entry point for the application. This script handles:

   * Initializing the NLP model and extracting text from the provided PDF files.
   * Running the Named Entity Recognition (NER) pipeline.
   * Saving the extracted entities to output formats like JSON and SQLite database.

2. **`extractor.py`**
   Contains functions related to the **extraction process**:

   * `extract_text_from_pdf`: Extracts raw text content from a given PDF file using PyMuPDF.
   * `extract_entities`: Processes the extracted text with the `dslim/bert-base-NER` model to identify and classify named entities.

3. **`storage.py`**
   Handles the **saving of results**:

   * `save_to_json`: Saves the identified entities and their details (including confidence scores) into a JSON file.
   * `save_to_db`: Saves the same data into an SQLite database for structured storage and querying.

5. **`README.md`**
   This file. It explains the purpose of the project, how to use it, and other relevant details (like setup instructions, file structure, etc.).

---

### 🛠️ Tech Stack

* Python 3.10+
* HuggingFace Transformers (`dslim/bert-base-NER`)
* PyMuPDF (`fitz`) for PDF text extraction
* SQLite3 for database storage
* JSON for structured data export


