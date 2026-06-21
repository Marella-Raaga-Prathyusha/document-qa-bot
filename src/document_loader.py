import os
from pypdf import PdfReader
from docx import Document

def load_pdf(file_path):
    pages = []

    reader = PdfReader(file_path)

    for page_num, page in enumerate(reader.pages, start=1):
        text = page.extract_text()

        if text:
            pages.append({
                "text": text,
                "metadata": {
                    "source": os.path.basename(file_path),
                    "page": page_num
                }
            })

    return pages


def load_docx(file_path):
    doc = Document(file_path)

    text = "\n".join([p.text for p in doc.paragraphs])

    return [{
        "text": text,
        "metadata": {
            "source": os.path.basename(file_path),
            "page": 1
        }
    }]


def load_txt(file_path):

    with open(file_path,"r",encoding="utf-8") as f:
        text = f.read()

    return [{
        "text": text,
        "metadata": {
            "source": os.path.basename(file_path),
            "page": 1
        }
    }]