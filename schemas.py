from pydantic import BaseModel, Field
from typing import Literal

class CaseRecord(BaseModel):
    customer_name: str = Field(..., description = "Full name of the customer, as it appears in the document.")
    email: str = Field(..., description = "Customer's email address, as it appears in the document.")
    phone_number: str = Field(..., description = "Customer's phone number, as it appears in the document.")
    complaint_category: str = Field(..., description = "Category of the complaint, e.g. billing, product defect, service delay, access.")
    issue_description: str = Field(..., description = "A concise summary of the customer's issue, based only on the document text.")
    resolution_provided: str = Field(..., description = "Any resolution, refund, or action the business has actually already provided or agreed to, based on the document. Do NOT include what the customer is requesting or hoping for — if the document only shows a request with no business action taken yet, say 'No resolution provided yet.'")
    complaint: Literal["Yes", "No"] = Field(..., description = "Whether this document is actually a customer complaint.")
    escalation_required: Literal["Yes", "No"] = Field(..., description = "Whether this case requires escalation to a higher support tier.")
    supporting_document_available: Literal["Yes", "No"] = Field(..., description = "Whether the document mentions any supporting documents or attachments.")
    overall_case_status: str = Field(..., description = "Current status of the case, e.g. Resolved, Pending, Escalated, Closed.")
