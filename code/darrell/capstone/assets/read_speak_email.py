import win32com.client
import pyttsx3

outlook = win32com.client.Dispatch("Outlook.Application").GetNamespace("MAPI")
inbox = outlook.GetDefaultFolder(6)
messages = inbox.Items
message = messages.GetLast()


""" print("Sender: " + message.SenderName)
print("Subject: " + message.subject)
print("Email: " + message.body) """

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.setProperty('rate', 150)
engine.setProperty('volume', 0.6)
# print(voices[1].id)
engine.say("Hello, Darrell")
engine.say("You have an email from {}".format(message.SenderName))
engine.say("Subject: {}".format(message.subject))
engine.say("Email message: {}".format(message.body))
engine.runAndWait()
