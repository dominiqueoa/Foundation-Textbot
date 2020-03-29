# /usr/bin/env python
# Download the twilio-python library from twilio.com/docs/libraries/python
from flask import Flask, request, redirect
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)
flashCards = {"1": ("Malade", "Feebar"), "2" : ("Parle", "Wax"), "3": ("Propre", "Cet")}

@app.route("/sms", methods=['GET', 'POST'])
def incoming_SMS():
    """Respond to incoming messages with a friendly SMS."""
    # Start our response
    resp = MessagingResponse()
    body = request.values.get('Body', None)
    # Add a message

    if body == "H":
    	resp.message("Eko Textbot is a flashcard based study tool over SMS. Use this bot to learn about new terms and definitions your teacher has chosen to share with you.")
    elif body in flashCards:
    	resp.message(flashCards[body][0] + ": " + flashCards[body][1])
    else:
    	resp.message("""Hello! Welcome to Eko's SMS Flashcards! Please enter a number from below to see a definition: 
    	1) Malade
    	2) Parle
    	3) Propre 

Send H for help
    		""")

    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)

