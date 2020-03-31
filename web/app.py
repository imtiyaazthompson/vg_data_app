import sys
sys.path.append('/src')

from flask import Flask,request,render_template,redirect
from src import reqqer,apic_engine,igdb_procs

app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/proc_title',methods=['GET','POST'])
def proc_title():
	title = request.form['gname']

	payload = {
		'search':title,
		'fields':'name,similar_games.name,rating,similar_games.rating,category,similar_games.category,\
			  summary,similar_games.summary,cover.url,similar_games.cover.url',
		'exclude':'category',
		'where':'category = 0 & similar_games.category = 0 & cover.url != null & similar_games.cover.url != null',
		'limit':10,
		'offset':0,
		'sort':''
	}
	query = apic_engine.run_engine('APP',payload)
	resp,code = reqqer.POST(API,'/games/',REQ_HEAD,query)
	jresp = reqqer.jsonify(resp)
	print(jresp)
	del global_results[:] # Flush Global Data
	for entry in jresp:
		data = []
		keys_g = entry.keys()
		name = entry['name']
		if 'rating' in keys_g:
			rating = '{}'.format(round(float(entry['rating']),2))
		else:
			rating = 'Not Available'
		summary = entry['summary']
		cover = igdb_procs.process_image_url(entry['cover']['url'],'med')
		for game in entry['similar_games']:
			keys_s = game.keys()
			sname = game['name']
			if 'rating' in keys_s:
				srating = game['rating']
			else:
				srating = 'Not available'
			
			ssummary = game['summary']
			if 'cover' in keys_s:
				scover = igdb_procs.process_image_url(game['cover']['url'],'med')
			else:
				scover = None
			data.append((sname,srating,ssummary,scover))
		global_results.append((name,rating,summary,cover,data))
		
	return redirect('/results')
	# return render_template('results.html',title=title,resp=data)


@app.route('/results')
def results():
	return render_template('results.html',resp=global_results)


if __name__ == '__main__':
	API = 'https://api-v3.igdb.com'
	KEY = 'cda00748d56ce784ef194c4634310970'
	REQ_HEAD = {'user-key':KEY} # Required by IGDB
	global_results = []

	app.run(debug=True)
