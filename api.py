from flask import Flask,request,jsonify
from peewee import *
from models import *
import requests
import json
import datetime
import yaml
import socket

database = SqliteDatabase('database.db')
app = Flask(__name__)
spek = yaml.load(open('/root/api/spesifikasi.yaml'))

def yaml_ip():
	hostname = socket.gethostbyname(socket.gethostname())
	spek['host']= hostname+':12032'

def get_time():
	r = requests.get('http://172.17.0.70:17088',)
	response = json.loads(r.text)
	return response['state']

def error_code(code):
	title = ''
	detail = ''
	if code == '400':
		detail = "'request' is a required property "
		title = 'Bad Request'
	elif code == '404':
		detail = "The requested URL was not found on the server. If you entered the URL manually please check your spelling and try again."
		title = 'Not Found'
	elif code == '405':
		detail = "Service call for the URL is not allowed"
		title = "Not Allowed"
	return jsonify(code=code,detail=detail,title=title),int(code)

@app.before_request
def _db_connect():
	database.connect()

@app.teardown_request
def _db_close(exc):
	if not database.is_closed():
		database.close()

@app.route('/api/hello',methods=['GET','POST'])
def hello():
	if request.method  == 'POST':
		req = json.loads(request.data.decode("utf-8"))['request']
		if req != None:
			count =1
			user_request, created = User_count.get_or_create(name=req)
			user_request.count += 1
			user_request.save()  
			time=str(datetime.datetime.now())
			response = 'Good '+get_time()+', '+req
			apiversion = spek['info']['version']
			return jsonify(response=response,currentvisit=time,apiversion=apiversion,count=user_request.count),200
		else:
			return error_code('400')
	else:
		return error_code('405')

@app.route('/api/plus_one/<int:integer>',methods=['GET'])
def plus_one(integer):
	if integer > 0:
		return jsonify(plusoneret=integer+1,apiversion=spek['info']['version']),200
	else:
		return error_code('404')

@app.route('/api/spesifikasi.yaml')
def spesifikasi():
	yaml_ip()
	return str(spek)

@app.errorhandler(404)
def not_found(e):
	return error_code('404')
