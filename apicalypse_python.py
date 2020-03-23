# Return a `fields` query
def generate_request(req_data, keyword, delim):
	r =  '{} {};'.format(keyword, delim.join(req_data))
	return r

def generate_exclusion(excl_data):
	return generate_request(excl_data,'exclude',',')

def generate_fields(field_data):
	return generate_request(field_data,'fields',',')


# data - list of field names filter on
# constraints - list, whose indices match the indices of the data[]
# must contain an operator followed by a string or integer
# delim can be ' & ' or ' | '
def generate_filter(data, constraints, logic):
	if len(data) != len(constraints):
		print('Invalid filter.')
		return
	
	data_f = []
	for i in range(len(data)):
		data_f.append('{} {}'.format(data[i],constraints[i]))

	if len(data_f) == 1:
		return generate_request(data_f,'where','')
	elif logic == 'AND':
		return generate_request(data_f,'where',' & ')
	elif logic == 'OR':
		return generate_request(data_f,'where',' | ')
	else:
		print('Some error when interpreting clause: "where"')
		return
		 

def generate_limit(limit):
	l = [str(limit)]
	return generate_request(l,'limit', '')

def generate_offset(offset):
	o = [str(offset)]
	return generate_request(o,'offset','')


def generate_sort(field, order):
	f = [field,order]
	return generate_request(f,'sort', ' ')


def generate_search(column,search_str):
	c = [column,search_str]
	return generate_request(c,'search',' ')

def compile_query(data):
	fields = data['fields'].split(',')
	data_f = data['data'].split(',')
	constraints = data['constraints'].split(',')
	logic = data['logic']
	limit = data['limit']
	offset = data['offset']
	sort = data['sort']
	order = data['order']
	print(fields)

	r = generate_fields(fields) + generate_filter(data_f,constraints,logic) + generate_limit(limit) + generate_offset(offset) + generate_sort(sort,order)
	print(r)
	return r


def main():
	fields = ['name','aggregated_rating','popularity']
	data = ['aggregated_rating','popularity']
	constraints = ['> 75', '> 2.5']
	limit = 20
	offset = 10
	sort = 'aggregated_rating'
	order = 'asc'

	full_query = ''
	full_query += generate_fields(fields) + generate_filter(data,constraints,'AND') + generate_limit(limit) + generate_offset(offset) + generate_sort(sort,order)

	print(full_query)

#main()
	
