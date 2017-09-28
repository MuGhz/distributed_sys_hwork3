from flask import Flask,request,jsonify
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
		req = json.load(request.data.decode("utf-8"))['request']
		if req != None:
			time=str(datetime.datetime.now())
			response = 'Good '+get_time()
			apiversion = 1
		else:
			return error(400)
	else:
		return error('405')

@app.route('/api/plus_one/{var}',methods=['GET'])
def plus_one(var):
	do_plus_one()
