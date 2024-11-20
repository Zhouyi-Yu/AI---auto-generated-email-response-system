import sys
from azure.ai.textanalytics import TextAnalyticsClient
from azure.core.credentials import AzureKeyCredential
from openAIresponse import *
# from email_classification import *


# Set up the credentials and endpoint
endpoint = "https://emailreply.cognitiveservices.azure.com/"
API_KEY = open("Azure_API_KEY", "r").read().strip()
key = API_KEY

# Create a client using the credentials
credential = AzureKeyCredential(key)
text_analytics_client = TextAnalyticsClient(endpoint=endpoint, credential=credential)

# Define a function to authenticate and connect
def authenticate_client():
    return text_analytics_client

# Function for sentiment analysis
#Some Tips: The sentiment has to analyze a list(required by the Azure API?), so we have to keep the enumerate function, even there is one single string!
def sentiment_analysis(client, documents):
    try:
        response = client.analyze_sentiment(documents=documents)
        for idx, doc in enumerate(response):
            #Since we are 100% sure that we will only paste one element which is the email content, thus we will return the value in the first iteration
            return (
            f"Document {idx} has sentiment: {doc.sentiment}\n"
            f"Overall scores: positive={doc.confidence_scores.positive}, "
            f"neutral={doc.confidence_scores.neutral}, "
            f"negative={doc.confidence_scores.negative}"
            )
    except Exception as err:
        return(f"Encountered an error while analyzing sentiment:{err}")

# Authenticate the client
client = authenticate_client()

#Ask User to mannually input the email content as the IMAP module has issues
print("Please Copy and Paste your email content here and end with Ctrl+D(Linux) or Ctrl+Z(Windows) then press enter: ")
email_content = sys.stdin.read() #to deal with the multiple line input

# Example text documents to analyze
documents = [
   email_content
]

# Perform sentiment analysis and email classifiction
azure_score = sentiment_analysis(client, documents)
# classification = classify_email(email_content)

#Generate an approciate response with that:
autoResponse(email_content, azure_score)

