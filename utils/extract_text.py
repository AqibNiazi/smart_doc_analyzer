import io
import pdfplumber
from docx import Document

def extract_text(uploaded_file):
    raw = uploaded_file.read()
    name = uploaded_file.name.lower()

    if name.endswith(".pdf"):
        return extract_text_from_pdf(raw)
    elif name.endswith(".docx") or name.endswith(".doc"):
        return extract_text_from_docx(raw)
    elif name.endswith(".txt"):
        return raw.decode(errors="ignore")
    return None

def extract_text_from_pdf(file_bytes):
    text = []
    with pdfplumber.open(io.BytesIO(file_bytes)) as pdf:
        for page in pdf.pages:
            if page.extract_text():
                text.append(page.extract_text())
    return "\n".join(text)

def extract_text_from_docx(file_bytes):
    doc = Document(io.BytesIO(file_bytes))
    return "\n".join([p.text for p in doc.paragraphs if p.text])
