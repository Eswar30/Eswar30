from twilio.rest import Client 
 
account_sid = 'ACb59c43e86f121b4fbf3ff8cdf81a3a25' 
auth_token = 'e8bd830b5de3822d4e712c10530becb4' 
client = Client(account_sid, auth_token) 
 
message = client.messages.create( 
                              from_='whatsapp:+14155238886',  
                              body='Hello Honey',      
                              to='whatsapp:+918074611376' 
                          ) 
 
print(message.sid)