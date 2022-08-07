from flask import Flask, flash, render_template, request
import json   
import boto3
import pathlib
import os
import requests

app = Flask(__name__)

@app.route("/", methods=['post', "get"])
def index ():
    return render_template('index.html')

userId ='rakeshravula'
pwd = '12345'

apiEndPoint = 'https://k8mv8phphj.execute-api.us-east-1.amazonaws.com/default/send_email_cloud'
with open('C:/Users/rravula/OneDrive - UAB - The University of Alabama at Birmingham/Desktop/key.json', 'r') as keys:
    aws_key = json.load(keys)
@app.route("/submitForm", methods=['post'])
def submitForm():
    user = request.form["userName"]
    password = request.form["password"]
    print('---', user, password)
    if user == userId and password == pwd:
        return render_template('fileshare.html', status = False)
    else: 
        return render_template("index.html")

    
@app.route("/uploadFile", methods=['post'])
def uploadFile():
    aws_access_key_id = aws_key['access_key']
    aws_secret_access_key= aws_key['secret_key']
    client = boto3.Session(
        aws_access_key_id ,
        aws_secret_access_key
    )
    s3 = client.resource('s3')
    
    res = s3.Bucket(aws_key['bucket']).upload_file('./Cloud_Assign_4.pdf', 'sample_cloud.txt')
    if res == None:
        return render_template('fileshare.html', status = True)
    return render_template('fileshare.html', status = False)

@app.route("/sendemail", methods=['post'])
def sendemail():
    mailObj = []
    index = 0
    if request.form['mail_1']:
        mailObj.insert(index, request.form['mail_1'])
        index +=1
    if request.form['mail_2']:
        mailObj.insert(index, request.form['mail_2'])
        index +=1
    if request.form['mail_3']:
        mailObj.insert(index, request.form['mail_3'])
        index +=1
    if request.form['mail_4']:
        mailObj.insert(index, request.form['mail_4'])
        index +=1
    if request.form['mail_5']:
        mailObj.insert(index, request.form['mail_5'])
        index +=1
    event = {
        'body':"Hi, Please find the below link of s3",
        "link": "www.google.com",
        "mail": mailObj
    }
    try:
        res=requests.post(apiEndPoint, json = event)
    except:
        return "unable to send request"
    return 'success'
@app.route("/report")
def report ():
    return render_template('report.html')

if __name__ == '__main__':
    app.run()


 