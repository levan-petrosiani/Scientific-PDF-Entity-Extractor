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

### 🛠️ Tech Stack

* Python 3.10+
* HuggingFace Transformers (`dslim/bert-base-NER`)
* PyMuPDF (`fitz`) for PDF text extraction
* SQLite3 for database storage
* JSON for structured data export

---

Would you also like help adding an example usage section, code snippets, or setup instructions?
