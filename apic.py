import logger as lg

# Master request generator
# Generate a the proper subquery from a given dataset
# keyword -> clause
# delim -> what to join the data set (list) by
def generate_request(req_data, keyword, delim):
	lg.log_terminal_only(('APIC','REQGEN',req_data))
	r =  '{} {};'.format(keyword, delim.join(req_data))
	return r

# Generate an exclusion query from a given data set
# By apicalypse standards, exclusion data is comma
# delimitted
def generate_exclusion(excl_data):
	lg.log_terminal_only(('APIC','EXCLGEN',excl_data))
	return generate_request(excl_data,'exclude',',')

# Generate a fields query from a given data set
# By apicalypse standards, fields data is comma
# delimitted
def generate_fields(field_data):
	lg.log_terminal_only(('APIC','FLDGEN',field_data))
	return generate_request(field_data,'fields',',')


# Generate a where query from a given data set
# and a list of constraints for each element of 
# that data set
# Constraints include an operator and value
# By apicalypse standards, where data is delimitted
# by either & or |
def generate_filter(data, constraints, logic):
	if len(data) != len(constraints):
		lg.log_terminal_only(('APIC','ERROR','Mismatch in constraints and data'))
		return
	
	data_f = []
	# Generate substrings consisting of the data and its constraint
	for i in range(len(data)):
		data_f.append('{} {}'.format(data[i],constraints[i]))

	if len(data_f) == 1:
		lg.log_terminal_only(('APIC','WHRGEN',data_f))
		return generate_request(data_f,'where','')
	elif logic == 'AND': # If & is used
		lg.log_terminal_only(('APIC','WHRGEN',data_f))
		return generate_request(data_f,'where',' & ')
	elif logic == 'OR': # If | is used
		lg.log_terminal_only(('APIC','WHRGEN',data_f))
		return generate_request(data_f,'where',' | ')
	else:
		lg.log_terminal_only(('APIC','ERROR','Some error when interpreting clause: "where"'))
		return
		 
# Generate a limit query from a given number
def generate_limit(limit):
	try:
		l = [str(limit)]
	except:
		lg.log_terminal_only(('APIC','ERROR','Invalid limit'))
	
	lg.log_terminal_only(('APIC','LTGEN',l))
	return generate_request(l,'limit', '')

# Generate an offset query from a given number
def generate_offset(offset):
	try:
		o = [str(offset)]
	except:
		lg.log_terminal_only(('APIC','ERROR','Invalid offset'))
	
	lg.log_terminal_only(('APIC','OFFGEN',o))
	return generate_request(o,'offset','')

# Generate a sort query based on a field
# and whether to sort in (asc)ending or
# (desc)ending order
def generate_sort(field, order):
	f = [field,order]
	lg.log_terminal_only(('APIC','SRTGEN',f))
	return generate_request(f,'sort', ' ')


def generate_search(column,search_str):
	c = [column,search_str]
	return generate_request(c,'search',' ')

# Compile the master query from smaller subqueries
# Expects a dictionary
def compile_query(data):
	fields = data['fields'].split(',')
	exclude = data['exclude'].split(',')
	data_f = data['data'].split(',')
	lg.log_terminal_only(('APIC','DATA',data_f))
	constraints = data['constraints'].split('\\')
	lg.log_terminal_only(('APIC','CSTR',constraints))
	logic = data['logic']
	limit = data['limit']
	offset = data['offset']
	sort = data['sort']
	order = data['order']
	
	f_q = generate_fields(fields) if (fields[0] != '' or fields[0] == '*') else ''
	e_q = generate_exclusion(exclude) if (exclude[0] != '' or exclude[0] == '*') else ''
	w_q = generate_filter(data_f,constraints,logic) if data_f[0] != '' else ''
	l_q = generate_limit(limit) if limit != '' else ''
	o_q = generate_offset(offset) if offset != '' else ''
	s_q = generate_sort(sort,order) if sort != '' else ''
	lg.log_terminal_only(('APIC','SUBQRY',(f_q,e_q,w_q,l_q,o_q,s_q)))	
	query = f_q + e_q  + w_q + l_q + o_q + s_q
	lg.log_terminal_only(('APIC','QUERY',query))
	return query


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
	
