from flask import Flask,request,render_template,redirect
import client

# NOTE: url_for builds a url for a function, and takes in kwargs for its arguments, still requires a route

# Store large amounts of session data with a global variable
sub_titles = []
app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')


@app.route('/get_name',methods=['POST','GET'])
def get_name():
	# Get form data	
	name = request.form['title']
	qs = client.build_query(name)
	data = client.setup(qs)
	client.parse_json(data)
	return redirect('/results/{}'.format(name))

@app.route('/results/<name>')
def results(name):
	# response is global
	
	qs = client.build_query(name)
	response = client.setup(qs)
	client.parse_json(response)

	for item in response:
		for game in item['similar_games']:
			sub_titles.append(game)
	return render_template('results.html',data=response)

@app.route('/similar/<name>')
def similar(name):
	for item in sub_titles:
		if item['name'] == name:
			current_game = item
			break

	return render_template('results_inner.html',game=current_game)

if __name__ == '__main__':
	app.run(debug=True)
