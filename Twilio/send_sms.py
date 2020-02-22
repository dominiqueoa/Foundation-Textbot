from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "AC6925242ba72859741e231862093599d0"
# Your Auth Token from twilio.com/console
auth_token  = "402f584311810577d63a1a9216f5c79a"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+14048607166", 
    from_="++12054486159",
    body="Hello from Python!")

print(message.sid)

