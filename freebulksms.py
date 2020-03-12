
import requests
url = "https://www.fast2sms.com/dev/bulk"
for var in range(10):
#Enter your message after &message
#You can send to multiple numbers seperated by ,(COMMA).
#Change Flash = 1 for flash SMS
    payload = "sender_id=FSTSMS&message=YOUR MESSAGE HERE&language=english&route=p&numbers=9999999999&flash=0"
    headers = {
    'authorization': "3kiDrXsTv9baMGhClLWHEm75R4c20FoNdYn8IVSuQyJB1zfKpxhJYac4joqWfFM09tKAQePR8mUsbDyT",
    'Content-Type': "application/x-www-form-urlencoded",
    'Cache-Control': "no-cache",
    }
    var + 1;
    response = requests.request("POST", url, data=payload, headers=headers)
    print(response.text)
  # Coded by Kshitij 