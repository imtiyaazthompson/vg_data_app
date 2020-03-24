import reqqer as req
import apic

API = 'https://api-v3.igdb.com'
KEY = 'cda00748d56ce784ef194c4634310970'
REQ_HEAD = {'user-key':KEY} # Required by IGDB

# TODO
# Parse specific game info from /games/ -> depends on what your app is going to be about
# Depending on the app, use the relevant info from /games/ to search other endpoints
# Caching

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

def test_endpoint():
	response = req.GET(API,ENDPOINT['games'],REQ_HEAD,{}) # request header included

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
# Note on apicalypse -> to access the members of a field, use the dot operator
# Example collection.name returns the name of the collection
def post_to(endpoint, body):
	response = req.post(API + endpoint, headers=REQ_HEAD, data=body)
	print(response.status_code)
	return response

def dump_endpoint(response, fname):
	f = open(fname, 'w')
	f.write(response)
	f.close()
	

def jsonify(response):
	return response.json()

# Construct the request body to form and apicalypse query
# Fields can be dot seperated to indicate entries from a given field
# if it exists in the API
# Example: genres -> returns an array of genre IDS
# but genres.slug -> returns an array of the names of the genres
def build_req_body(fld,excl,data,constr,logic,lim,off,sort,order):
	body = {
		'fields':fld,
		'exclude':excl,
		'data':data,
		'constraints':constr,
		'logic':logic,
		'limit':lim,
		'offset':off,
		'sort':sort,
		'order':order
	}
	return body
def client():
	data = build_req_body('name,rating,genres.slug,collection.slug','rating','collection.name','= "Sonic"','',10,0,'','')
	request_body = apic.compile_query(data)

	resp,code = req.POST(API,ENDPOINT['games'],REQ_HEAD,request_body)
	dump_endpoint(req.textify(resp), 'output.txt')

client()
