__author__ = 'Ramanan'
import smtplib
from email.message import EmailMessage
import csv
#Global variables
credit =500
new_credit =0
def maincall(UserName,Password,Subject,Body,filenamein,attach1,attach2):
    #print(user,pass67,sub67,body67,filenamein)
    filenamein=str(filenamein)
    attach1=str(attach1)
    attach2=str(attach2)    
    with open('D:/Bulk_Mail_Flask/DataBase/'+filenamein, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            length=len(row)
            for i in range (0,length,1):
                To_Email=(row[i])
                try:
                    #print("Try Loop")
                    msg      = EmailMessage()
                    username = str(UserName)
                    password = str(Password)
                    to       = To_Email
                    subject  = str(Subject)
                    body     = str(Body)
                    msg['subject'] = subject
                    msg['from'] = username
                    msg['to'] = to
                    msg.set_content(body)
                    attachments=[]
                    filename1 = str("D:/Bulk_Mail_Flask/Attachments/"+attach1)
                    attachments.append(filename1)
                    filename2 = str('D:/Bulk_Mail_Flask/Attachments/'+attach2)
                    attachments.append(filename2)
                    #print(attachments)
                    for i in range(0,len(attachments),1):
                        with open(attachments[i], 'rb') as f:
                            file_data = f.read()
                            print(attachments[i])
                        msg.add_attachment(file_data, maintype='application', subtype='octet-stream', filename=f.name)
                    if username=="" or password=="" or to=="" or subject=="" or body=="":
                        print("All fields required")
                    else:
                        server   = smtplib.SMTP('smtp.gmail.com',587)
                        server.starttls()
                        server.login(username, password)
                        server.send_message(msg)
                        print("Email Delivried")
                        new_credit=credits-1
                        credits=new_credit
                        result="Successfully"
                        print(new_credit)
                except:
                    print("Error Sending Mail")
                    result="Not Successfully"
                    new_credit=credit
                    print(new_credit) 
        return result,new_credit   
#status,credits_remain=maincall("info.weedirect@gmail.com","weedirect@123","hello","helo","Email.csv","imagesd.png","imagesd.png",credit)
#print(status,credits_remain)
