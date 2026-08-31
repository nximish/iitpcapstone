from llm_provider import get_llm
from schemas import CaseRecord
from langchain_core.prompts import PromptTemplate

llm = get_llm().with_structured_output(CaseRecord)

extract_prompt = PromptTemplate(
    input_variables = ["document_text"],
    template = (
        "You are processing a customer complaint document for a business workflow.\n"
        "Extract the required structured information from the document text below.\n"
        "Only use the information present in the text - do not invent or assume anything not stated.\n"
        "If a field is not mentioned in the text, use your best judgement based on the field's description.\n\n"
        "Document:\n{document_text}"
    )
)

extract_chain = extract_prompt | llm

def extract_case_record(document_text):
    record = extract_chain.invoke({"document_text": document_text})
    return record

if __name__ == "__main__":
    from ingest import load_document

    text = load_document("data/complaint_001.txt")
    record = extract_case_record(text)
    print(record) 