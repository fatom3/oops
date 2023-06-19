jfrom flask import *
import os,json
import requests


app = Flask(__name__)


@app.route('/')
def main():
	return "This site made with https://t.me/ClassError !"

@app.route('/ai')
def ai():
	query = request.args.get('query')
	headers = {
            'Host': 'us-central1-chat-for-chatgpt.cloudfunctions.net',
            'Connection': 'keep-alive',
            'If-None-Match': 'W/"1c3-Up2QpuBs2+QUjJl/C9nteIBUa00"',
            'Accept': '*/*',
            'User-Agent': 'com.tappz.aichat/1.2.2 iPhone/15.6.1 hw/iPhone8_2',
            'Content-Type': 'application/json',
            'Accept-Language': 'en-GB,en;q=0.9'
	}
	data = {
            'data': {
                'message': query,
        }
    }
	url = 'https://us-central1-chat-for-chatgpt.cloudfunctions.net/basicUserRequestBeta'
	response = requests.post(url, headers=headers, data=json.dumps(data))
	try:
		result = response.json()["result"]["choices"][0]["text"]
		return {"done":"ok","result":result}
	except:
		return {"done":"error"}
		
@app.route('/chat')
def chat():
	query = request.args.get('query')
	headers = {
            'Host': 'us-central1-chat-for-chatgpt.cloudfunctions.net',
            'Connection': 'keep-alive',
            'If-None-Match': 'W/"1c3-Up2QpuBs2+QUjJl/C9nteIBUa00"',
            'Accept': '*/*',
            'User-Agent': 'com.tappz.aichat/1.2.2 iPhone/15.6.1 hw/iPhone8_2',
            'Content-Type': 'application/json',
            'Accept-Language': 'en-GB,en;q=0.9'
	}
	data = {
            'data': {
                'message': query,
        }
    }
	url = 'https://us-central1-chat-for-chatgpt.cloudfunctions.net/basicUserRequestBeta'
	response = requests.post(url, headers=headers, data=json.dumps(data))
	try:
		result = response.json()["result"]["choices"][0]["text"]
		return {"done":"ok","result":result}
	except:
		return {"done":"error"}
		

@app.route('/To-En')
def toen():
	query = request.args.get('query')
	headers = {
            'Host': 'us-central1-chat-for-chatgpt.cloudfunctions.net',
            'Connection': 'keep-alive',
            'If-None-Match': 'W/"1c3-Up2QpuBs2+QUjJl/C9nteIBUa00"',
            'Accept': '*/*',
            'User-Agent': 'com.tappz.aichat/1.2.2 iPhone/15.6.1 hw/iPhone8_2',
            'Content-Type': 'application/json',
            'Accept-Language': 'en-GB,en;q=0.9'
	}
	data = {
            'data': {
                'message': "Translate into English only : \n " + query,
            }
	}
	url = 'https://us-central1-chat-for-chatgpt.cloudfunctions.net/basicUserRequestBeta'
	response = requests.post(url, headers=headers, data=json.dumps(data))
	try:
		result = response.json()["result"]["choices"][0]["text"]
		return {"done":"ok","result":result}
	except:
		return {"done":"error"}

@app.route('/To-Ar')
def toar():
	query = request.args.get('query')
	headers = {
            'Host': 'us-central1-chat-for-chatgpt.cloudfunctions.net',
            'Connection': 'keep-alive',
            'If-None-Match': 'W/"1c3-Up2QpuBs2+QUjJl/C9nteIBUa00"',
            'Accept': '*/*',
            'User-Agent': 'com.tappz.aichat/1.2.2 iPhone/15.6.1 hw/iPhone8_2',
            'Content-Type': 'application/json',
            'Accept-Language': 'en-GB,en;q=0.9'
	}
	data = {
            'data': {
                'message': "Translate into Arabic only : \n " + query,
            }
	}
	url = 'https://us-central1-chat-for-chatgpt.cloudfunctions.net/basicUserRequestBeta'
	response = requests.post(url, headers=headers, data=json.dumps(data))
	try:
		result = response.json()["result"]["choices"][0]["text"]
		return {"done":"ok","result":result}
	except:
		return {"done":"error"}

@app.route('/explane')
def expl():
	query = request.args.get('query')
	headers = {
            'Host': 'us-central1-chat-for-chatgpt.cloudfunctions.net',
            'Connection': 'keep-alive',
            'If-None-Match': 'W/"1c3-Up2QpuBs2+QUjJl/C9nteIBUa00"',
            'Accept': '*/*',
            'User-Agent': 'com.tappz.aichat/1.2.2 iPhone/15.6.1 hw/iPhone8_2',
            'Content-Type': 'application/json',
            'Accept-Language': 'en-GB,en;q=0.9'
	}
	data = {
            'data': {
                'message': " Explain and analyze the code only, and if I ask you about any other question, tell me that I could not find the codes Just : \n " + query,
	}
	}
	url = 'https://us-central1-chat-for-chatgpt.cloudfunctions.net/basicUserRequestBeta'
	response = requests.post(url, headers=headers, data=json.dumps(data))
	try:
		result = response.json()["result"]["choices"][0]["text"]
		return {"done":"ok","result":result}
	except:
		return {"done":"error"}
		

@app.route('/Rv-Ar')
def evar():
	query = request.args.get('query')
	headers = {
            'Host': 'us-central1-chat-for-chatgpt.cloudfunctions.net',
            'Connection': 'keep-alive',
            'If-None-Match': 'W/"1c3-Up2QpuBs2+QUjJl/C9nteIBUa00"',
            'Accept': '*/*',
            'User-Agent': 'com.tappz.aichat/1.2.2 iPhone/15.6.1 hw/iPhone8_2',
            'Content-Type': 'application/json',
            'Accept-Language': 'en-GB,en;q=0.9'
	}
	data = {
            'data': {
                'message': "صحح لي باللغة العربية هذي الجملة من الاخطاء نحوية و الاملائية : \n " + query,
            }
	}
	url = 'https://us-central1-chat-for-chatgpt.cloudfunctions.net/basicUserRequestBeta'
	response = requests.post(url, headers=headers, data=json.dumps(data))
	try:
		result = response.json()["result"]["choices"][0]["text"]
		return {"done":"ok","result":result}
	except:
		return {"done":"error"}


@app.route('/Rv-En')
def even():
	query = request.args.get('query')
	headers = {
            'Host': 'us-central1-chat-for-chatgpt.cloudfunctions.net',
            'Connection': 'keep-alive',
            'If-None-Match': 'W/"1c3-Up2QpuBs2+QUjJl/C9nteIBUa00"',
            'Accept': '*/*',
            'User-Agent': 'com.tappz.aichat/1.2.2 iPhone/15.6.1 hw/iPhone8_2',
            'Content-Type': 'application/json',
            'Accept-Language': 'en-GB,en;q=0.9'
	}
	data = {
            'data': {
                'message': "Just correct the mistakes in the English words only : \n " + query,
            }
	}
	url = 'https://us-central1-chat-for-chatgpt.cloudfunctions.net/basicUserRequestBeta'
	response = requests.post(url, headers=headers, data=json.dumps(data))
	try:
		result = response.json()["result"]["choices"][0]["text"]
		return {"done":"ok","result":result}
	except:
		return {"done":"error"}
	
if __nname__=="__mmain__":
	app.run(port=81,host="0.0.0.0",debug=True)

