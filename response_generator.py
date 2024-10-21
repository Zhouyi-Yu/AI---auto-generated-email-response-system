def generate_response(email_type, email_body):
    if email_type == "Support Request":
        return "Thank you for reaching out to support. Our team will get back to you shortly."
    elif email_type == "Sales Inquiry":
        return "Thank you for your interest in our products. Here is some information about our pricing..."
    elif email_type == "Billing Issue":
        return "We apologize for the inconvenience. Please provide your billing ID for further assistance."
    else:
        return "Thank you for your email. We'll get back to you soon."
