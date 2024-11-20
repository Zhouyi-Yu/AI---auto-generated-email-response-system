import spacy

# Load spaCy's NLP model
nlp = spacy.load("en_core_web_sm")

# Function to classify email content
def classify_email(content):
    """
    Classifies email content based on detected keywords using spaCy NLP.

    Args:
        content (str): The email content to classify.

    Returns:
        str: The classification of the email.
    """
    
    # Process the email content with spaCy
    # named entities (e.g., people, dates, organizations, money amounts).
    doc = nlp(content.lower())

    # Define keyword categories
    support_keywords = {"support", "help", "issue", "problem"}
    sales_keywords = {"pricing", "quote", "cost", "purchase"}
    billing_keywords = {"billing", "invoice", "payment", "charge"}

    # Check for keywords in the email content
    for token in doc:
        if token.lemma_ in support_keywords:
            return "Support Request"
        elif token.lemma_ in sales_keywords:
            return "Sales Inquiry"
        elif token.lemma_ in billing_keywords:
            return "Billing Issue"

    # Default classification if no keywords are found
    return "General Inquiry"


