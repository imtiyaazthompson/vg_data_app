from . import logger as lg

# Search is used to search for specific titles
# for any given endpoint
# Search also has its own endpoint
def get_search(mode,search=''):
	if mode == 'DEBUG':
		r = input('SEARCH: ')
		return ('search {};'.format(r)) if r != '' else ''
	elif mode == 'APP':
		return ('search "{}";'.format(search)) if search != '' else ''

def get_fields(mode,fields=''):
	if mode == 'DEBUG':
		r = input('FIELDS: ')
		return ('fields {};'.format(r)) if r != '' else ''
	elif mode == 'APP':
		return ('fields {};'.format(fields)) if fields != '' else ''

def get_exclude(mode,exclude=''):
	if mode == 'DEBUG':
		r = input('EXCLUDE: ')
		return ('exclude {};'.format(r)) if r != '' else ''
	elif mode == 'APP':
		return ('exclude {};'.format(exclude)) if exclude != '' else ''

# To test for values that are null, use '!= null'
def get_where(mode,where=''):
	if mode == 'DEBUG':
		r = input('WHERE: ')
		return ('where {};'.format(r)) if r != '' else ''
	elif mode == 'APP':
		return ('where {};'.format(where)) if where != '' else ''

def get_limit(mode,limit=''):
	if mode == 'DEBUG':
		r = input('LIMIT: ')
		return ('limit {};'.format(r)) if r != '' else ''
	elif mode == 'APP':
		return ('limit {};'.format(limit)) if limit != '' else ''

def get_offset(mode,offset=''):
	if mode == 'DEBUG':
		r = input('OFFSET: ')
		return ('offset {};'.format(r)) if r != '' else ''
	elif mode == 'APP':
		return ('offset {};'.format(offset)) if offset != '' else ''

def get_sort(mode,sort=''):
	if mode == 'DEBUG':
		r = input('SORT:')
		return ('sort {};'.format(r)) if r != '' else ''
	elif mode == 'APP':
		return ('sort {};'.format(sort)) if sort != '' else ''

def run_engine(mode='DEBUG',payload=None):
	query = []

	if payload != None:
		query.append(get_search(mode,payload['search']))
		query.append(get_fields(mode,payload['fields']))
		query.append(get_exclude(mode,payload['exclude']))
		query.append(get_where(mode,payload['where']))
		query.append(get_limit(mode,payload['limit']))
		query.append(get_offset(mode,payload['offset']))
		if query[0] == '':
			query.append(get_sort(mode,payload['sort']))

	else:
		query.append(get_search(mode))
		query.append(get_fields(mode))
		query.append(get_exclude(mode))
		query.append(get_where(mode))
		query.append(get_limit(mode))
		query.append(get_offset(mode))
		if query[0] == '':
			query.append(get_sort(mode))
	
	q = compile_query(query)
	lg.log_terminal_only(('AE','QRY',q))
	return q

def compile_query(query):
	return ''.join(query)


def main():
	run_engine()

if __name__ == '__main__':
	main()
