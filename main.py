from flask import Flask, flash, render_template, request
import json   
import boto3
import pathlib
import os
import requests
import mysql.connector

app = Flask(__name__)
@app.route("/", methods=['post', "get"])
def index ():
    return render_template('index.html')

userId = 1
end="cloudfinaldb.cl7uutdsqhvw.us-east-1.rds.amazonaws.com"
port="3306"
user="admin"
reg="us-east-1c"
db="clouddb"

apiEndPoint = 'https://k8mv8phphj.execute-api.us-east-1.amazonaws.com/default/send_email_cloud'
with open('C:/Users/rravula/OneDrive - UAB - The University of Alabama at Birmingham/Desktop/key.json', 'r') as keys:
    aws_key = json.load(keys)

s3_g = boto3.client('s3')
@app.route("/submitForm", methods=['post'])
def submitForm():
    username = request.form["userName"]
    password = request.form["password"]
    try:
        query = "select * from user where user.username='"+ username + "' &&  user.password = '"+ password + "'"
        results = executeQuery(query)
        if results != []:
            return render_template('fileshare.html', status = False)
        else:
            return render_template("index.html")
    except Exception as e:
        print("Error occured", format(e))  
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
    res = s3.Bucket(aws_key['bucket']).upload_file('./Cloud_Assign_4.pdf', 'sample_cloud')
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
    path = s3_g.generate_presigned_url('get_object', Params={'Bucket': aws_key['bucket'], 'Key': 'sample_cloud'}, ExpiresIn=3600)
    mail = ",".join(mailObj)
    qry = "Insert into record(userId, mail) values('"+userId+"','"+mail+"')"
    executeQuery(qry)
    event = {
        'body':"Hi, Please find the below link of s3",
        "link": path,
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

def create_presigned_url(bucket_name, object_name, expiration=3600):
    s3_c = boto3.client('s3')
    s3_c.generate_presigned_url('get_object', Params={'Bucket': bucket_name, 'Key': object_name}, ExpiresIn=expiration)

def executeQuery(qry):
    print(qry)
    conn =  mysql.connector.connect(host=end, user=user, passwd='ravibabu', port=port, database=db, ssl_ca='SSLCERTIFICATE')
    cur = conn.cursor()
    cur.execute(qry)
    res = cur.fetchall()
    return res


if __name__ == '__main__':
    app.run()


 
