from apic_engine import AQuery
from reqqer import Request
from igdb_media import IGDBimage,IGDBvideo
import logger as lg

def setup(qs):
	query = AQuery(qs)
	# api,key
	r = Request('https://api-v3.igdb.com','cda00748d56ce784ef194c4634310970')
	r.set_endpoint('/games')

	r.post(query.get_query())
	if r.get_status() != 200:
		return -1
	else:
		return r.json()


def generate_cover_urls(url):
	return IGDBimage(url).get_medium()

def parse_json(json):
	# Restrict to top 3 similar games
	subset = []
	for item in json:
		if 'cover' in item:
			item['cover'] = generate_cover_urls(item['cover']['url'])
		else:
			item['cover'] = 'No available cover art'


		if 'rating' in item:
			item['rating'] = int(item['rating'])
		else:
			item['rating'] = 0

		for game in item['similar_games']:
			if 'cover' in game:
				game['cover'] = generate_cover_urls(game['cover']['url'])
			else:
				game['cover'] = 'No available cover art'


			if 'rating' in game:
				game['rating'] = int(game['rating'])
			else:
				game['rating'] = 0

		similar = sorted(item['similar_games'],key = lambda i:i['rating'],reverse=True)
		similar = similar[:3]
		item['similar_games'] = similar
		
		subset.append(item)

	json = sorted(json,key=lambda i:i['rating'],reverse=True)
				

def build_query(search_param):
	search = 'search "{}";'.format(search_param)

	fields = '''
			fields
			name,genres.name,platforms.name,rating,rating_count,release_dates.human,
			cover.url,similar_games.name,similar_games.genres.name,similar_games.rating,
			similar_games.rating_count,similar_games.release_dates.human,similar_games.cover.url,
			similar_games.platforms.name,summary,similar_games.summary,
			parent_game,bundles;
		 '''

	where = '''
			where parent_game = null & 
			similar_games != null & 
			similar_games.rating != null &
			version_parent = null &
			platforms != [34,39,73,74];
		'''

	limit = 'limit 10;'
	query = (search + fields + where + limit)
	#lg.log_terminal_only(('CLIENT','QUERY','\n{}'.format(query)))
	return query

def main():
	q = build_query('sonic forces')
	json = setup(q)
	parse_json(json)

if __name__ == '__main__':
	main()
