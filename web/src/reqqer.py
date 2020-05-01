import requests as req
import json
import traceback
#from . import logger as lg
#from . import diskify
import logger as lg
from apic_engine import AQuery

API = 'https://api-v3.igdb.com'
KEY = ''
#REQ_HEAD = {'user-key':KEY} # Required by IGDB

#TODO build a similarity tree visualization
class Request:

	def __init__(self,api,apikey):
		self.request_header = {'user-key':apikey}
		self.api = api
		self.endpoint = None
		self.resp = None
		self.status = None

	def set_endpoint(self,end):
		self.endpoint = self.api + end

	def get(self,request_params):
		try:
			self.resp = req.get(self.endpoint,headers=self.request_header,params=req_params)
			self.status = self.resp.status_code
			lg.log_terminal_only(('GET','LOG','code: {}'.format(self.status)))
			self.dump()
		except Exception as e:
			lg.log_terminal_only(('REQUEST_GET','ERROR','\nSTACK\n{}'.format(traceback.format_exc())))

	def post(self,request_body):
		try:
			self.resp = req.post(self.endpoint,headers=self.request_header,data=request_body)
			self.status = self.resp.status_code
			lg.log_terminal_only(('POST','LOG','code: {}'.format(self.status)))
			self.dump()
		except Exception as e:
			lg.log_terminal_only(('REQUEST_POST','ERROR','\nSTACK\n{}'.format(traceback.format_exc())))
		
	def json(self):
		try:
			return self.resp.json()
		except Exception as e:
			lg.log_terminal_only(('REQUEST_JSON','ERROR','\nSTACK\n{}'.format(traceback.format_exc())))

	def raw(self):
		try:
			return self.resp.text
		except Exception as e:
			lg.log_terminal_only(('REQUEST_RAW','ERROR','\nSTACK\n{}'.format(traceback.format_exc())))

	def encoding(self):
		try:
			return self.resp.encoding
		except Exception as e:
			lg.log_terminal_only(('REQUEST_ENC','ERROR','\nSTACK\n{}'.format(traceback.format_exc())))

	def get_status(self):
		try:
			return self.status
		except Exception as e:
			lg.log_terminal_only(('REQUEST_STAT','ERROR','\nSTACK\n{}'.format(traceback.format_exc())))	

	def dump(self):
		try:
			f = open('response_dump.txt','w')
			f.write(self.raw())
			f.close()
			lg.log_terminal_only(('DUMP','LOG','DUMPED RESPONSE TO FILE'))
		except Exception as e:
			lg.log_terminal_only(('REQUEST_DUMP','ERROR','\nSTACK\n{}'.format(traceback.format_exc())))



def main():
	r = Request(API,KEY)
	r.set_endpoint('/games/')

	query_str = 'search "nioh";fields name,genres.slug,rating,similar_games.name;limit 10;'
	body = AQuery(query_str)

	r.post(body.get_query())
	r.dump()
	j = r.json()
	print('Type of json: {}'.format(type(j)))
	print('Size of json: {}'.format(len(j)))
	print('Investigate')
	print(type(j[0]))
	print(j[5])

if __name__ == '__main__':
	main()
