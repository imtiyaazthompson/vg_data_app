import sys
sys.path.append('/src')

from flask import Flask,request,render_template
from src import chrono,logger,reqqer,apic_engine,igdb_procs

app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/proc_title',methods=['GET','POST'])
def proc_title():
	title = request.form['gname']

	payload = {
		'search':title,
		'fields':'name,rating,videos.video_id,videos.name',
		'exclude':'',
		'where':'videos.video_id != null',
		'limit':10,
		'offset':0,
		'sort':''
	}
	query = apic_engine.run_engine('APP',payload)
	resp,code = reqqer.POST(API,'/games/',REQ_HEAD,query)
	data = []
	jresp = reqqer.jsonify(resp)
	for entry in jresp:
		keys = entry.keys()
		gname = entry['name']
		if 'rating' in keys:
			rating = entry['rating']
		else:
			rating = 'Not available'
		vids = []
		for video in entry['videos']:
			vname = video['name']
			vurl = igdb_procs.process_video_id(video['video_id'])
			chunk = (vname,vurl)
			vids.append(chunk)
			print(chunk)
		data.append((gname,rating,vids)) 
	return render_template('results.html',title=title,resp=data)

if __name__ == '__main__':
	API = 'https://api-v3.igdb.com'
	KEY = 'cda00748d56ce784ef194c4634310970'
	REQ_HEAD = {'user-key':KEY} # Required by IGDB

	app.run(debug=True)
