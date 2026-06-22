from fastapi import FastAPI
from fastapi.templating import Jinja2Templates
from fastapi.requests import Request

from drive_service import *
from parser import *
from summarizer import *
from report_generator import *

app = FastAPI()

templates = Jinja2Templates(
    directory="templates"
)

FOLDER_ID = "YOUR_FOLDER_ID"


@app.get("/")
def generate():

    files = list_files(FOLDER_ID)

    results = []

    for file in files:

        name = file["name"]

        if not (
            name.endswith(".pdf")
            or name.endswith(".docx")
            or name.endswith(".txt")
        ):
            continue

        path = download_file(
            file["id"],
            name
        )

        text = extract_text(path)

        summary = summarize_document(text)

        results.append({
            "file_name": name,
            "summary": summary
        })

    generate_csv(results)
    generate_pdf(results)

    return results


@app.get("/report")
def report(request: Request):

    files = list_files(FOLDER_ID)

    results = []

    for file in files:

        name = file["name"]

        if not (
            name.endswith(".pdf")
            or name.endswith(".docx")
            or name.endswith(".txt")
        ):
            continue

        path = download_file(
            file["id"],
            name
        )

        text = extract_text(path)

        summary = summarize_document(text)

        results.append({
            "file_name": name,
            "summary": summary
        })

    return templates.TemplateResponse(
        "index.html",
        {
            "request": request,
            "results": results
        }
    )