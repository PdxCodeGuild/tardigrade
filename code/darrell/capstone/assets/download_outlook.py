from pathlib import Path
import win32com.client
import xlsxwriter
import re

output_dir = Path.cwd() / "Output"
output_dir.mkdir(parents=True, exist_ok=True)

outlook = win32com.client.Dispatch("Outlook.Application").GetNameSpace("MAPI")
inbox = outlook.GetDefaultFolder(6)

messages = inbox.Items


workbook = xlsxwriter.Workbook("OutlookToExcel.xlsx")
worksheet = workbook.add_worksheet("Outlook_Email")

worksheet.write(0, 0, "#")
worksheet.write(0, 1, "Subject")
worksheet.write(0, 2, "Sender")
worksheet.write(0, 3, "SenderEmailAddress")
worksheet.write(0, 4, "Date")
worksheet.write(0, 5, "Unread")
worksheet.write(0, 6, "CC")
worksheet.write(0, 7, "Email")


for index, message in enumerate(messages):
    subject = message.Subject
    sender = message.sender
    sender_address = message.SenderEmailAddress
    date = message.SentOn
    unread = message.UnRead
    cc = message.CC
    body = message.body
    attachments = message.Attachments
    worksheet.write(index+1, 0, str(index))
    worksheet.write(index+1, 1, subject)
    worksheet.write(index+1, 2, str(sender))
    worksheet.write(index+1, 3, str(sender_address))
    worksheet.write(index+1, 4, date.replace(tzinfo=None))
    worksheet.write(index+1, 5, unread)
    worksheet.write(index+1, 6, str(cc))
    worksheet.write(index+1, 7, body)

workbook.close()
