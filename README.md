# USAID-Project
This is a prototype of a potential product for USAID. We believe they may be interested in a text based flash card system to reach technologically challenged areas.

## Getting Started
1. Pull from this repository so that you have all of the necessary files. From there, follow the tutorial found at this link so that you have the correct versions of Python, PIP, and virtualenv installed: https://docs.python-guide.org/dev/virtualenvs/. Once those are installed, create a new environment titled "USAID" and run the following commands separately: `source USAID/bin/activate` and `python3 -m pip install -r requirements.txt`.

2. Follow the Twilio Python quickstart tutorial so that you have Node.js installed correctly: https://www.twilio.com/docs/sms/quickstart/python

3. From within your "USAID" environment, run `python3 run.py` in one terminal, and in a second terminal you want to execute `twilio phone-numbers:update "+12054486159" --sms-url="http://localhost:5000/sms"`. These two commands create a Python Flask server and create a webhook to the server respectively. Once these two things are running locally, you can text the following number and receive automated replies: 1205-448-6159
