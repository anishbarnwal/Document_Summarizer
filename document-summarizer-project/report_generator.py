import os
import pandas as pd

from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer
)

from reportlab.lib.styles import getSampleStyleSheet


def generate_csv(data):

    os.makedirs("reports", exist_ok=True)

    df = pd.DataFrame(data)

    csv_path = "reports/document_summary.csv"

    df.to_csv(csv_path, index=False)

    return csv_path


def generate_pdf(data):

    pdf_path = "reports/document_summary.pdf"

    pdf = SimpleDocTemplate(pdf_path)

    styles = getSampleStyleSheet()

    content = []

    for row in data:

        content.append(
            Paragraph(
                f"<b>{row['file_name']}</b>",
                styles["Heading2"]
            )
        )

        content.append(
            Paragraph(
                row["summary"],
                styles["BodyText"]
            )
        )

        content.append(Spacer(1, 12))

    pdf.build(content)

    return pdf_path