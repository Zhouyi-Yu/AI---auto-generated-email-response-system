import imaplib
import email
from email.header import decode_header
from email_classification import classify_email
from response_generator import generate_response

def fetch_emails():
    mail = imaplib.IMAP4_SSL("imap.gmail.com")
    mail.login("zhukenblue@gmail.com", "Jookenblue@0711")
    mail.select("inbox")

    status, messages = mail.search(None, "ALL")
    email_ids = messages[0].split()

    for email_id in email_ids:
        status, msg_data = mail.fetch(email_id, "(RFC822)")
        
        for response_part in msg_data:
            if isinstance(response_part, tuple):
                msg = email.message_from_bytes(response_part[1])
                subject = decode_header(msg["Subject"])[0][0]
                sender = msg.get("From")
                email_body = get_email_body(msg)

                # Classify email and respond
                email_type = classify_email(email_body)
                response = generate_response(email_type, email_body)
                print(f"From: {sender}\nSubject: {subject}\nBody: {email_body}\nResponse: {response}\n")
                
def get_email_body(msg):
    if msg.is_multipart():
        for part in msg.walk():
            if part.get_content_type() == "text/plain":
                return part.get_payload(decode=True).decode()
    return msg.get_payload(decode=True).decode()

def test_email_processing():
    # Simulate fetching an email
    test_email_body = "I have a question about billing."
    test_email_type = classify_email(test_email_body)
    response = generate_response(test_email_type, test_email_body)
    
    print("Test Email Body:", test_email_body)
    print("Classified Email Type:", test_email_type)
    print("Generated Response:", response)

if __name__ == '__main__':
    fetch_emails()
    test_email_processing()  # Call the test function here

