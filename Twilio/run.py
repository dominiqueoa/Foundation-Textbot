# /usr/bin/env python
# Download the twilio-python library from twilio.com/docs/libraries/python
from flask import Flask, request, redirect
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)
flashCards = {"A": ("term1", "definition1"), "B" : ("term2", "definition2"), "C": ("term3", "definition3"), "D": ("term4", "definition4")}

@app.route("/sms", methods=['GET', 'POST'])
def incoming_SMS():
    """Respond to incoming messages with a friendly SMS."""
    # Start our response
    resp = MessagingResponse()
    body = request.values.get('Body', None)
    # Add a message

    if body in flashCards:
    	resp.message(flashCards[body][0] + ": " + flashCards[body][1])
    else:
    	resp.message("Hello! Welcome to Eko's SMS Flashcards! Please enter A, B, C, or D to see some of our terms")

    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)

