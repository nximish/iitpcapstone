import pandas as pd
import logging
from ingest import load_all_documents
from workflow import process_document

documents = load_all_documents("data")

records = []
for doc in documents:
    record = process_document(doc["doc_id"], doc["text"])
    if record is not None:
        row = record.model_dump()
        row["doc_id"] = doc["doc_id"]
        row["filename"] = doc["filename"]
        records.append(row)

report_df = pd.DataFrame(records)
report_df.to_csv("output/final_report.csv", index = False)

logging.info(f"Batch complete: {len(records)}/{len(documents)} documents processed successfully")