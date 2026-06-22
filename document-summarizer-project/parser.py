# PDF/DOCX/TXT parsing logic placeholder

import fitz
from docx import Document


def parse_pdf(file_path):

    text = ""

    pdf = fitz.open(file_path)

    for page in pdf:
        text += page.get_text()

    return text


def parse_docx(file_path):

    doc = Document(file_path)

    text = "\n".join(
        para.text for para in doc.paragraphs
    )

    return text


def parse_txt(file_path):

    with open(
        file_path,
        "r",
        encoding="utf-8"
    ) as file:

        return file.read()


def extract_text(file_path):

    if file_path.endswith(".pdf"):
        return parse_pdf(file_path)

    if file_path.endswith(".docx"):
        return parse_docx(file_path)

    if file_path.endswith(".txt"):
        return parse_txt(file_path)

    return ""
