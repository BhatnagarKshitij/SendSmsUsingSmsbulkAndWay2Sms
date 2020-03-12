from webbot import Browser
web = Browser()
web.go_to('https://www.way2sms.com/')
web.type('9999999999' , id='mobileNo')#Enter your phone number
web.type('YourPassword' , id='password')#Enter your Way2Sms Password
web.press(web.Key.ENTER) 
web.type('9999999999' , id='mobile')#Sender phone number
web.type('Text to send' , id='message')#Sender Text
web.click(tag='button' ,  id = 'sendButton')
