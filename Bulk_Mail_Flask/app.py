__author__ = 'Ramanan'
from logging import root
from flask import Flask,render_template,request
from werkzeug.utils import secure_filename
from Main import  maincall
import os 
UPLOAD_FOLDER = 'D:/Bulk_Mail_Flask/DataBase'
UPLOAD_FOLDER1 = 'D:/Bulk_Mail_Flask/Attachments'


app=Flask(__name__, template_folder='templates')


app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['UPLOAD_FOLDER1'] = UPLOAD_FOLDER1


@app.route('/')
@app.route('/home')

def home():
    return render_template('register.html')

@app.route('/confirm',methods=['POST','GET'])
def register():
    if request.method =='POST':
        UserName = request.form.get('Username')
        Password = request.form.get('Password')
        Subject = request.form.get('subject')
        Body = request.form.get('body')
        f = request.files['file']
        f.save(os.path.join(app.config['UPLOAD_FOLDER'],f.filename))
        if request.files['attach1'].filename == '':
            print("No Files")
            attachment1_filename="imagesd.png"
        else:
            attachment1 = request.files['attach1']
            attachment1.save(os.path.join(app.config['UPLOAD_FOLDER1'],attachment1.filename))
            attachment1_filename = attachment1.filename
        if request.files['attach2'].filename == '':
            print("No Files")
            attachment2_filename="imagesd.png"
        else:
            attachment2 = request.files['attach2']
            attachment2.save(os.path.join(app.config['UPLOAD_FOLDER1'],attachment2.filename))
            attachment2_filename=attachment2.filename
        msg_status,credits_bal=maincall(UserName,Password,Subject,Body,f.filename,attachment1_filename,attachment2_filename)
        print(msg_status,credits_bal)

        return render_template("output.html",name_out=UserName,password_out=Password,subject_out=Subject,body_out=Body,Email_list=f.filename,Status_mail=msg_status,crd=credits_bal)             
if __name__ =="__main__":
    app.run(debug=True)
