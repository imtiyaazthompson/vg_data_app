import logger as lg

def get_search(mode):
	if mode == 'DEBUG':
		r = input('SEARCH: ')
		return ('search {};'.format(r)) if r != '' else ''
	elif mode == 'APP':
		pass

def get_fields(mode):
	if mode == 'DEBUG':
		r = input('FIELDS: ')
		return ('fields {};'.format(r)) if r != '' else ''
	elif mode == 'APP':
		pass

def get_exclude(mode):
	if mode == 'DEBUG':
		r = input('EXCLUDE: ')
		return ('exclude {};'.format(r)) if r != '' else ''
	elif mode == 'APP':
		pass

def get_where(mode):
	if mode == 'DEBUG':
		r = input('WHERE: ')
		return ('where {};'.format(r)) if r != '' else ''
	elif mode == 'APP':
		pass

def get_limit(mode):
	if mode == 'DEBUG':
		r = input('LIMIT: ')
		return ('limit {};'.format(r)) if r != '' else ''
	elif mode == 'APP':
		pass

def get_offset(mode):
	if mode == 'DEBUG':
		r = input('OFFSET: ')
		return ('offset {};'.format(r)) if r != '' else ''
	elif mode == 'APP':
		pass

def get_sort(mode):
	if mode == 'DEBUG':
		r = input('SORT:')
		return ('sort {};'.format(r)) if r != '' else ''
	elif mode == 'APP':
		pass

def run_engine(mode='DEBUG'):
	query = []
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
