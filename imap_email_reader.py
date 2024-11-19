import imaplib
import email
from email.header import decode_header

# Your credentials
imap_server = "imap.gmail.com"
email_user = "jookenblue1997@gmail.com"
email_pass = "LA5BMbDkGMdJsUme"  # App-specific password

try:
    # Connect to the IMAP server
    imap = imaplib.IMAP4_SSL(imap_server, 993)
    print("Connected to IMAP server.")

    # Log in to the email account
    imap.login(email_user, email_pass)
    print("Logged in successfully.")

    # Select the mailbox (e.g., INBOX)
    status, mailbox_info = imap.select("INBOX")
    if status != "OK":
        print(f"Failed to select mailbox: {mailbox_info}")
        exit()
    print("Mailbox selected successfully.")

    # Search for all emails
    status, messages = imap.search(None, "ALL")
    if status != "OK":
        print("Failed to search for emails.")
        exit()

    # Convert the result to a list of email IDs
    email_ids = messages[0].split()

    if not email_ids:
        print("No emails found in the inbox.")
    else:
        print(f"Found {len(email_ids)} emails.")
        # Fetch the latest email
        latest_email_id = email_ids[-1]
        status, msg_data = imap.fetch(latest_email_id, "(RFC822)")

        for response_part in msg_data:
            if isinstance(response_part, tuple):
                # Parse the email
                msg = email.message_from_bytes(response_part[1])

                # Decode the subject
                subject, encoding = decode_header(msg["Subject"])[0]
                if isinstance(subject, bytes):
                    subject = subject.decode(encoding if encoding else "utf-8")
                print("Subject:", subject)

                # Print the sender
                print("From:", msg.get("From"))

                # Extract the email body
                if msg.is_multipart():
                    for part in msg.walk():
                        content_type = part.get_content_type()
                        if content_type == "text/plain" and not part.get("Content-Disposition"):
                            try:
                                body = part.get_payload(decode=True).decode("utf-8")
                                print("Body:", body)
                            except Exception as e:
                                print("Could not decode body:", e)
                            break
                else:
                    try:
                        body = msg.get_payload(decode=True).decode("utf-8")
                        print("Body:", body)
                    except Exception as e:
                        print("Could not decode body:", e)

    # Close the mailbox and logout
    imap.close()
    imap.logout()

except imaplib.IMAP4.error as imap_error:
    print("IMAP Error:", imap_error)
except Exception as e:
    print("An error occurred:", e)
