import os
import pdfplumber
import docx

# ============================
# Readers
# ============================

def read_txt(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        text = f.read()
    return text

def read_pdf(filepath):
    text = ""
    with pdfplumber.open(filepath) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + "\n"
    return text

def read_docx(filepath):
    doc = docx.Document(filepath)
    paragraphs = [p.text for p in doc.paragraphs]
    text = "\n".join(paragraphs)
    return text

# ============================
# Dispatcher
# ============================

def load_document(filepath):
    ext = os.path.splitext(filepath)[1].lower()

    try:
        if ext == ".txt":
            text = read_txt(filepath)
        elif ext == ".pdf":
            text = read_pdf(filepath)
        elif ext == ".docx":
            text = read_docx(filepath)
        else:
            raise ValueError(f"Unsupported file type: {ext}")
        return text

    except Exception as e:
        print(f"Failed to load {filepath}: {e}")
        return None

# ============================
# Batch loop
# ============================

def load_all_documents(data_dir):
    documents = []
    
    for filename in os.listdir(data_dir):
        ext = os.path.splitext(filename)[1].lower()
        if ext not in (".txt", ".pdf", ".docx"):
            continue

        filepath = os.path.join(data_dir, filename)
        text = load_document(filepath)

        if text is not None:
            doc_id = os.path.splitext(filename)[0]
            documents.append({"doc_id": doc_id, "filename": filename, "text":text})
            print(f"Loaded {filename}")
        else:
            print(f"Skipped {filename}")

    return documents

# ============================
# Manual Test
# ============================

if __name__ == "__main__":
    docs = load_all_documents("data")
    print(f"Loaded {len(docs)} documents")

