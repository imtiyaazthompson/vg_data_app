import requests as req

API = 'https://api-v3.igdb.com'
KEY = 'cda00748d56ce784ef194c4634310970'
REQ_HEAD = {'user-key':KEY} # Required by IGDB

# TODO
# Parse specific game info from /games/ -> depends on what your app is going to be about
# Depending on the app, use the relevant info from /games/ to search other endpoints
# Caching
# Learn Apicalypse query language for RESTful APIs, Create a apicalypse_python wrapper to process 

# Interesting endpoints the API exposes
ENDPOINT = {
	'artwork':'/artwork/',
	'characters':'/characters/',
	'cms':'/character_mug_shot/',
	'series':'/collection/',
	'cover_art':'/covers/',
	'games':'/games/',
	'mode':'/game_modes/',
	'versions':'/game_versions/',
	'vfeatures':'/game_version_features/',
	'genres':'/genres/',
	'tags':'/keywords/',
	'platforms':'/platforms/',
	'ratings':'/count/',
	'release_dates':'/release_dates/',
	'search':'/search/',
	'themes':'/themes/'
}

def test_endpoint(endpoint):
	response = req.get(API, headers=REQ_HEAD) # request header included
	print(response.status_code)
	return response

'''
	IGDB requires the data for a POST request to be in byte form - a string
	Keywords: fields, limit, where, exclude
	The data is basically a query language, since when we make a post
	we are querying for a subset of data

	Where fields refer to the various information to be gathered at an
	endpoint
	
	where can be used to filter information at and endpoint
	Example:
		'fields name; where count > 75'
	count represents the review score for a specific game
	
	keywords (queries) must seperated by ;

	The games endpoint has fields with numerical values - IDs
	that must be used to extrapolate data from other endpoints
'''
def post_to(endpoint):
	response = req.post(API + endpoint, headers=REQ_HEAD, data="fields name,genres,tags; where name \"Final Fantasy\";")
	print(response.status_code)
	return response

def dump_endpoint(response, fname):
	f = open(fname, 'w')
	f.write(response)
	f.close()
	

def jsonify(response):
	return response.json()

data = {
	'fields':['name']
}
r = post_to(ENDPOINT['games']) 
dump_endpoint(r.text, 'output.txt')
