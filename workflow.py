import os
import json
import logging
from extract import extract_case_record
from generate_email import generate_customer_email
from generate_summary import generate_case_summary

logging.basicConfig(level = logging.INFO, format = "%(asctime)s - %(levelname)s - %(message)s")

os.makedirs("output/structured_data",exist_ok = True)
os.makedirs("output/customer_emails",exist_ok = True)
os.makedirs("output/case_summaries",exist_ok = True)

def process_document(doc_id, text):
    try:
        record = extract_case_record(text)
        email = generate_customer_email(record)
        summary = generate_case_summary(record)

        with open(f"output/structured_data/{doc_id}.json", "w") as f:
            json.dump(record.model_dump(), f, indent = 2)
        with open(f"output/customer_emails/{doc_id}.txt", "w") as f:
            f.write(email)
        with open(f"output/case_summaries/{doc_id}.txt", "w") as f:
            f.write(summary)
        logging.info(f"Processed {doc_id} successfully")
        return record

    except Exception as e:
        logging.error(f"Failed to process {doc_id}: {e}")
        return None

if __name__ == "__main__":
    from ingest import load_document

    text = load_document("data/complaint_001.txt")
    result = process_document("complaint_001", text)
    print(result)