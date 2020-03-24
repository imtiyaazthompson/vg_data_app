import requests as req
import logger as lg

# GET request wrapper
def GET(api,endpoint,header,req_params):
	try:
		resp = req.get(api + endpoint,headers=header,params=req_params)
		lg.log_terminal_only(('REQQER','GET',resp))
		stat = resp.status_code
		lg.log_terminal_only(('REQQER','GET',stat))
		return (resp,stat)
	except Exception as e:
		lg.log_terminal_only(('REQQER','ERROR',str(e)))
		return (None,-1)

# POST request wrapper
def POST(api,endpoint,header,body):
	try:
		resp = req.post(api + endpoint,headers=header,data=body)
		lg.log_terminal_only(('REQQER','POST',resp))
		stat = resp.status_code
		lg.log_terminal_only(('REQQER','POST',stat))
		return (resp,stat)
	except Exception as e:
		lg.log_terminal_only(('REQQER','ERROR',str(e)))
		return (None,-1)
# Get the JSON of a response
def jsonify(response):
	try:
		ret = response.json()
		return ret
	except Exception as e:
		lg.log_terminal_only(('REQQER','ERROR',str(e)))
		return None
# Get the raw html of a response
def textify(response):
	try:
		ret = response.text
		return ret
	except Exception as e:
		lg.log_terminal_only(('REQQER','ERROR',str(e)))
		return None
# Get the character encoding of the response
def get_encoding(response):
	try:
		ret = response.encoding
		return ret
	except Exception as e:
		lg.log_terminal_only(('REQQER','ERROR',str(e)))
		return None
