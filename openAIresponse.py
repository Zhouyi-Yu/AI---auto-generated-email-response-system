import openai

API_KEY = open("GPT_API_KEY", "r").read()
openai.api_key = API_KEY
chat_log = []

def autoResponse(email, azure_score):
    user_message = (
        f"The content of the email is: {email}. "
        f"The Azure sentiment score is {azure_score}, "
        "Please reply appropriately (with a title and contents)."
    )

    #put the user message in to the log, i.e. send this message
    chat_log.append({"role":"user", "content":user_message})

    #the response will be replied in a rather messy form with A LOT of extra information
    response = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages=chat_log
    )
    assistant_response = response['choices'][0]['message']['content']

    #therefore, strip for a better display
    print("Chat:"+ assistant_response.strip("\n").strip())
    chat_log.append({"role":"assistant", "content":assistant_response.strip("\n").strip()})