import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QLabel, QPushButton, QTextEdit, QFileDialog
)
from extractor import extract_text_from_pdf, extract_entities
from storage import save_to_json, save_to_db

class PDFEntityApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Scientific PDF AI Extractor")
        self.setGeometry(100, 100, 700, 500)

        layout = QVBoxLayout()

        self.label = QLabel("Upload a scientific PDF to analyze entities")
        layout.addWidget(self.label)

        self.text_output = QTextEdit()
        self.text_output.setReadOnly(True)
        layout.addWidget(self.text_output)

        self.upload_btn = QPushButton("Upload PDF")
        self.upload_btn.clicked.connect(self.upload_pdf)
        layout.addWidget(self.upload_btn)

        self.save_btn = QPushButton("Save Results (JSON + DB)")
        self.save_btn.clicked.connect(self.save_results)
        layout.addWidget(self.save_btn)

        self.setLayout(layout)
        self.entities = []

    def upload_pdf(self):
        path, _ = QFileDialog.getOpenFileName(self, "Open PDF", "", "PDF Files (*.pdf)")
        if path:
            text = extract_text_from_pdf(path)
            self.entities = extract_entities(text)
            formatted = "\n".join([f"{e['word']} ({e['entity_group']}, {e['score']:.2f})" for e in self.entities])
            self.text_output.setText(formatted)

    def save_results(self):
        if self.entities:
            save_to_json(self.entities)
            save_to_db(self.entities)
            self.label.setText("✅ Results saved to JSON and SQLite DB!")
        else:
            self.label.setText("⚠️ No data to save. Please upload and extract first.")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = PDFEntityApp()
    win.show()
    sys.exit(app.exec_())
