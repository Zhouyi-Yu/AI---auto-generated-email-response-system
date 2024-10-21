import unittest
from email_classification import classify_email
from response_generator import generate_response

class TestEmailSystem(unittest.TestCase):

    def test_classify_email(self):
        # Test cases for classify_email function
        self.assertEqual(classify_email("I need support with my account"), "Support Request")
        self.assertEqual(classify_email("What are your pricing options?"), "Sales Inquiry")
        self.assertEqual(classify_email("I have a billing question."), "Billing Issue")
        self.assertEqual(classify_email("Just a general question."), "General Inquiry")

    def test_generate_response(self):
        # Test cases for generate_response function
        self.assertEqual(generate_response("Support Request", "Need help!"), 
                         "Thank you for reaching out to support. Our team will get back to you shortly.")
        self.assertEqual(generate_response("Sales Inquiry", "Tell me about your products."),
                         "Thank you for your interest in our products. Here is some information about our pricing...")
        self.assertEqual(generate_response("Billing Issue", "I have a billing problem."),
                         "We apologize for the inconvenience. Please provide your billing ID for further assistance.")
        self.assertEqual(generate_response("General Inquiry", "Just checking in."),
                         "Thank you for your email. We'll get back to you soon.")

if __name__ == '__main__':
    unittest.main()
