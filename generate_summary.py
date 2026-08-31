from llm_provider import get_llm
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

llm = get_llm()
parser = StrOutputParser()

summary_prompt = PromptTemplate(
    input_variables = ["customer_name", "complaint_category", "issue_description", "resolution_provided", "escalation_required", "overall_case_status"],
    template = (
        "Write a concise internal case summary for staff reviewing this customer complaint.\n"
        "Include: a brief case overview, the key issue, any action taken so far, the current status, "
        "and recommend next action.\n"
        "Only use the information given below - do not invent any details. \n\n"
        "Customer Name: {customer_name}\n"
        "Category: {complaint_category}\n"
        "Issue: {issue_description}\n"
        "Resolution Provided: {resolution_provided}\n"
        "Escalation Required: {escalation_required}\n"
        "Case Status: {overall_case_status}"
    )
)

summary_chain = summary_prompt | llm | parser

def generate_case_summary(case_record):
    summary_text = summary_chain.invoke({
        "customer_name": case_record.customer_name,
        "complaint_category": case_record.complaint_category,
        "issue_description": case_record.issue_description,
        "resolution_provided": case_record.resolution_provided,
        "escalation_required": case_record.escalation_required,
        "overall_case_status": case_record.overall_case_status
    })
    return summary_text

if __name__ == "__main__":
    from ingest import load_document
    from extract import extract_case_record

    text = load_document("data/complaint_001.txt")
    record = extract_case_record(text)
    summary = generate_case_summary(record)
    print(summary)