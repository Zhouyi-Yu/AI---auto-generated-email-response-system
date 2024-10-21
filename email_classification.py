import spacy

# Load spaCy's NLP model
nlp = spacy.load("en_core_web_sm")

def classify_email(content):
    doc = nlp(content)
    if "support" in doc.text.lower():
        return "Support Request"
    elif "pricing" in doc.text.lower():
        return "Sales Inquiry"
    elif "billing" in doc.text.lower():
        return "Billing Issue"
    else:
        return "General Inquiry"
