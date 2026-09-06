from pathlib import Path
from pypdf import PdfReader


# Healthcare PDF folder ka location
DOCUMENTS_PATH = Path("../data/healthcare_documents")


def load_pdfs():

    documents = []

    # Folder ke andar saare PDF files find karo
    for pdf_file in DOCUMENTS_PATH.glob("*.pdf"):

        print(f"Reading: {pdf_file.name}")

        reader = PdfReader(str(pdf_file))

        text = ""

        # PDF ki har page read karo
        for page in reader.pages:

            page_text = page.extract_text()

            if page_text:
                text += page_text + "\n"

        documents.append({
            "filename": pdf_file.name,
            "text": text
        })

    return documents