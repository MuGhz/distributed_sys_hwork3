from flask import Flask
from flask import request
import requests
import json
import datetime

def get_time()
	r = requests.get('http://172.17.0.70:17088',)
	response = json.loads(r.text)
	return response['state']

def error(code):
	return 'ERROR '+code+'\n'



@app.route('/api/hello',methods=['GET','POST'])
def hello():
	if request.method  == 'POST':
		if request.m
		time=str(datetime.datetime.now())
		
	else:
		return error('404')

@app.route('/api/plus_one/{var}',methods=['GET'])
def plus_one(var):
	do_plus_one()
