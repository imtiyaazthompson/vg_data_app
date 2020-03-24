import chrono

# Log any useful information

# Write log entry to the terminal and given file
# info - Tuple of 3 elements - PLACE,MSG_TYPE,MSG
def log(info,logf):
	time = chrono.now()
	log = '[{}][{}][{}] {}'.format(time,info[0],info[1],info[2])
	print(log)
	logf.write('{}\n'.format(log))

# Write log to the terminal only
# info - Tuple of 3 elements - PLACE,MSG_TYPE,MSG
def log_terminal_only(info):
	time = chrono.now()
	log = '[{}][{}][{}] {}'.format(time,info[0],info[1],info[2])
	print(log)
