from llm_provider import get_llm
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

llm = get_llm()
parser = StrOutputParser()

email_prompt = PromptTemplate(
    input_variables = ["customer_name", "issue_description", "resolution_provided", "overall_case_status"],
    template = (
        "Write a professional customer service email responding to the complaint below.\n"
        "Address the customer by name, briefly summarise their issue in an empathetic tone, "
        "clearly state the resolution or current status, and close professionally.\n"
        "Only use the information given below - do not invent any details, promises or resolutions.\n\n"
        "Customer Name: {customer_name}\n"
        "Issue: {issue_description}\n"
        "Resolution Provided: {resolution_provided}\n"
        "Case Status: {overall_case_status}"
    )
)

email_chain = email_prompt | llm | parser

def generate_customer_email(case_record):
    email_text = email_chain.invoke({
        "customer_name": case_record.customer_name,
        "issue_description": case_record.issue_description,
        "resolution_provided": case_record.resolution_provided,
        "overall_case_status": case_record.overall_case_status
    })
    return email_text

if __name__ == "__main__":
    from ingest import load_document
    from extract import extract_case_record
    
    text = load_document("data/complaint_001.txt")
    record = extract_case_record(text)
    email = generate_customer_email(record)
    print(email)